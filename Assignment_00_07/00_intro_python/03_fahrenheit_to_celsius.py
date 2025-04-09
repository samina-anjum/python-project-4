def main():
    fahrenheit=float(input('\033[1:3mEnter the temperature in Fahrenheit:\033[0m'))
    celsius=(fahrenheit-32.00)*(5.00/9.00)
    print(f"The temperature in Celsius is {celsius:.2f}.")



if __name__ == '__main__':
    main()





