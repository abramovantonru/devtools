def console_reset():
	print(chr(27) + "[2J")
	return


def delimiter():
	print('---------------------')
	return


i = 0
j = 0
k = 0

n = 0
system = []
roots = []


def main():
	global i, j, k, n, system

	invite()

	n = get_system_count()

	init()

	for i in range(n):
		for j in range(n + 1):
			system[i][j] = get_system_element(i, j)

	print_system()

	if not search_roots():
		return 0

	show_answer()

	return 1


def init():
	global system, roots, i, n
	system = [[0] * (n + 1) for i in range(n)]
	for i in range(n):
		roots.append(0)
	return


def invite():
	console_reset()
	print('Программа для решения систем уравнений методом Гаусса.')
	print('Для выхода используйте комбинацию клавиш "Ctrl+C".')
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


def get_system_element(i, j):
	element = get_float(input('Введите элемент системы [' + str(i) + ';' + str(j) + '] = '))
	if element is False:
		print('Не верно указан элемент системы! Попробуйте еще раз.')
		return get_system_element(i, j)
	else:
		return element


def get_system_count():
	count = get_int(input('Введите число уравнений системы (Примечание: больше одного) = '))
	if count <= 1:
		print('Не верно указано число уравнений! Попробуйте еще раз.')
		return get_system_count()
	else:
		return count


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


def swap_rows(j):
	global i, k, system
	for i in range(j + 1, n, 1):
		if system[i][j] != 0:
			for j in range(n + 1):
				k = system[i - 1][j]
				system[i - 1][j] = system[i][j]
				system[i][j] = k
	return


def search_roots():
	global i, j, k, n, system, roots
	for item in range(n - 1):
		if system[item][item] == 0:
			swap_rows(item)

		for j in range(n, item - 1, -1):
			try:
				system[item][j] /= system[item][item]
			except:
				print('Ответ: Система не имеет корней!')
				return False

		for i in range(item + 1, n, 1):
			for j in range(n, item - 1, -1):
				system[i][j] -= system[item][j] * system[i][item]

	try:
		roots[n - 1] = system[n - 1][n] / system[n - 1][n - 1]
	except:
		print('Ответ: Система не имеет корней!')
		return False

	for i in range(n - 2, -1, -1):
		k = 0
		for j in range(n - 1, i, -1):
			k = system[i][j] * roots[j] + k
		roots[i] = system[i][n] - k
	return True


def show_answer():
	global i, roots
	print('Ответ:')
	delimiter()
	for i in range(len(roots)):
		print('x' + str(i + 1) + ' = ' + str(roots[i]))
	delimiter()
	return


main()