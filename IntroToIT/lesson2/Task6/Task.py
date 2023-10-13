#INTRO TO IT 2nd COURSE
# Задача 6: Гласные в высоте!
# Посчитай количество гласных букв в строке.
def vowel_count(line):
    return sum(1 for символ in line if символ.lower() in "аеёиоуыэюя")
line = "Привет, мир!"
print(f"В '{line}' {vowel_count(line)} гласных")
