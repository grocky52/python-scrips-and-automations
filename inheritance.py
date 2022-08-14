 
#!/usr/bin/python3
class base():
    def sum(self, a, b):
        return a + b

class child(base):
    def mul(self, c, d):
        return c * d

child_obj = child()
child_mul = child_obj.mul(3, 6)
chil_add = child_obj.sum(10, 36)
print((child_mul))
print(chil_add)
