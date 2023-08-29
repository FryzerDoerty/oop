#Шаблон Наблюдатель:
#Реализуйте паттерн Наблюдатель на языке Python для системы уведомлений. Создайте класс NotificationSystem (наблюдаемый объект), который будет иметь методы для добавления наблюдателей и уведомления о событиях. Создайте несколько наблюдателей, реагирующих на уведомления.
from abc import ABC, abstractmethod
class NotificationSystem:
    def __init__(self):
        self.__observers = set()
    def attach(self, observer):
        self.__observers.add(observer)
    def detach(self, observer):
        self.__observers.remove(observer)
    def notify(self):
        for observer in self.__observers:
            observer.make_ev()
class AbstractObserver(ABC):
    @abstractmethod
    def make_ev(self):  
        pass
class Event(AbstractObserver):
    def __init__(self, name):
        self.name = name
    def make_ev(self):
        print('{} наблюдатель среагировал'.format(self.name))
event1 = Event('Событие произошло #1')
event2 = Event('Событие произошло #2')
event3 = Event('Событие произошло #3')
ev_system = NotificationSystem()
ev_system.attach(event1)
ev_system.attach(event2)
ev_system.attach(event3)
ev_system.notify()