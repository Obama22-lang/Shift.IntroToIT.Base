#INTRO TO IT 2nd COURSE
# Задача 3: Четное или нечетное?
# Попробуй определить, является ли введенное число четным или нечетным.
def odd_ever_number (number):
    return "Четное" if number % 2 == 0 else "Нечетное"
number = 5
print(f"{number} - {odd_ever_number (number)}")
