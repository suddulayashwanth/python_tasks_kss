def vowels(s):
    count=0
    for i in s:
        if i.lower() in "aeiou":
            count=count+1
    return count

text=input()
print(vowels(text))