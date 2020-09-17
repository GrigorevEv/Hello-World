# Задача A-Шестнадцатеричные и двоичные
# Вычислите XOR от двух чисел.
# Логическая операция "исключающее или".
# FALSE XOR FALSE = FALSE
# FALSE XOR TRUE =TRUE
# TRUE XOR FALSE =TRUE
# TRUE XOR TRUE =FALSE
# Операция дает FALSE если операнды равны не зависимо от них. Еще одно название "Сложение по модулю 2"

x, y = input().split()
x = int(x, 16)
y = int(y, 16)

print(hex(x ^ y)[2:])
