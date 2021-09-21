text = input('Writea text: ')
for i in range(len(text) // 2):
    if text[i] != text[len(text) - 1 - i]:
        print("It's not a palindrome")
        break