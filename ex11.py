eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp = {'one':'uno','two':'dos','three':'tres'}
print(len(eng2sp))
print('one' in eng2sp)
print('uno' in eng2sp)
print('uno' in eng2sp.values())


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

# h = histogram('brontosaurus')
# print(h)
# print(h.get('a',0))
# print(h.get('c',0))

def print_hist(h):
    for c in sorted(h):
        print(c,h[c])

def reverse_lookup(d,v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('Value does not appear in the dictionary')

# h = histogram('parrot')
# key = reverse_lookup(h, 3)
# print(key)
# print_hist(h)

def invert_dict(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key],[]).append(key)
    return inverse

#hist= histogram('parrot')
#print(hist)
#inverse = invert_dict(hist)
#print(inverse)

# t = [1,2,3]
# d = dict()
# d[t] = 'oops'

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

# print(fibonacci(3))
# print(fibonacci(100))

verbose = True

# def example1():
#     if verbose:
#         print('Running Example 1')
#
# example1()
#
# been_called = False
#
# def example2():
#     global been_called
#     been_called = True
#
# count = 0
#
# def example3():
#     global count
#     count = count + 1
# print(count)
# example3()
# print(count)
#
# print(known)
# def example4():
#     known[2] = 4
# example4()
# print(known)
#
# def example5():
#     global known
#     known = dict()
# example5()
# print(known)

def make_worddictionary(finname):
    fin = open(finname)
    dd = dict()
    for line in fin:
        word = line.strip().lower()
        dd[word] = dd.get(word,0) + 1
    return dd

# A(m,n) = { n+1                if m=0
#            A(m-1,1)           if m>0 and n=0
#            A(m-1, A(m,n-1))   if m>0 and n>0

def read_dictionary(filename='cmudict.txt'):
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

cache = {}
def ack(m,n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m-1, 1)
    if (m, n) in cache:
        return cache[m,n]
    else:
        cache[m,n] = ack(m-1, ack(m,n-1))
    return cache[m,n]

a = ack(3, 4)
print(str(a))

a = ack(3, 6)
print(str(a))


#ss = make_worddictionary('words.txt')
#print(list(ss.items())[:10])

# word = 'schooled'
# if word in ss:
#     print(word)


def has_duplicates(ss):
    d = {}
    for x in ss:
        if x in d:
            return True
        d[x] = True
    return False

#ss = ['p','a','r','o','t']
#print(has_duplicates(ss))

def rotate_pairs():
    cc = {}
    dd = make_worddictionary('words.txt')
    for x in dd:
        aa = x[::-1]
        if aa in dd:
            cc[x] = aa
    return cc

#cc = rotate_pairs()
#print(cc.items())

def cartalk4():
    cc = {}
    dd = make_worddictionary('words.txt')
    ee = read_dictionary()
    print('root word :   ')
    for x in dd:
        if len(x) == 5:
            aa = x[1:]
            bb = x[0]+x[2:]
            if aa in dd and bb in dd:
                if aa in ee and bb in ee:
                    if ee[aa] == ee[bb]:
                        cc[x] = [aa,bb]
    return cc

cc = cartalk4()
for f in cc:
    print(f, cc[f])
