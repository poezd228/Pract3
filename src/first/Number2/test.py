import module_example
result = module_example.test_function()
print(result)

# Попытка повторного импорта
import module_example
result = module_example.test_function()
print(result)
#модуль загружается и инициализируется только один раз