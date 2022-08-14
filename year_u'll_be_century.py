
from datetime import date

name = input('please enter youur name        :')
age = int(input('enter your age       :'))
print_number = int(input('enter a number depending on the print out you want'))
years = 100 - age
today = date.today()
current_year = today.year
century = current_year + years
for i in range(print_number):
    print(f'{name} you will be a century in {century}\n')
