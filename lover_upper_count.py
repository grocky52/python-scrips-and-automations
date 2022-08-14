
import os
def lower_upper_count():
    print(os.getcwd())

    with open('/home/medusa/Documents/python/scripting/text.txt', 'r') as f:
        l_count = 0
        u_count = 0

        values = f.read()
        for i in values:
            if i.islower():
                l_count += 1
            elif i.isupper():
                u_count += 1

        print(f'lower case {l_count}')
        print(f'upper case {u_count}')

lower_upper_count()
