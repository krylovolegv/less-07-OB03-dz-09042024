# 1. Создай базовый класс Animal, который будет содержать общие атрибуты (например, name, age) и методы (make_sound(), eat()) для всех животных.
# 2. Реализуй наследование, создав подклассы Bird, Mammal, и Reptile, которые наследуют от класса Animal. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для make_sound()).
# 3. Продемонстрируй полиморфизм: создайте функцию animal_sound(animals), которая принимает список животных и вызывает метод make_sound() для каждого животного.
# 4. Используй композицию для создания класса Zoo, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создай классы для сотрудников, например, ZooKeeper, Veterinarian, которые могут иметь специфические методы (например, feed_animal() для ZooKeeper и heal_animal() для Veterinarian).
# 6. добавь дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import json

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} поет.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_staff(self, staff_member):
        self.staff.append(staff_member)

    def list_animals(self):
        for animal in self.animals:
            print(f"{animal.name}, Age: {animal.age}")

    def list_staff(self):
        for staff in self.staff:
            print(f"{staff.name}, Position: {staff.position}")

class ZooKeeper:
    def __init__(self, name):
        self.name = name
        self.position = "ZooKeeper"

    def feed_animal(self, animal_name):
        print(f"{self.name} is feeding {animal_name}.")

class Veterinarian:
    def __init__(self, name):
        self.name = name
        self.position = "Veterinarian"

    def heal_animal(self, animal_name):
        print(f"{self.name} is healing {animal_name}.")

def save_zoo_state(zoo, filename="zoo_state.json"):
    animals = [{'name': a.name, 'age': a.age, 'class': a.__class__.__name__} for a in zoo.animals]
    staff = [{'name': s.name, 'position': s.position} for s in zoo.staff]
    with open(filename, 'w') as file:
        json.dump({'animals': animals, 'staff': staff}, file)

def load_zoo_state(filename="zoo_state.json"):
    with open(filename, 'r') as file:
        data = json.load(file)
    zoo = Zoo()
    for animal_info in data['animals']:
        class_ = globals()[animal_info['class']]
        animal = class_(name=animal_info['name'], age=animal_info['age'])
        zoo.add_animal(animal)
    for staff_info in data['staff']:
        if staff_info['position'] == "ZooKeeper":
            staff = ZooKeeper(name=staff_info['name'])
        elif staff_info['position'] == "Veterinarian":
            staff = Veterinarian(name=staff_info['name'])
        zoo.add_staff(staff)
    return zoo

# Создание объекта Zoo
my_zoo = Zoo()

# 1. Добавление животных в зоопарк
my_zoo.add_animal(Bird("Павлин", 2))
my_zoo.add_animal(Mammal("Шерхан", 4))
my_zoo.add_animal(Reptile("Удафф", 3))

# 2. Добавление сотрудников зоопарка
my_zoo.add_staff(ZooKeeper("Николай Иванович"))
my_zoo.add_staff(Veterinarian("Аннушка"))

# 3. Вывод списка животных
print("Список животных в зоопарке:")
my_zoo.list_animals()

# 4. Вывод списка сотрудников
print("\nСписок сотрудников зоопарка:")
my_zoo.list_staff()

# 5. Проигрывание звуков животными
print("\nЖивотные издают звуки:")
animal_sound(my_zoo.animals)

# 6. Сохранение состояния зоопарка в файл
save_zoo_state(my_zoo)

# 7. Загрузка состояния зоопарка из файла
loaded_zoo = load_zoo_state()

# 8. Вывод списка животных из загруженного состояния зоопарка
print("\nСписок животных в зоопарке:")
loaded_zoo.list_animals()