def decimal_to_binary(decimal):
  """Переводит десятичное число в двоичное."""
  return bin(decimal)[2:]

def binary_to_decimal(binary):
  """Переводит двоичное число в десятичное."""
  return int(binary, 2)

def binary_to_octal(binary):
  """Переводит двоичное число в восьмеричное."""
  return oct(binary_to_decimal(binary))[2:]

def binary_to_hexadecimal(binary):
  """Переводит двоичное число в шестнадцатеричное."""
  return hex(binary_to_decimal(binary))[2:].upper()

def decimal_to_octal(decimal):
  """Переводит десятичное число в восьмеричное."""
  return oct(decimal)[2:]

def decimal_to_hexadecimal(decimal):
  """Переводит десятичное число в шестнадцатеричное."""
  return hex(decimal)[2:].upper()

def octal_to_decimal(octal):
  """Переводит восьмеричное число в десятичное."""
  return int(octal, 8)

def hexadecimal_to_decimal(hexadecimal):
  """Переводит шестнадцатеричное число в десятичное."""
  return int(hexadecimal, 16)

def binary_addition(num1, num2):
  """Сложение двоичных чисел."""
  return bin(int(num1, 2) + int(num2, 2))[2:]

def binary_subtraction(num1, num2):
  """Вычитание двоичных чисел."""
  return bin(int(num1, 2) - int(num2, 2))[2:]

def binary_multiplication(num1, num2):
  """Умножение двоичных чисел."""
  return bin(int(num1, 2) * int(num2, 2))[2:]

def binary_division(num1, num2):
  """Деление двоичных чисел."""
  return bin(int(num1, 2) // int(num2, 2))[2:]

def octal_addition(num1, num2):
  """Сложение восьмеричных чисел."""
  return oct(int(num1, 8) + int(num2, 8))[2:]

def octal_subtraction(num1, num2):
  """Вычитание восьмеричных чисел."""
  return oct(int(num1, 8) - int(num2, 8))[2:]

def hexadecimal_addition(num1, num2):
  """Сложение шестнадцатеричных чисел."""
  return hex(int(num1, 16) + int(num2, 16))[2:].upper()

def hexadecimal_subtraction(num1, num2):
  """Вычитание шестнадцатеричных чисел."""
  return hex(int(num1, 16) - int(num2, 16))[2:].upper()

while True:
  print("Выберите операцию:")
  print("1. Десятичное в двоичное")
  print("2. Двоичное в десятичное")
  print("3. Двоичное в восьмеричное")
  print("4. Двоичное в шестнадцатеричное")
  print("5. Десятичное в восьмеричное")
  print("6. Десятичное в шестнадцатеричное")
  print("7. Восьмеричное в десятичное")
  print("8. Шестнадцатеричное в десятичное")
  print("9. Сложение двоичных чисел")
  print("10. Вычитание двоичных чисел")
  print("11. Умножение двоичных чисел")
  print("12. Деление двоичных чисел")
  print("13. Сложение восьмеричных чисел")
  print("14. Вычитание восьмеричных чисел")
  print("15. Сложение шестнадцатеричных чисел")
  print("16. Вычитание шестнадцатеричных чисел")
  print("17. Выход")

  choice = input("Введите номер операции: ")

  if choice == '1':
    decimal = int(input("Введите десятичное число: "))
    print("Двоичное число:", decimal_to_binary(decimal))
  elif choice == '2':
    binary = input("Введите двоичное число: ")
    print("Десятичное число:", binary_to_decimal(binary))
  elif choice == '3':
    binary = input("Введите двоичное число: ")
    print("Восьмеричное число:", binary_to_octal(binary))
  elif choice == '4':
    binary = input("Введите двоичное число: ")
    print("Шестнадцатеричное число:", binary_to_hexadecimal(binary))
  elif choice == '5':
    decimal = int(input("Введите десятичное число: "))
    print("Восьмеричное число:", decimal_to_octal(decimal))
  elif choice == '6':
    decimal = int(input("Введите десятичное число: "))
    print("Шестнадцатеричное число:", decimal_to_hexadecimal(decimal))
  elif choice == '7':
    octal = input("Введите восьмеричное число: ")
    print("Десятичное число:", octal_to_decimal(octal))
  elif choice == '8':
    hexadecimal = input("Введите шестнадцатеричное число: ")
    print("Десятичное число:", hexadecimal_to_decimal(hexadecimal))
  elif choice == '9':
    num1 = input("Введите первое двоичное число: ")
    num2 = input("Введите второе двоичное число: ")
    print("Сумма:", binary_addition(num1, num2))
  elif choice == '10':
    num1 = input("Введите первое двоичное число: ")
    num2 = input("Введите второе двоичное число: ")
    print("Разность:", binary_subtraction(num1, num2))
  elif choice == '11':
    num1 = input("Введите первое двоичное число: ")
    num2 = input("Введите второе двоичное число: ")
    print("Произведение:", binary_multiplication(num1, num2))
  elif choice == '12':
    num1 = input("Введите первое двоичное число: ")
    num2 = input("Введите второе двоичное число: ")
    print("Частное:", binary_division(num1, num2))
  elif choice == '13':
    num1 = input("Введите первое восьмеричное число: ")
    num2 = input("Введите второе восьмеричное число: ")
    print("Сумма:", octal_addition(num1, num2))
  elif choice == '14':
    num1 = input("Введите первое восьмеричное число: ")
    num2 = input("Введите второе восьмеричное число: ")
    print("Разность:", octal_subtraction(num1, num2))
  elif choice == '15':
    num1 = input("Введите первое шестнадцатеричное число: ")
    num2 = input("Введите второе шестнадцатеричное число: ")
    print("Сумма:", hexadecimal_addition(num1, num2))
  elif choice == '16':
    num1 = input("Введите первое шестнадцатеричное число: ")
    num2 = input("Введите второе шестнадцатеричное число: ")
    print("Разность:", hexadecimal_subtraction(num1, num2))
  elif choice == '17':
    break
  else:
    print("Неверный выбор. Пожалуйста, введите число от 1 до 17.")
