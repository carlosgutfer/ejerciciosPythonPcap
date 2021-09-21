import sys

text1 = input('Write your first text: ').upper()
text2 = input('Write your second text: ').upper()

for letter in text1:
    if letter in text2:
        continue
    else:
        print("It's not an anagram")
        sys.exit()
        break
    
print("It is an anagram")