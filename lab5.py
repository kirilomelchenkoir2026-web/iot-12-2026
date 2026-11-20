from enum import Enum

# Створюємо перелік видів тварин
class Kind(Enum):
    DOG = "Собака"
    CAT = "Кіт"
    BIRD = "Птах"
    HAMSTER = "Хом'як"


# Клас домашнього улюбленця
class Pet:
    # Конструктор
    def __init__(self, name, breed, age, greeting, mass, kind):
        self.name = name
        self.breed = breed
        self.age = age
        self.greeting = greeting
        self.mass = mass
        self.kind = kind

    # Деструктор
    def __del__(self):
        print("Об'єкт тварини видалено:", self.name)

    # Функції доступу (гетери і сетери)
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    # Метод перевірки, чи тваринка ввічлива
    def isPolite(self):
        if "Hello" in self.greeting:
            return True
        else:
            return False

    # Виведення інформації про тваринку на екран
    def show_info(self):
        print("Ім'я:", self.name)
        print("Вид:", self.kind.value)
        print("Порода:", self.breed)
        print("Вік:", self.age)
        print("Маса:", self.mass)
        print("Привітання:", self.greeting)
        print("Ввічливий:", self.isPolite())
        print("--------------------")


# Клас Дім, де живуть тварини
class Home:
    # Конструктор
    def __init__(self):
        self.pets = []

    # Деструктор
    def __del__(self):
        print("Об'єкт дому видалено")

    # Додати тваринку в дім
    def add_pet(self, pet):
        self.pets.append(pet)

    # Отримати список тварин
    def get_pets(self):
        return self.pets

    # Вивести всіх тварин на екран
    def show_all_pets(self):
        for pet in self.pets:
            pet.show_info()

    # Сортування тварин за віком (звичайне сортування бульбашкою)
    def sort_by_age(self):
        n = len(self.pets)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.pets[j].age > self.pets[j + 1].age:
                    # Міняємо місцями
                    temp = self.pets[j]
                    self.pets[j] = self.pets[j + 1]
                    self.pets[j + 1] = temp


# Функція пошуку друзів (різниця у віці менше 2 років)
def areFriends(pets_list):
    n = len(pets_list)
    for i in range(n):
        for j in range(i + 1, n):
            # Рахуємо різницю віку
            diff = pets_list[i].age - pets_list[j].age
            if diff < 0:
                diff = -diff  # робимо число додатнім (модуль)

            if diff < 2:
                print(pets_list[i].name, "і", pets_list[j].name, "- друзі!")


# Головна функція програми
def main():
    # Створюємо кількох тварин
    pet1 = Pet("Рекс", "Вівчарка", 4, "Гав, Hello!", 30, Kind.DOG)
    pet2 = Pet("Мурчик", "Британець", 2.5, "Мяу", 5, Kind.CAT)
    pet3 = Pet("Кеша", "Папуга", 1, "Hello!", 0.1, Kind.BIRD)
    pet4 = Pet("Бобік", "Такса", 6, "Ррр", 9, Kind.DOG)

    # Створюємо дім і додаємо туди тварин
    my_home = Home()
    my_home.add_pet(pet1)
    my_home.add_pet(pet2)
    my_home.add_pet(pet3)
    my_home.add_pet(pet4)

    print("=== Усі тварини в домі ===")
    my_home.show_all_pets()

    print("=== Шукаємо друзів ===")
    areFriends(my_home.get_pets())

    print("\n=== Сортуємо за віком ===")
    my_home.sort_by_age()
    my_home.show_all_pets()

    print("=== Перевірка гетера і сетера ===")
    print("Старе ім'я:", pet1.get_name())
    pet1.set_name("Барон")
    print("Нове ім'я:", pet1.get_name())

    print("\n=== Кінець програми ===")


# Запуск програми
main()