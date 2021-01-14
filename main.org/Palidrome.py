import time

num1 = list((input("Enter a number for palindrome checking\n")))
copy = num1.copy()
copy.reverse()
# print(num1, copy)


def pali_check():
    if num1 == copy:
        print("Checking...")
        time.sleep(1)
        return "yes it is palindrome number"
    else:
        print("Checking...")
        time.sleep(1)
        return "no its not palindrome number"


if __name__ == '__main__':
    print(pali_check())
