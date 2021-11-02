import re

level4 = '.'

while level4 and level4.startswith('.'):
    print("temp sp ::: " + str(level4) )
    level4=level4.lstrip('.')

print(level4)
print('hello')