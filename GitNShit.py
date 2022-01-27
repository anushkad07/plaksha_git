#PALINDROME CODE

pal = input('Enter a phrase of string')

def isPalindrome(pal):
    if type(pal)!=str:
        raise TypeError("String only")
    else:
        return pal == pal[::-1]

ans = isPalindrome(pal)
 
if ans:
    print("Yes")
else:
    print("No")