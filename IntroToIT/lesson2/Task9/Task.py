#INTRO TO IT 2nd COURSE
# Задача 9: Палиндром ли это?
# Определи, является ли введенная строка палиндромом.
def this_palindrome(line):
    return line == line[::-1]
line = "радар"
print(f"Является ли '{line}' палиндромом? {this_palindrome(line)}")
