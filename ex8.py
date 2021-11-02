#i = input("give me a word and I will print it backwards")
#j = 0
#while j < len(i):
#    print(i[(-1*j)-1])
#    j += 1

#print("or another way")

#for letter in i:
#    print(letter)

#prefixes = 'JKLMNOPQ'
#suffixes = 'ack'

#for letter in prefixes:
#    if letter == 'O' or letter == 'Q':
#        letter = letter+'u'
#    print(letter+suffixes)

# def find(word, letter, start):
#     index = start
#     while index < len(word):
#         if word[index] == letter:
#             return index
#         index += 1
#     return -1
#
# def count(word, s, start):
#     index = start
#     count = 0
#     while index < len(word):
#         r = find(word, s, index)
#         if r == -1:
#             break
#         count += 1
#         index = r+1
#     return count
#
# word = 'tonnnnnaaassddprpdpsdasdr'
# sear = 'd'
# s = count(word,sear,0)
# print('There are '+str(s)+' '+sear+'s in '+word)


# def is_reverse(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     i = 0
#     j = len(word2)-1
#
#     while j >= 0:
#         if word1[i] != word2[j]:
#             return False
#         i = i + 1
#         j = j - 1
#     return True
#
# print(is_reverse('pots', 'stop'))
# print(is_reverse('banana', 'ananat'))

# a = 'banana'
# print(a.count('t'))

# word='tinnit'
# print((word[0:] == word[::-1]))

def rotate_letter(letter,i):
    if letter.isupper():
        start = ord('A')
    elif letter.islower():
        start = ord('a')
    else:
        return letter

    c = ord(letter)-start
    d = (c + i) % 26 + start
    return chr(d)

def rotate_word(word,i):
    newword=''
    for k in word:
        newword += rotate_letter(k,i)
    return newword
    
print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))
print(rotate_word('sleep', 9))
