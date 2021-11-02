def nested_sum(tt):
    count = 0
    for ii in tt:
        count += sum(ii)
    return count

#tt = [[1,2],[3],[4,5]]
#print(nested_sum(tt))

def cumsum(tt):
    ss = tt[:]
    ll = len(tt)
    for ii in range(ll):
        ss[ii] = sum(tt[:ii+1])
    return ss

#tt = [1,2,3]
#print(cumsum(tt))

def middle(tt):
    ss = tt[1:-1]
    return ss

#tt = [1,2,3,4]
#print(middle(tt))

def chop(ss):
    del ss[0]
    del ss[-1]

#tt = [1,2,3,4]
#chop(tt)

def is_sorted(ss):
    for ii in range(len(ss)-1):
        if ss[ii] > ss[ii+1]:
            return False
    return True

#aa = [1,2,2]
#print(is_sorted(aa))
#bb = ['b','a']
#print(is_sorted(bb))

def is_anagram(ss,tt):
    if len(ss) != len(tt):
        return False
    aa = sorted(ss)
    bb = sorted(tt)
    if aa != bb:
        return False
    return True

#string1='stop'
#string2='pots'
#print(is_anagram(string1,string2))

def has_duplicates(ss):
    aa = sorted(ss)
    for ii in range(len(aa)-1):
        if aa[ii] == aa[ii+1]:
            return True
    return False

#ss = ['s','d','s']
#print(has_duplicates(ss),ss)
#ss = ['s','d','r']
#print(has_duplicates(ss),ss)
#ss = [1,1,2,3]
#print(has_duplicates(ss),ss)
#ss = [1,2,3,4,4]
#print(has_duplicates(ss),ss)

finname = 'words.txt'
fin = open(finname)

# tt = []
# check = 0
# counter = 0
# if check == 0:
#     for line in fin:
#         word = line.strip()
#         tt.append(word[0])
#         counter += 1
# else:
#     for line in fin:
#         word = line.strip()
#         tt = tt+[word[0]]
#         counter += 1
#
# print(counter)

def in_bisect(sortedwordlist, target):
    if len(sortedwordlist) == 0:
        return False

    ll = len(sortedwordlist) // 2

    if sortedwordlist[ll] == target:
        return True

    if sortedwordlist[ll] > target:
        return in_bisect(sortedwordlist[:ll], target)
    else:
        return in_bisect(sortedwordlist[ll+1:], target)


import time

# starttime = time.time()
# for word in ['aa', 'alien', 'allen', 'zymurgy']:
#         print(word, 'in list', in_bisect(word_list, word))
# print(time.time()-starttime)
#
# newstarttime = time.time()
# for word in ['aa', 'alien', 'allen', 'zymurgy']:
#         print(word in word_list)
# print(time.time()-newstarttime)


def is_reverse(word1, word2):
     if len(word1) != len(word2):
         return False
     i = 0
     j = len(word2)-1

     while j >= 0:
         if word1[i] != word2[j]:
             return False
         i = i + 1
         j = j - 1
     return True

def reverse_pair(wordlist, word):
    revword = word[::-1]
    return in_bisect(wordlist, revword)


#for word in word_list:
#    if reverse_pair(word_list, word):
#        print(word+' is the reverse of '+word[::-1])

def interlock2(wordlist, word):
    evens = word[::2]
    odds  = word[1::2]
    return in_bisect(wordlist, evens) and in_bisect(wordlist, odds)

def interlockn(wordlist, word, n):
    for ii in range(n):
            inter = word[ii::n]
            if not in_bisect(wordlist, inter):
                return False
    return True

fin = open('words.txt')
wordlist = []
for line in fin:
    wordlist.append(line.strip())
nn = 3
for word in wordlist:
    thisstr = word+' '
    if interlockn(wordlist,word,nn):
        for ii in range(nn):
            thisstr += word[ii::nn]+' '
        print(thisstr)
