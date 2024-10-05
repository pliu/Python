class MethodAdding(type):
    def __init__(cls, name, bases, class_dict):
        setattr(cls, "test", classmethod(lambda c, x: x**2))
        setattr(cls, "test2", lambda self: self.lol*2)
        super(MethodAdding, cls).__init__(name, bases, class_dict)

    def __new__(mcs, name, bases, class_dict):
        for check in class_dict:
            if type(class_dict[check]).__name__ == 'classmethod':
                class_dict[check] = classmethod(lambda cls: 'Yay!')
            if check == 'instance_method':
                class_dict[check] = lambda self: 'Rip'
        return super(MethodAdding, mcs).__new__(mcs, name, bases, class_dict)


class ConcreteClass(object):
    __metaclass__ = MethodAdding

    def __init__(self):
        self.lol = 5

    def instance_method(self):
        return None

    @classmethod
    def class_method(cls):
        return None


x = ConcreteClass()
print x.test(5)
print ConcreteClass.test(5)
print x.test2()
print ConcreteClass.class_method()
print x.instance_method()
