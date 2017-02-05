import random

n = 0
i = 0
j = 0

random_type = False  # false = int / true = float
random_min = -100
random_max = 100

consts = []
set_consts = False

variables = []
set_variables = False

results = []
system = []


def main():
	global n, i, j, variables, set_variables, consts, set_consts

	invite()

	n = get_system_count()

	init()

	if not q_random():
		if q_consts():
			set_consts = True
			for i in range(n):  # индекс уравнения
				for j in range(n):  # индекс константы
					consts[i][j] = get_const_element(i, j)
		if q_vars():
			set_variables = True
			for i in range(n):  # индекс переменной
				variables[i] = get_var_element(i)
		gen()
	else:
		if q_random_range():
			get_range()
		gen_random()

	print_system()
	print_roots()

	return


def invite():
	console_reset()
	delimiter()
	print('Программа для генерации систем уравнений.')
	print('Возможности:')
	print('    - генерировать полностю случайную систему')
	print('    - генерировать типовое случайное уравнение')
	print('    - генерировать только не заданные параметры')
	print('    - генерировать ответ по всем заданным параметрам')
	delimiter()
	return


def console_reset():
	print(chr(27) + "[2J")
	return


def delimiter():
	print('---------------------')
	return


def init():
	global i, consts, variables, results
	consts = [[0] * n for i in range(n)]
	variables = [0 for i in range(n)]
	results = [[0] * n for i in range(n)]
	return


def get_int(string):
	try:
		integer = int(string)
		return integer
	except ValueError:
		return False


def get_float(string):
	try:
		double = float(string)
		return double
	except ValueError:
		return False


def get_const_element(i, j):
	element = get_float(input('[' + str(i + 1) + ' уравнение] Введите постоянную при x' + str(j + 1) + ' = '))
	if element is False:
		print('Не верно указана постоянная! Попробуйте еще раз.')
		return get_const_element(i, j)
	else:
		return element


def get_var_element(i):
	element = get_float(input('Введите переменную x' + str(j + 1) + ' = '))
	if element is False:
		print('Не верно указана постоянная! Попробуйте еще раз.')
		return get_var_element(i)
	else:
		return element


def get_system_count():
	count = get_int(input('Введите количество неизвестных величин в системе (от 2 до 6) = '))
	if not count >= 2 and count <= 6:
		print('Не верно указано количество неизвестных величин! Попробуйте еще раз.')
		return get_system_count()
	else:
		return count


def q_vars():
	answer = input('Задать переменные? (Y/N) = ')
	if answer == 'Y' or answer == 'y':
		return True
	elif answer == 'N' or answer == 'n':
		return False
	else:
		return q_random()


def q_consts():
	answer = input('Задать постоянные? (Y/N) = ')
	if answer == 'Y' or answer == 'y':
		return True
	elif answer == 'N' or answer == 'n':
		return False
	else:
		return q_random()


def get_range():
	global random_min, random_max
	random_min = get_random_min()
	random_max = get_random_max()
	return 1


def get_random_min():
	r_min = get_float(input('Введите минимум = '))
	if r_min is False:
		print('Не верно задан минимум! Попробуйте еще раз.')
		return get_random_min()
	else:
		return r_min


def get_random_max():
	r_max = get_float(input('Введите максимум = '))
	if r_max is False:
		print('Не верно задан максимум! Попробуйте еще раз.')
		return get_random_max()
	else:
		return r_max


def get_random_type():
	answer = input('Использовать только целые случайные числа? (Y/N) = ')
	if answer == 'Y' or answer == 'y':
		return False
	elif answer == 'N' or answer == 'n':
		return True
	else:
		return get_random_type()


def q_random_range():
	print('Примечание: по умолчанию минимум = ' + str(random_min) + ' и максимум = ' + str(random_max) + '!')
	answer = input('Задать диапазон для случайных чисел? (Y/N) = ')
	if answer == 'Y' or answer == 'y':
		return True
	elif answer == 'N' or answer == 'n':
		return False
	else:
		return q_random_range()


def q_random():
	answer = input('Сгенерировать случайное уравнение? (Y/N) = ')
	if answer == 'Y' or answer == 'y':
		return True
	elif answer == 'N' or answer == 'n':
		return False
	else:
		return q_random()


def gen_random():
	global random_type
	random_type = get_random_type()
	return


def gen():
	global variables, consts, set_variables, n, i, j, random_min, random_max, results, random_type
	if not set_variables:
		print('Не заданы переменные.')
		random_type = get_random_type()
		if q_random_range():
			get_range()
		for i in range(n):
			if random_type:
				variables[i] = random.uniform(random_min, random_max)
			else:
				variables[i] = random.randint(int(random_min), int(random_max))

	if not set_consts:
		print('Не заданы постоянные.')
		random_type = get_random_type()
		if q_random_range():
			get_range()
		for i in range(n):
			for j in range(n):
				if random_type:
					consts[i][j] = random.uniform(random_min, random_max)
				else:
					consts[i][j] = random.randint(int(random_min), int(random_max))

	for i in range(n):
		result = 0.00
		for j in range(n):
			result += variables[j] * consts[i][j]
		results[i] = result
	return


def print_system():
	global i, j, n, consts, variables
	print('Ваша система:')
	delimiter()
	for i in range(n):
		line = ''
		for j in range(n):
			line += str(consts[i][j]) + ' * x' + str(j + 1)
			if not j == n - 1:
				line += ' + '
			else:
				line += ' = ' + str(results[i])
		print(line)
	delimiter()
	return


def print_roots():
	global i, variables
	print('Ответ:')
	delimiter()
	for i in range(len(variables)):
		print('x' + str(i + 1) + ' = ' + str(variables[i]))
	delimiter()
	return


main()