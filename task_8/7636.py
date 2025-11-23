# (№ 7636) (Демо-2025) Определите количество 12-ричных пятизначных чисел, в записи которых ровно одна цифра 7
# и не более трёх цифр с числовым значением, превышающим 8.

from itertools import *

k = 0

for x in product('0123456789AB', repeat = 5):
    str_x = ''.join(x)
    if str_x.count('7') == 1 and (str_x.count('9') + str_x.count('A') + str_x.count('B')) <= 3 and str_x[0] != '0':
        k += 1
print(k)