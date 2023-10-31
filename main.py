# coding: utf-8

def create_list():
    with open('files/list.txt', 'r', encoding="utf-8") as f:
        list = f.readlines()
    return list

def main():
    list = create_list()
    for i in list:
        print(i)
        return


if __name__ == '__main__': main()

