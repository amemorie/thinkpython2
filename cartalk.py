def is_triple_double(word):
    ii = 0
    count = 0
    while ii < len(word)-1:
        if word[ii] == word[ii+1]:
            count += 1
            if count == 3:
                return True
            ii += 2
        else:
            ii = ii + 1 - 2*count
            count = 0

    return False

def cartalk():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if is_triple_double(word):
            print(word+' has three consecutive double letters')

#cartalk()

def is_palindrome(word):
    ii = 0
    jj = len(word)-1

    while ii < jj:
        if word[ii] != word[jj]:
            return False
        ii += 1
        jj = jj - 1

    return True

def cartalk2():
    counter = 0
    starting_number = -1
    wordstr = ''
    for ii in range(1000000):
        word = str(ii)
        ll = len(word)
        if ll != 6:
            for jj in range(6-ll):
                word = '0'+word
        if counter == 3:
            if is_palindrome(word):
                wordstr = wordstr+' '+word
                print(wordstr)
            wordstr=''
            starting_number = -1
            counter = 0
        if counter == 2:
            if is_palindrome(word[-5:-2]):
                counter = 3
                wordstr = wordstr+' '+word
            else:
                counter = 0
                wordstr = ''
        if counter == 1:
            if is_palindrome(word[-5:]):
                wordstr = wordstr+' '+word
                counter = 2
            else:
                counter = 0
                wordstr = ''
        if counter == 0:
            if is_palindrome(word[-4:]):
                wordstr = wordstr+' '+word
                counter = 1
                starting_number = ii
            else:
                starting_number = -1
                wordstr = ''

#cartalk2()

def myage():

    myage_now = ''
    for jj in range(40):
        diff = jj + 15
        counter = 0
        testage = ''
        for ii in range(100):
            if ii+diff <= 100:
                myage = str(ii)
                if ii < 10:
                    myage = '0'+myage
                reverse_myage = myage[1]+myage[0]
                mumage = str(ii+diff)
                mumage1 = str(ii+diff+1)
                if mumage == reverse_myage or mumage1 == reverse_myage:
                    counter += 1
                    if counter == 6:
                        testage = myage
                    if counter >= 8:
                        myage_now = testage
    print('My age now is '+myage_now)
myage()
