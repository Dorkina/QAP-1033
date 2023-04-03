money = int(input("Введите сумму: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

# Первый вариант решения задачи.
deposit = []
for i in per_cent.values():
    deposit.append(round(i*money/100))
print(max(deposit))

# Второй вариант решения.
per_cent_key = []
per_cent_value = []
maximum = 0
index = None
for k, v in per_cent.items():
    per_cent_key.append(k)
    per_cent_value.append(round(v*money/100))
for i in range(len(per_cent_value)):
    if per_cent_value[i] > maximum:
        maximum = per_cent_value[i]
        index = i

print(f"Самое выгодное предложение: \nБанк: {per_cent_key[index]}, сумма процентов годовых: {maximum}")
