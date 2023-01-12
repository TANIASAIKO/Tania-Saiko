# 1 Реализовать Рекурсию. Возведение числа x в степень y
def power(base, exp):
  if (exp == 1):
    return base
  return base * power(base, exp - 1)


def power(base, exp):
  if (exp == 1):
    return (base)
  if (exp != 1):
    return (base * power(base, exp - 1))
base = int(input("Введите число: "))
exp = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", power(base, exp))


#ИЛИ
#Определить функцию, которая будет дублировать нули в списке и вернуть в виде итеррируемого объекта-коллекции.
#Input:                         Output:
# func([0,0,0])            --> [0,0,0,0,0,0]
# # func([1,2,100,0,3,4,5,0])--> [1,2,100,0,0,3,4,5,0,0]

def duplicate_zero(items):
    new_items = []
    for item in items:
        new_items.append(item)
        if item == 0:
            new_items.append(item)

    return new_items




# 2 Определить функцию, которая проверяет является ли строка,
# введенная пользователем, целым числом. Решение задачи сдать ссылкой на GitHub.

def is_int(str):
  try:
    int(str)
    print('The variable is a number')
  except ValueError:
    print('The variable is not a number')

#ИЛИ
#Даны две строки. Определить функцию, которая будет находить индекс второго входения второй строки в первую.
# Если подстрока ' ' вывести None. Решение сдать ссылкой на GitHub.
#Input:                                 Output:
# func('marry', 'r')            --> 3
# func('merry christmas', 's')  --> 14
# func('happy new year', ' ')   --> None

def second_index(text, sub_value, repeat=2):
    if sub_value == ' ':
        return None

    count = 0
    while count < repeat:
        result = text.find(sub_value)

    return result



# 3 Создайте класс IceCream (для заказа мороженого с добавкой или без),
# принимающий 1 аргумент при инициализации (отвечающий за добавку к мороженому).
# В этом классе реализуйте метод info_about_icecream(), выводящий на печать «Мороженное и {ДОБАВКА}»
# в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое».

class IceCream:
  def __init__(self, добавка = None):
    self.добавка = добавка

  def info_about_icecream(self):
    if self.добавка:
      print(f'Мороженное и { self.добавка }')
    else:
      print('Обычное мороженое')




# 4 Инкапсуляция. Определить класс Car, который будет содержать конструктор,
# в котором будет инициализироваться private переменная maxprice,
# а также методы изменения и вывода максимальной стоимости машины.
class Car:
  def __init__(self, max_price):
    self.__max_price = max_price
  @property
  def max_price(self):
    return self.__max_price
  @max_price.setter
  def max_price(self, new_max_price):
    self.__max_price = new_max_pri



# 5 Создать класс Animal и определить в нем метод make_a_sound(). Метод должен вывоводить строку "Издает звук"
# Cоздать классы Cat и Dog с методами scratch() и dig() соответственно.
# Метод scratch должен выводить строку "Царапать мебель".
# Метод dig должен выводить строку "Рыть землю".
# в классах Cat и Dog переопределите метод make_a_sound() базового класса Animal.
# (Cat: make_a_sound() -> '<...>', Dog: make_a_sound() -> '<...>')

class Animal:
    def __init__(self, type):
        self.type = type
    def make_a_sound(self):
        print("Издает звук")

class Cat:
    def __init__(self):
        super().__init__('Cat')
    def make_a_sound(self):
        print("Дай поесть)")
    def scratch(self):
        print("Царапать мебель")

class Dog:
    def __init__(self):
        super().__init__('Dog')
    def make_a_sound(self):
        print("Бегите")
    def dig(self):
        print("Рыть землю")


