# I-Размен денег
# Написать функцию make_exchange(money, coins), которая принимает сумму денег (целое число)
# и массив номиналов разменных монет (целых чисел) (возможно пустой) и возвращает количество способов произвести размен.
# Считаем, что разменных монет бесконечное множество.
# Формат выходных данных
# Число способов произвести размен. Способы 1+2 и 2+1 считаем тождественными.


def make_exchange(money: int, coins: list):
    ways = [0] * (money + 1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(len(ways)):
            if coins[i] <= j:
                ways[j] += ways[j-coins[i]]
    return ways[money]


print(make_exchange(10, [2, 3, 5]))
