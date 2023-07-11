sum = 0

while True:
    try:
        n = input("Digite um número:")
        if len(n) == 0:
            break
        n = float(n)
    except (ValueError, TypeError) as e:
        print("Digite apenas números")
    else:
        sum += n
        print("Soma parcial:", sum)