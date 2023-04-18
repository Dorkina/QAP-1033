# Вариант решения 1
# price = []
# bilet_n = int(input("Введите количество билетов: "))
# for b in range(bilet_n):
#     person_age = int(input("Введите возраст участника "))
#     if person_age < 18:
#         price.append(0)
#     elif person_age < 25:
#         price.append(990)
#     else:
#         price.append(1390)
# if bilet_n > 3:
#     print(sum(price)*0.9)
# else:
#     print(sum(price))

# Вариант решения 2
price_sum = 0
bilet_n = int(input("Введите количество билетов: "))
for b in range(bilet_n):
    person_age = int(input("Введите возраст участника "))
    if person_age < 18:
        continue
    elif person_age < 25:
        price_sum += 990
    else:
        price_sum += 1390
if bilet_n > 3:
    print(price_sum*0.9)
else:
    print(price_sum)