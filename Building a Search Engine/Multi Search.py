def multi_lookup(index, query):
    def make_url_pos (list):
        url_pos = {}
        if list:
            for entry in list:
                if entry[0] not in url_pos:
                    url_pos[entry[0]] = entry[1]
                else:
                    for pos in entry[1]:
                        url_pos[entry[0]].append(pos)
        return url_pos
    
    if not query:
        return []
    firstq = lookup(index, query[0])
    if firstq:
        firstq = firstq[:]
        for q in range(len(query)-1):
            toremove = []
            results = lookup(index, query[q+1])
            url_pos = make_url_pos (results)
            for entry in firstq:
                if entry[0] not in url_pos:
                    toremove.append(entry)
                else:
                    remove = True
                    toremove2 = []
                    for pos in entry[1]:
                        if (pos+q+1) in url_pos[entry[0]]:
                            remove = False
                        else:
                            toremove2.append(pos)
                    if remove:
                        toremove.append(entry)
                    else:
                        while toremove2:
                            entry[1].remove(toremove2.pop())                    
            while toremove:
                firstq.remove(toremove.pop())
                
    output = []
    if firstq:
        for entry in firstq:
            output.append(entry[0])
    return output


def crawl_web(seed): # returns index, graph of inlinks
    tocrawl = [seed]
    crawled = []
    #graph = {}  # <url>, [list of pages it links to]
    index = {} 
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            outlinks = get_all_links(content)
            #graph[page] = outlinks
            union(tocrawl, outlinks)
            crawled.append(page)
    return index#, graph


def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def add_page_to_index(index, url, content):
    words = content.split()
    for pos in range(len(words)):
        add_to_index(index, [words[pos], pos], url)
        
def add_to_index(index, keyword, url):
    if keyword[0] in index:
        for entry in index[keyword[0]]:
            if entry[0] == url:
                entry[1].append(keyword[1])
                return
        index[keyword[0]].append([url, [keyword[1]]])
    else:
        index[keyword[0]] = [[url,[keyword[1]]]]

def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    else:
        return None
    

cache = {
   'http://www.udacity.com/cs101x/final/multi.html': """<html>
<body>

<a href="http://www.udacity.com/cs101x/final/a.html">A</a><br>
<a href="http://www.udacity.com/cs101x/final/b.html">B</a><br>

</body>
""", 
   'http://www.udacity.com/cs101x/final/b.html': """<html>
<body>

Monty likes the Python programming language
Thomas Jefferson founded the University of Virginia
When Mandela was in London, he visited Nelson's Column.

</body>
</html>
""", 
   'http://www.udacity.com/cs101x/final/a.html': """<html>
<body>

Monty Python is not about a programming language
Udacity was not founded by Thomas Jefferson
Nelson Mandela said "Education is the most powerful weapon which you can
use to change the world."
</body>
</html>
""", 
}

def get_page(url):
    if url in cache:
        return cache[url]
    else:
        print "Page not in cache: " + url
        return None
    

#Here are a few examples from the test site:

index = crawl_web('http://www.udacity.com/cs101x/final/multi.html')

print multi_lookup(index, ['Python'])
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

print multi_lookup(index, ['Monty', 'Python'])
#>>> ['http://www.udacity.com/cs101x/final/a.html']

print multi_lookup(index, ['Python', 'programming', 'language'])
#>>> ['http://www.udacity.com/cs101x/final/b.html']

print multi_lookup(index, ['Thomas', 'Jefferson'])
#>>> ['http://www.udacity.com/cs101x/final/b.html', 'http://www.udacity.com/cs101x/final/a.html']

print multi_lookup(index, ['most', 'powerful', 'weapon'])
#>>> ['http://www.udacity.com/cs101x/final/a.html']

