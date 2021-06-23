class Person:

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        print("我叫%s，体重%.2f千克" % (self.name, self.weight))

    def __str__(self):
        return "我现在%.2f千克" % self.weight

    def run(self):
        print("跑步减肥，体重减少0.5kg")
        self.weight -= 0.5

    def eat(self):
        print("吃饭增重，体重增加1kg")


xiaoming = Person("小明", 70.0)

xiaoming.run()
xiaoming.eat()

print(xiaoming)
