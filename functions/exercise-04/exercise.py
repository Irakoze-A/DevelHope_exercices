names = ['John', 'Tristram ','Baldwin ', 'Wally ']
surnames = [ 'Doe', 'Mcbride','Preston', 'Collins']

def hello(name ='Joe', surname='Doe'):
    print(f'Hello {name} {surname} !')
    
for i in range(len(family)):
    hello(names[i], surnames[i])