def palindrome(str):

    rev = ""
    for i in str:
        rev = i + rev
    if rev == str:
        return True
    else:
        return False

print(palindrome("racecar"))