'''
Source: https://codeforces.com/group/yQ3W2TUEr9/contest/346021/problem/A
'''

def diary_riddle(names):
    my_set = set()
    for name in names:
        if name not in my_set:
            my_set.add(name)
            print('NO')

        else:
            print('YES')

def main():
    n = int(input())
    names = list()
    for _ in range(n):
        names.append(input())

    print(diary_riddle(names))


if __name__ == '__main__':
    main()