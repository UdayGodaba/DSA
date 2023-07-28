def isPalindrome(s, i = 0):
    if i >= len(s)//2:
        return True
    if s[i] == s[len(s) - i - 1] and isPalindrome(s, i + 1):
        return True
    else:
        return False

string = 'aba'
string = 'abc'
string = '11211'
# string = '11221'
print(isPalindrome(string))