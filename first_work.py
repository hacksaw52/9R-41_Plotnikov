temperature = float(input("Сколько градусов на улице?: "))

if temperature > 20 and temperature < 30:
    is_rainy = input("Дождь идет? (да/нет): ") == "да"
    if is_rainy:
        print("Надеть: Футболку, шорты, дождевик")
    else:
        print("Надеть: Футболку и шорты")

elif temperature <= 0:
    print("Надеть: Пуховик")

else:
    is_rainy = input("Дождь идет? (да/нет): ") == "да"
    if is_rainy:
        is_raining_heavily = input("Сильный ли дождь? (да/нет): ") == "да"
        if is_raining_heavily:
            print("Надеть: Пальто, резиновые сапоги и зонт")
        else:
            print("Надеть: Пальто и дождевик")
    else:
        print("Надеть: Пальто")
