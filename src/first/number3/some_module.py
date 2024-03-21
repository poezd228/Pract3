# some_module.py

class GlobalVariable:
    def __init__(self, initial_value):
        self.value = initial_value

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

GLOBAL_VAR = GlobalVariable(42)
#Затем другие пользователи могут создать экземпляр класса и использовать методы для доступа и изменения значения переменной.
