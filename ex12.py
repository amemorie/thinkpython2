def sumall(*args):
    t = 0
    print(type(args))
    for f in range(len(args)):
        t = t+args[f]
    return t

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c,0) + 1
    return d

def most_frequent(ss):
    hh = histogram(ss)

    t = []
    for x, freq in hh.items():
        t.append((freq,x))
    t.sort(reverse=True)
    res = []
    for freq,x in t:
        res.append(x)
    return(res)


# tt = ['StendhalFr.txt','StendhalEn.txt']
# ll = ['French','English']
# for x in range(len(tt)):
#     t = tt[x]
#     line = open(t).read()
#
#     ff = [" ","\n","'","-",".",",","?","!","ï","»","¿",":","/","*","0","1","2","3","4","5","6","7","8","9","©","(",")","\"","\xa0"]
#     for f in ff:
#         line = line.replace(f,"")
#     ss = line.lower()
#
#     gg = most_frequent(ss)
#     print('The most frequent letters in '+ll[x]+' are:')
#     for x in gg:
#         print(x)
def make_worddictionary(finname):
    fin = open(finname)
    dd = dict()
    for line in fin:
        word = line.strip().lower()
        dd[word] = dd.get(word,0) + 1
    for letter in ['a','i','']:
        dd[letter] = 1
    return dd

dd = make_worddictionary('words.txt')

# def print_anagrams(dd):
#     for word in dd:
#         if len(dd[word]) > 1:
#             print(dd[word])
#
#
# print_anagrams(dd)

def print_anagrams_by_length(dd):
    t = []
    for v in dd.values():
        if len(v) > 1:
            t.append((len(v),v))
    t.sort()
    for x in t:
        print(x)

#print_anagrams_by_length(dd)

def filter_length(dd, nn):
    res = {}
    for word, anagrams in dd.items():
        if len(word) == nn:
            res[word] = anagrams
    return res

#ss = filter_length(dd, 8)
#print_anagrams_by_length(ss)

def metathesis(dd):
    # metathesis pairs must be anagrams of each other
    for anagrams in dd.values():
        for word1 in anagrams:
            for word2 in anagrams:
                if word1 < word2 and word_distance(word1,word2) == 2:
                    print(word1, word2)

def word_distance(word1,word2):
    if len(word1) == len(word2):
        count = 0
        for c1, c2 in zip(word1,word2):
            if c1 != c2:
                count += 1
    return count

#pairs = metathesis(dd)

def children(word,dd):
    res = []
    ll = len(word)
    for ii in range(ll):
        child = word[:ii]+word[ii+1:]
        if child in dd :
            res.append(child)
    return res

memo = {}
memo[''] = ['']

def is_reducible(word,dd):
    if word in memo:
        return memo[word]
    res = []
    for child in children(word,dd):
        if is_reducible(child,dd):
            res.append(child)
    memo[word] = res
    return res

def all_reducible(dd):
    res = []
    for word in dd:
        tt = is_reducible(word,dd)
        if tt != []:
            res.append(word)
    return res

def print_trail(word,dd):
    if len(word) == 0:
        return
    print(word, end=' ')
    t = is_reducible(word, dd)
    print_trail(t[0],dd)

def print_longest_words(dd):
    words = all_reducible(dd)

    # use DSU to sort by word length
    t = []
    for word in words:
        t.append((len(word), word))
    t.sort(reverse=True)

    # print the longest 5 words
    for _, word in t[0:5]:
        print_trail(word,dd)
        print('\n')

dd = make_worddictionary('words.txt')
print_longest_words(dd)
