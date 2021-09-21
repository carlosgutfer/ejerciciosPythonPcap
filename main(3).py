def read_int(prompt, min, max):
    try:
        prompt = int(prompt)
        if prompt  in range(min, max):
            return prompt
    except:
        raise  ArithmeticError
        
try:
    v = read_int(input('Enter a number from -10 to 10: '), -10, 10)
    assert v
    print("The number is:", v)
except AssertionError:
    print('Error: the value is not within permitted range (min..max)')
except ArithmeticError:
    print('Error: wrong input')

