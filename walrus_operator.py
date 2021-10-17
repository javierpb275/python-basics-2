text = 'hellooooooo'

if ((m := len(text)) > 10):
    print(f'too long {m} elements')

while((n := len(text)) >= 1):
    print(n, text)  # 5 hello, 4 hell... 1 h
    text = text[:-1]
