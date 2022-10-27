
from employeedb import Employee
import sqlite3
conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE employee (first text, last text, pay integer)""")

def insert_emp(emp):
    with conn:
        c.execute('INSERT INTO employee VALUES (:first, :last, :pay)', {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emp_by_names(lastname):
    with conn:
        c.execute('SELECT * FROM employee WHERE last = :last', {'last': lastname})
        return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("UPDATE employee SET pay = :pay WHERE first = :first AND last = :last",
         {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def remove_emp(emp):
    with conn:
        c.execute('DELETE FROM employee WHERE first = :first AND last = :last',
        {'first': emp.first, 'last': emp.last})

emp_1 = Employee('john', 'doe', 3500)
emp_2 = Employee('jane', 'doe', 5000)
emp_3 = Employee('james', 'ngubia', 5000)

insert_emp(emp_1)
insert_emp(emp_2)
insert_emp(emp_3)


update_pay(emp_3, 10000)
remove_emp(emp_1)
emps = get_emp_by_names('ngubia')



print(emps)


# c.execute("INSERT INTO employee VALUES (?,?,?)",(emp_1.first, emp_1.last, emp_1.pay))
# conn.commit()
#
# c.execute("INSERT INTO employee VALUES (?,?,?)",(emp_3.first, emp_3.last, emp_3.pay))
# conn.commit()
#
# c.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last': emp_2.last, 'pay':emp_2.pay})
# conn.commit()
#
# c.execute("SELECT * FROM employee WHERE last=?", ('doe',))
# valuedb1 = c.fetchall()
# print(valuedb1)
#
# c.execute("SELECT * FROM employee WHERE last=:last", {'last': 'ngubia'})
# valuesdb = c.fetchall() #needed to show what fetched
# print(valuesdb)
#
#
#
# conn.commit()
conn.close()
