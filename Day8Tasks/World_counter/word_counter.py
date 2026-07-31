file=open("article.txt","r")
text=file.read()
file.close()

words=len(text.split())
lines=len(text.splitlines())
characters=len(text)

print("Words =",words)
print("Lines =",lines)
print("Characters =",characters)