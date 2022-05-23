

def get_cs():
    s = str(input("enter a string"))


def cs_to_lot(cs):
    a=[]
    c = cs.split()
    for i in c:
        a.append(i)
    return a


def lot_to_cs(lot):
    for i in lot:
        c = str(c+i)


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()
