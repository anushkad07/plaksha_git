#PALINDROM CODE

pal = input('Enter a phrase of string')

def isPalindrome(pal):
    return pal == pal[::-1]


ans = isPalindrome(pal)
 
if ans:
    print("Yes")
else:
    print("No")