#Single Inheritance
class Parent:
    def fun1(self):
        print("This is coming from parent class....")

    def newfunc(self):
        print("This is parent class new function.......")

class Child(Parent):
    def fun2(self):
        print("This is from child class")

child_obj = Parent()
child_obj.fun1()
child_obj.newfunc()

child_obj = Child()
child_obj.fun2()
child_obj.fun1()
child_obj.newfunc()
