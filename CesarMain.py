
while True:
    text = input('Enter a text: ')
    if text.isalnum:
        break
while True:
    try:
        num = int(input('Enter a number between 1 - 25: '))
        if num < 1 or num > 25:
            continue
        break
    except:
        continue
new_text = ''   
for letter in text:
    if letter.isalpha():
        for i in range(num):
            if letter == 'z':
                letter = 'a'
                continue
            elif letter == 'Z':
                letter  = 'A'
                continue
            letter = chr(ord(letter) + 1)
    new_text += letter
print(new_text)