#ООП Концепции:
#Создайте класс Person, который имеет атрибуты name, age и метод introduce(), выводящий информацию о человеке. Создайте несколько объектов этого класса и вызовите метод introduce() для каждого из них.
class Person:  
    """Базовый класс для всех"""  
 
    def __init__(self, name, age):  
        self.name = name  
        self.age = age
         
 
    def introduce(self):  
        print('Имя: {}. Возраст: {}'.format(self.name, self.age))  
 
 
person1 = Person("Анастасия", 23)  
person2 = Person("Мария", 30)  
person1.introduce()  
person2.introduce()  