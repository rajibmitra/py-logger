class Employee:
    """A Sample employee class """

    def __init__(self, first, last):
        self.first = first
        self.last = last

        print('Created emp:{} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp1 = Employee('john','smith')