from collections import defaultdict

if __name__=="__main__":
    name_collections = defaultdict(int)

    name_amounts = list(map(int, input().split(' ')))

    for _ in range(name_amounts[0]):
        name_collections[input()] = 1

    for _ in range(name_amounts[1]):
        name = input()
        if name_collections[name] == 1:
            name_collections[name] += 1

    names = dict(filter(lambda x: x[1]==2, name_collections.items())).keys()
    names = sorted(names)
    print(len(names))

    for name in names:
        print(name)
