def reverse(s):
    if len(s)==0:
        return s
    return reverse(s[1:])+s[0]

text=input("Enter string: ")
print(reverse(text))