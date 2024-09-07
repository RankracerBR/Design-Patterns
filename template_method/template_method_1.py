from abc import ABC, abstractmethod


class Abstract(ABC):
    def template_method(self):
        self.hook()
        self.base_class_method()
        self.operation1()
        self.operation2()
    
    def hook(self): pass

    def base_class_method(self):
        print('OLÁ EU SOU DA CLASS ABSTRATA E SEREI EXECUTADO TAMBÉM')

    @abstractmethod
    def operation1(self): pass

    @abstractmethod
    def operation2(self): pass


class ConcreteClass1(Abstract):
    def hook(self):
        print('Olha eu vou utilizar o hook')

    def operation1(self):
        print('Operação 1 concluída')

    def operation2(self):
        print('Operação 2 concluída')


class ConcreteClass2(Abstract):
    def operation1(self):
        print('Operação 1 concluída (de maneira diferente)')

    def operation2(self):
        print('Operação 2 concluída (de maneira diferente)')


if __name__ == "__main__":
    c1 = ConcreteClass1()
    c1.template_method()

    print()
    c2 = ConcreteClass2()
    c2.template_method()