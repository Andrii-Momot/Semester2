class ProtectedDictInt:
    def __init__(self):
        self.__d = {}
    def __setitem__(self, key, value):
        if type(key) != int:
            raise TypeError('key must be an integer')
        if key in self.__d:
            raise KeyError('key already exists')
        self.__d[key] = value
    def __getitem__(self, key):
        return self.__d[key]
    def __iter__(self):
        yield from sorted(self.__d.keys())

if __name__ == '__main__':
    pd = ProtectedDictInt()
    pd[1]="one"
    print(pd[1])
    pd[2]="two"
    print(pd[2])
    pd[0]="zero"

    # pd[2]="dva"
    # print(pd[2])

    for key in pd:
        print(pd[key])

    # ordinary_dictionary = {}
    # ordinary_dictionary[1]="one"
    # print(ordinary_dictionary[1])


# d={"Ludmyla":"Bobeshko","Viktoria":"Kohanenko"}
#
# print(d["Ludmyla"])
#
# d["Maria"]="Morozova"
# d[3]=128
# d["Maria"]="Tancura"
#
#
# for key in d:
#     print(d[key])
