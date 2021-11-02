def has_no_e(word):
    little_e = 'e'
    big_e    = 'E'
    for letter in word:
        if letter == little_e or letter == big_e:
            return False
    return True

def avoids(word,a):
    if len(a) == 1:
        little_a = a.lower()
        big_a = a.upper()
        for letter in word:
            if letter == little_a or letter == big_a:
                return False
        return True
    else:
        print("Please pass in a single letter")

def avoidsstring(word, b):
    for letter in b:
        c = avoids(word,letter)
        if c == False:
            return False
    return True

def find(word, letter, start):
     index = start
     while index < len(word):
         if word[index] == letter:
             return index
         index += 1
     return -1

def count(word, ss, start):
    index = start
    cc = 0
    while index < len(word):
        rr = find(word, ss, index)
        if rr == -1:
            break
        cc += 1
        index = rr+1
    return cc

def try_all_the_letter_combinations(finname):

    ss = ord('a')
    number_in_combinations = 5
    this_str = 'abcde'
    ord_str = [0,1,2,3,4]

    ee = False
    lowestp = -1
    lowest_str = ''

    counter = 0
    while ee == False:
        ## make a string with n letters in it

        # don't run this if there are repeat letters in this_str
        chk = 0
        for letter in this_str:
            tt = count(this_str, letter, 0)
            if tt > 1:
                chk = 1
        if chk == 0:
            count1 = 0
            count2 = 0
            fin = open(finname)
            for line in fin:
                word = line.strip()
                aa = avoidsstring(word,this_str)
                if aa :
                    count2 += 1
                count1 += 1
            if count1 > 0 :
                p = (100.* count2 / count1)
            else:
                p = 0
            if lowestp == -1 or p < lowestp :
                lowestp = p
                lowest_str = this_str

            ord_str[4]=ord_str[4]+1
            this_str=''
            for ii in range(number_in_combinations):
                this_str += chr(ord_str[ii]+ss)
            if this_str == 'vwxyz' or counter == 20:
                ee = True
            counter += 1
    print(lowest_str, lowestp)

#try_all_the_letter_combinations('words.txt')

def uses_only_string(word, b):
    counter = 0
    l = len(word)
    for letter in b:
        c = count(word,letter,0)
        if c != 0:
            counter += c
    if counter == l:
        return True
    return False

def uses_only(finname):
    this_str = 'acefhlo'
    fin = open(finname)
    counter = 0
    for line in fin:
        word = line.strip()
        aa = uses_only_string(word,this_str)
        if aa:
            print(word,this_str)
        counter += 1

#uses_only('words.txt')

def uses_all_string(word,b):
    counter = 0
    l = len(b)
    for letter in b:
        c = count(word,letter,0)
        if c != 0:
            counter += 1
    if counter == l:
        return True
    return False

def uses_all(finname):
    this_str = 'aeiouy'
    fin = open(finname)
    counter = 0
    for line in fin:
        word = line.strip()
        aa = uses_all_string(word,this_str)
        if aa:
            print(word,this_str)
            counter += 1
    if counter == 0:
        print('No words found will all of the string '+this_str)
    else:
        print(str(counter)+' words found with all of the string '+this_str)

#uses_all('words.txt')

def is_abecedarian(word):
    counter = 0
    lastletter = -1
    for letter in word:
        aa = ord(letter)
        if aa >= lastletter:
            counter += 1
        else:
            return False
        lastletter = aa
    if counter == len(word):
        return True

def abecedarian(finname):
    fin = open(finname)
    counter = 0
    for line in fin:
        word = line.strip()
        aa = is_abecedarian(word)
        if aa:
            print(word)
            counter += 1
    if counter == 0:
        print('No words found with letters in alphabetical order')
    else:
        print(str(counter)+' words found with letters in alphabetical order')

abecedarian('words.txt')
