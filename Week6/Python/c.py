'''
https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
'''

def timeConversion(s):
    # Write your code here
    if s[-2:] == 'PM' and s[:2] != '12':
        s = str(int(s[:2]) + 12) + s[2:]
    if s[-2:] == 'AM' and s[:2] == '12':
        s = '00' + s[2:]
    return s[:-2]

def main():
    s = input()
    result = timeConversion(s)
    print(result)

if __name__ == '__main__':
    main()