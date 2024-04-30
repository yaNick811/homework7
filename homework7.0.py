x =46
if x < 25:
    print('yes')
print('Goodbye!')
if x > 2:
    print('yes')
print('Goodbye!')

# примеры

a = 34
b = 756
if a > b:
    print('a > b')
if a < b and a > 3:
    print('YES')
if a > b or b > 45:
    print('YES')
if a == 4 and (a > 2 or b < 1000):
    print('YES')

# можно сравнивать числа, строки, списки,

if '76' > '436':
    print('Yes')
if '42' > '436':
    print('YES')
if [1, 1] > [3, 3]:
    print('YES')

# нельзя сравнивать РАЗНЫЕ ТИПЫ

if '34' < 37:
    print('YES')
if [1, 1] > 8:
    print('YES')

# но

if '6' != 6:
    print('YES')
