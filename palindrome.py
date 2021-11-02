# think python 2

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    l=len(word)
    if l < 2:
        return False
    if first(word) != last(word):
        return False
    if len(middle(word)) > 1:
        return is_palindrome(middle(word))
    return True


print(is_palindrome(word))
