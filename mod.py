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
