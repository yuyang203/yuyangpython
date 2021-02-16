"""
创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
"""


class Animal:
    def __init__(self, name, color, age, sex):
        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    def scream(self):
        print(f'{self.name}会叫')

    def run(self):
        print(f'{self.name}会跑')


if __name__ == '__main__':
    animals = Animal('animals', 'yellow', 3, 'male')
    print(animals.name)
    print(animals.age)
    print(animals.sex)
    print(animals.color)
    animals.scream()
    animals.run()


