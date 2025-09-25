import string
text = input()
for ch in string.punctuation:
    text.replace('ch','')
words = text.split()
result = '#'
for w in words:
    result += w.capitalize()
if len(result) > 140:
    result = result[:140]
print(result)