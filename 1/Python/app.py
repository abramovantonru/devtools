i = 0  # вспомогательные переменные
j = 0
k = 0

n = 0  # основные переменные
system = []
roots = []


# Главный поток программы
# @ var{int} n
# @ return {int} code
def main():
	global n

	invite()  # приглашение

	n = get_system_count()  # количество систем уравнений

	init()  # заполнение массивов для системы

	input_system()  # ввод системы
	print_system()  # заполненная система

	if not search_roots():  # поиск корней
		return 0

	show_answer()  # показать ответ

	return 1


# Инициализация массивов для системы
# @global {array} system
# @global {array} roots
# @global {int} n
# @global {int} i
def init():
	global system, roots, i, n
	system = [[0] * (n + 1) for i in range(n)]
	for i in range(n):
		roots.append(0)
	return


# Очищает консоль
def console_reset():
	print(chr(27) + "[2J")
	return


# Рисует разделитель
def delimiter():
	print('---------------------')
	return


# Приглашение
# Очищает экран, выводит приглашение
def invite():
	console_reset()
	print('Программа для решения систем уравнений методом Гаусса.')
	return


# Обработка введенной строки
# Натуральное число ? вернуть число : вернуть false
# @param string
# @return integer or boolean
def get_int(string):
	try:
		integer = int(string)
		return integer
	except ValueError:
		return False


# Обработка введенной строки
# Число ? вернуть число : вернуть false
# @param string
# @return float or boolean
def get_float(string):
	try:
		double = float(string)
		return double
	except ValueError:
		return False


# Ввод системы
# @global {array} system
# @global {int} n
# @global {int} i
# @global {int} j
def input_system():
	global system, n, i, j
	for i in range(n):
		for j in range(n + 1):
			system[i][j] = get_system_element(i, j)
	return 1


# Получение элемента системы с индексами [i,j]
# Число ? вернуть число : вернуть ошибку и еще один запрос ввода элемента системы.
# @param i
# @param j
# @returns float or self
def get_system_element(i, j):
	element = get_float(input('Введите элемент системы [' + str(i) + ';' + str(j) + '] = '))
	if element is False:
		print('Не верно указан элемент системы! Попробуйте еще раз.')
		return get_system_element(i, j)
	else:
		return element


# Получение количества уравнений системы
# Натуральное число ? венуть число : вернуть ошибку и еще один запрос ввода количества уравнений системы.
# @returns integer or self
def get_system_count():
	count = get_int(input('Введите число уравнений системы (Примечание: больше одного) = '))
	if count <= 1:
		print('Не верно указано число уравнений! Попробуйте еще раз.')
		return get_system_count()
	else:
		return count


# Рисует заполненную систему
# @global {array} system
# @global {int} i
# @global {int} j
# @var {string} line
def print_system():
	global i, j, n, system
	print('Ваша система: ')
	delimiter()
	for i in range(len(system)):
		line = ''
		for j in range(len(system[i])):
			line += ' ' + str(system[i][j]) + ' '
		print(line)
	delimiter()
	return


# Смена строк
# @global {array} system
# @global {int} i
# @global {int} k
# @param {int} j
def swap_rows(j):
	global i, k, system
	for i in range(j + 1, n, 1):
		if system[i][j] != 0:
			for j in range(n + 1):
				k = system[i - 1][j]
				system[i - 1][j] = system[i][j]
				system[i][j] = k
	return


# Безопасное деление
# @param a
# @param b
# @returns boolean || number
def division(a, b):
	if b == 0:
		return False
	else:
		return a / b


# Поиск корней методом Гаусса
# @global {array} system
# @global {array} roots
# @global {int} n
# @global {int} i
# @global {int} j
# @global {float} k
# @var {int} item
# @returns boolean
def search_roots():
	global i, j, k, n, system, roots
	for item in range(n - 1):
		if system[item][item] == 0:
			swap_rows(item)

		for j in range(n, item - 1, -1):
			result = division(system[item][j], system[item][item])
			if not result:
				print('Ответ: Система не имеет корней!')
				return False
			else:
				system[item][j] = result

		for i in range(item + 1, n, 1):
			for j in range(n, item - 1, -1):
				system[i][j] -= system[item][j] * system[i][item]

	result = division(system[n - 1][n], system[n - 1][n - 1])
	if not result:
		print('Ответ: Система не имеет корней!')
		return False
	else:
		roots[n - 1] = result

	for i in range(n - 2, -1, -1):
		k = 0
		for j in range(n - 1, i, -1):
			k = system[i][j] * roots[j] + k
		roots[i] = system[i][n] - k
	return True


# Показывает ответ по массиву
# @global {array} roots
# @global {int} i
def show_answer():
	global i, roots
	print('Ответ:')
	delimiter()
	for i in range(len(roots)):
		print('x' + str(i + 1) + ' = ' + str(int(roots[i] * 100) / 100))
	delimiter()
	return


main()
