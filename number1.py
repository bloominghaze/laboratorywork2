import math
def calculate_tan_alpha():
    alpha = float(input("Введіть значення α (у радіанах): "))
    z = math.tan(3 * alpha)
    print(f"Значення z = tan(3α): {z}")
    return z

def calculate_power():
    x = float(input("Введіть значення x: "))

    while True:
        try:
            n = int(input("Введіть значення n (ціле число): "))
            break
        except ValueError:
            print("Помилка! Потрібно ввести ціле число для степеня.")

    result = 1
    for i in range(abs(n)):
        result *= x
    if n < 0:
        result = 1 / result

    print(f"Значення Z = x^n: {result}")
    return result

def main():
    z = calculate_tan_alpha()
    z_power = calculate_power()

if __name__ == "__main__":
    main()
