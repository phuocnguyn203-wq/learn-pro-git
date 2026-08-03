def greet(name):
    return f'hello {name}'

def main():
    greet('John')
    print('Fun fact: You can\'t cache if your response is 3xx')
    print(f'This is server. You can play supergame')

if __name__ == '__main__':
    main()