def is_year_leap(year):
    """Проверяет, является ли год високосным."""
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False


# Выбор любого года для проверки
input_year = 1985

result = is_year_leap(input_year)

print(f'Год {input_year}: {result}')
