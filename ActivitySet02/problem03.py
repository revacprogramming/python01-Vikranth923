

def get_cs():
    s = str(input("enter string"))
    return s


def cs_to_lot(cs):
    a=[]
    c = cs.split()
    for i in c:
        a.append(i)
    return a


def main():
    cs = get_cs()
    lot = cs_to_lot(cs)
    print(lot)
12

if __name__ == '__main__':
    main()
