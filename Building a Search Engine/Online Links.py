import urllib

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links=[]
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            return links

def get_page (url):
    return urllib.urlopen(url).read()


print "Please enter the URL you'd like to crawl"
url = raw_input()
html = get_page(url)
links = get_all_links(html)
for i in links:
    print i
