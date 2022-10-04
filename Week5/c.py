'''
Source: https://codeforces.com/group/yQ3W2TUEr9/contest/346021/problem/B
'''

def indian_summer(names): 
    my_set = set()
    for name in names:
        if name not in my_set:
            my_set.add(name)

    return len(my_set)


# Pythonic Solution 
def indian_summer(names):
    return len(set(names))
    

def main():
    n = int(input())
    names = list()
    for _ in range(n):
        names.append(input())

    print(indian_summer(names))


if __name__ == '__main__':
    main()