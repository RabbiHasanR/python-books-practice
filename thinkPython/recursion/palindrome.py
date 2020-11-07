def first(word):
    """Returns the first of a string"""
    return word[0]

def last(word):
    """Return the last of a string"""
    return word[-1]

def middle(word):
    """Return all without first and last character"""
    return word[1:-1]

def is_palindrome(word):
    """Returns true if word is palaindrome"""
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('allen'))
print(is_palindrome('bob'))
print(is_palindrome('otto'))
print(is_palindrome('redivider'))
