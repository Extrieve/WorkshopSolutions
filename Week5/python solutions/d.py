'''
Source: https://codeforces.com/group/yQ3W2TUEr9/contest/346021/problem/C
'''

def second_order(numbers):
    return sorted(set(numbers))[1]


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    print(second_order(numbers))


if __name__ == '__main__':
    main()