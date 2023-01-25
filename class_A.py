class A():
    name='Deepak'
    def __init__(self, age):
        self.age=age

    def show(self):
        return (f'{self.name}\n{self.age}')


owner = A(22)

print(owner.show())