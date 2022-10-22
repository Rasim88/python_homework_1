# 1 - Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal

num = input('Enter number: ')
d = input('Enter number accuracy: ')
num = Decimal(num)
num = num.quantize(Decimal(d))
print(f'Number will be equal to: {num}')