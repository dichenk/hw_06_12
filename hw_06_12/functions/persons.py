class Person:
    def __init__(self, fio, age, passport, weight):

        if self.__verify_fio(fio):
            self.__fio = fio

        if self.__verify_age(age):
            self.__age = age
        
        if self.__verify_passport(passport):
            self.__passport = passport

        if self.__verify_weight(weight):
            self.__weight = weight
   
    def __verify_fio(self, item):
        a = item.split(' ') ## облегчаем код - понадобится дальше

        if type(item) is not str:
            raise TypeError('ФИО должно быть строкой')
        
        if len(item.split(' ')) !=3:
            raise TypeError('Неверный формат записи ФИО')
        
        if not "".join(a).isalpha():
            raise TypeError('В ФИО можно использовать только буквенные символы')
        return True
   
    def __verify_age(self, item):
        
        if type(item) is not int or item < 14 or item > 150:
            raise TypeError('Возраст должен быть целым числом от 14 до 150')
        return True

    def __verify_passport(self, item):
        a = item.split(' ') ## облегчаем код

        if type(item) is not str:
            raise TypeError('Паспорт должен быть строкой')
        
        if len(item) != 11 or len(a) != 2: 
            raise TypeError('Неверный формат паспорта')

        if not "".join(a).isdigit():
            raise TypeError('Серия и номер паспорта должны содержать только числа')
        return True

    def __verify_weight(self, item):

        if type(item) is not float or item < 25:
            raise TypeError('Вес должен быть вещественным числом от 25 и выше')
        return True

    @property
    def fio(self):
        return self.__fio

    @property
    def age(self):
        return self.__age

    @property
    def passport(self):
        return self.__passport

    @property
    def weight(self):
        return self.__weight

    @fio.setter
    def fio(self, fio):
        self.__verify_fio(fio)
        self.__fio = fio

    @age.setter
    def age(self, age):
        self.__verify_age(age)
        self.__age = age

    @passport.setter
    def passport(self, passport):
        self.__verify_passport(passport)
        self.__passport = passport

    @weight.setter
    def weight(self, weight):
        self.__verify_weight(weight)
        self.__weight = weight

