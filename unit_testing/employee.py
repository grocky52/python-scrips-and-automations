class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last



    @property #build in decorator, here it acts to return the returned value to the main class other than the object as earlier 
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

