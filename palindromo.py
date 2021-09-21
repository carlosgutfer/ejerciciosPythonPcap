text = input('Writea text: ')
text = text.replace(' ', '')
for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i] and ord(text[i])  != ord(text[len(text) - 1 - i]) + 32 and ord(text[i])  != ord(text[len(text) - 1 - i]) - 32:
        print("It's not a palindrome")
        break
    if i == len(text) // 2 - 1:
        print("It's a palindrome")
    