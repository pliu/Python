from random import randint


class IndexedHeap:
    def __init__(self, key_func=None):
        self.backing_list = []
        self.index = {}
        self.key_func = key_func

    def get(self, key):
        if key not in self.index:
            return None
        return self.backing_list[self.index[key]]

    def delete(self, o):
        key = self._key(o)
        if key not in self.index:
            return
        i = self.index[key]
        self._swap(i, len(self.backing_list) - 1)
        self.index.pop(key)
        self.backing_list.pop()
        self._bubble_down(self._bubble_up(i))

    def add(self, o):
        key = self._key(o)
        if key in self.index:
            return
        i = len(self.backing_list)
        self.index[key] = i
        self.backing_list.append(o)
        self._bubble_up(i)

    def peek(self):
        if not self.backing_list:
            return None
        return self.backing_list[0]

    def _bubble_up(self, i):
        while i >= 1:
            if i == len(self.backing_list):
                return i
            check = (i - 1)/2
            if self._key(self.backing_list[i]) < self._key(self.backing_list[check]):
                self._swap(i, check)
                i = check
            else:
                return i
        return i

    def _bubble_down(self, i):
        while i <= (len(self.backing_list) - 1)/2:
            check_left = i*2 + 1
            check_right = i*2 + 2
            if check_left == len(self.backing_list):
                return i
            if check_right >= len(self.backing_list):
                check = check_left
            else:
                check = check_left if self._key(self.backing_list[check_left]) < \
                                      self._key(self.backing_list[check_right]) else check_right
            if self._key(self.backing_list[check]) < self._key(self.backing_list[i]):
                self._swap(check, i)
                i = check
            else:
                return i
        return i

    def _swap(self, i, j):
        t_o = self.backing_list[i]
        self.backing_list[i] = self.backing_list[j]
        self.index[self._key(self.backing_list[j])] = i
        self.backing_list[j] = t_o
        self.index[self._key(t_o)] = j

    def _key(self, o):
        return o if not self.key_func else self.key_func(o)


class _ValueCount:
    def __init__(self, value):
        self.value = value
        self.count = 1

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def is_empty(self):
        return self.count == 0


def _key_func(o):
    return o.value


counts = {}
a = []

for _i in xrange (100000):
    r = randint(0, 10000)
    if r not in counts:
        counts[r] = 0
    counts[r] += 1
    a.append(r)

ih = IndexedHeap(key_func=_key_func)
for e in a:
    o = ih.get(e)
    if not o:
        o = _ValueCount(e)
        ih.add(o)
    else:
        o.increment()

if len(counts) != len(ih.backing_list):
    print len(counts), len(ih.backing_list)
for e in ih.backing_list:
    if counts[_key_func(e)] != e.count:
        print _key_func(e), counts[_key_func(e)], e.count

for _i in xrange(100000):
    r = randint(0, 10000)
    if r in counts:
        counts[r] -= 1
        if counts[r] == 0:
            counts.pop(r)
    o = ih.get(r)
    if o:
        o.decrement()
        if o.is_empty():
            ih.delete(o)
    if len(counts) != len(ih.backing_list):
        print len(counts), len(ih.backing_list)
    o = ih.get(r)
    if r in counts and o and counts[r] != o.count:
        print r, counts[r], o.count
