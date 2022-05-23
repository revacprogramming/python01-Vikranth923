
def input_two_numbers():
    x = int(input("enter 1st number"))
    y = int(input("enter 2nd number"))
    return x,y
    
def add(a, b):
    return (a+b)

def output(a, b, sm):
    print(sm)

def main():
    a,b = input_two_numbers()
    sm = add(a, b)
    output(a, b, sm)

if __name__ == '__main__':
    main()
