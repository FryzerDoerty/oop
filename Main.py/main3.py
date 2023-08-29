#Шаблон Singleton:
#Реализуйте паттерн Singleton на языке Python для класса Logger, который будет использоваться для логирования информации в приложении. Гарантируйте, что только один экземпляр класса Logger будет создан.
class Singleton(object):
  def __new__(cls):
    if not hasattr(cls, 'instance'):
      cls.instance = super(Singleton, cls).__new__(cls)
    return cls.instance
   
class Logger(Singleton):
    pass
   
singleton = Singleton()
logger = Logger()
print(logger is singleton)
 
singleton.singl_variable = "Singleton Variable"
print(logger.singl_variable)