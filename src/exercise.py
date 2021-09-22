def main():
    #write your code below this line
    num = int(input())
    print_until_number(num)


def print_until_number(number):
    i = 1
    while (i <= number):
        print(i)
        i += 1

if __name__ == '__main__':
    main()
