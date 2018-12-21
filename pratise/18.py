# 1、创建员工类Employee，属性有姓名name、能力值ability、年龄age（能力值为100-年龄），功能有doWork（），该方法执行一次，该员工的能力值-5，创建str方法，打印该员工的信息
# 2、创建老板类Boss，属性有金钱money,员工列表employeeList（存储员工类对象），工作量work,功能有雇佣员工addEmployee()，雇佣后将员工添加至列表中，雇佣一人money减5000，金额不足时不能雇佣新员工；开始工作startWork(),工作开始后，依次取出员工列表中的员工开始工作，员工能力值减少的同时总的工作量work也减少，当工作量work为0时，工作结束，调用endWork（该方法为Boss类方法，打印员工的能力值信息）方法，如果所有员工使用完后，依然没有完成工作，则提示老板需要雇佣新员工，并打印剩余工作量
# 3、创建Boss类对象，默认执行雇佣3个员工，年龄分别为30,40,50，然后死循环开始工作，直至工作完成。


class Employee:

    def __init__(self, name, age):
        self.name = name
        self.ability = 100 - int(age)
        self.age = age

    def doWork(self):
        self.ability -= 5

    def __str__(self):
        print("员工：%s，年龄：%s，能力值：%s" % (self.name, self.age, self.ability))


class Boss:

    work = 10000

    def __init__(self, money, work):
        self.money = money
        self.employeeList = []
        self.set_work(work)

    @classmethod
    def set_work(cls, work):
        cls.work = work

    @classmethod
    def reduce_work(cls):
        cls.work -= 1

    def addEmployee(self, empolyee):
        if self.money < 5000:
            print("余额不足，无法雇佣新员工")
            return
        self.employeeList.append(empolyee)
        self.money -= 5000

    def startWork(self):
        for item in self.employeeList:
            for a in range(item.ability):
                self.employee_work()

    def employee_work(self, employee):
        employee.doWork()
        self.reduce_work()


    @classmethod
    def endWork(cls):
        for item in cls.employeeList:
            print(item.ability)

