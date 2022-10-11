'''
https://codeforces.com/problemset/problem/978/A
'''

def removeDuplicates(nums):
    # return list(dict.fromkeys(nums)) to keep order (I don't think it's necessary)
    return set(nums)

def main():
    n = int(input())
    nums = map(int, input().split())
    print(*removeDuplicates(nums)) # * unpacks the set


if __name__ == '__main__':
    main()