# Завдання 1

filtered_numbers = [x for x in range(1, 101) if x % 3 == 0 and x % 5 != 0]
print("Числа, кратні 3, але не кратні 5:", filtered_numbers)


# Завдання 2 

celsius = [0, 10, 20, 30, 40, 100]
fahrenheit = [round(c * 9/5 + 32, 1) for c in celsius]
print("Температури у Фаренгейтах:", fahrenheit)


# Завдання 3

even_squares = [x**2 for x in range(1, 51) if x % 2 == 0]
print("Квадрати парних чисел:", even_squares)


# Завдання 4 

text = "Python is amazing and powerful language"
word_lengths = [len(word) for word in text.split()]
print("Довжини слів:", word_lengths)


# Завдання 5 

composite_numbers = [
    n for n in range(2, 101)
    if len([d for d in range(1, n + 1) if n % d == 0]) > 2
]
print("Складні числа від 1 до 100:", composite_numbers)
