# some_module.py

__all__ = ['GLOBAL_VAR', 'function1', 'function2']

GLOBAL_VAR = 42


def function1():
    pass


def function2():
    pass


def _internal_function():
    pass


'''В этом примере, при импорте с использованием from some_module import *, будут доступны только GLOBAL_VAR, function1 и 
function2. При этом переменная _internal_function останется скрытой и не будет импортирована.
Таким образом, вы контролируете, какие переменные будут доступны для импорта с использованием звездочки, и предоставляете 
более четкий интерфейс для пользователей вашего модуля.'''
