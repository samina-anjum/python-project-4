def main():
    number = float(input("\033[1;3mType a number to see its square:\033[0m "))
    square = number * number
    print(f"\033[1;3mThe square of {number} is {square}\033[0m")

if __name__ == '__main__':
    main()

