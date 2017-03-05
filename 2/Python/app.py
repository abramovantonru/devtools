N = 4
M = 5


class Table:
	sum = 0.0
	plan = [0.0] * N

	def __init__(self):
		self.sum = 0.0
		self.plan = [0.0] * N


Income = [[0 for x in range(N)] for y in range(M + 1)]
Profitability = [
	[0.00, 0.00, 0.00, 0.00],
	[0.28, 0.25, 0.15, 0.20],
	[0.23, 0.21, 0.13, 0.18],
	[0.22, 0.18, 0.13, 0.14],
	[0.20, 0.16, 0.13, 0.12],
	[0.18, 0.15, 0.12, 0.11]
]
Optimal = [[0 for z in range(N)] for t in range(M + 1)]
Best = [0] * (M + 1)
maxI = 0


def begin():
	global Optimal, Income, N, M, Profitability, Best, maxI

	for i in range(M + 1):
		for j in range(N):
			Optimal[i][j] = Table()

	print()
	print('Моделирования оптимального плана инвестиций методом Беллмана.')
	print()

	for i in range(M + 1):
		for j in range(N):
			Income[i][j] = Profitability[i][j] * i

	for i in range(M + 1):
		for j in range(N):
			Optimal[i][0].sum = Income[i][0]
			Optimal[i][0].plan[0] = i

	for i in range(M + 1):
		for j in range(1, N, 1):
			for k in range(i + 1):
				Best[k] = Optimal[k][j - 1].sum + Income[i - k][j]

			maxI = 0

			for k in range(i + 1):
				if Best[k] > Best[maxI]:
					maxI = k

			Optimal[i][j].sum = Best[maxI]
			Optimal[i][j].plan = Optimal[maxI][j - 1].plan
			Optimal[i][j].plan[j] = i - maxI

	print("Оптимальный план инвестиций:")
	print("----------------------------")

	for i in range(N):
		print("В проект № " + str(i + 1) + " инвестировать " + str(round(Optimal[M][N - 1].plan[i])) + "млн.")

	print("----------------------------")
	print("Планируется получить доход: " + str(Optimal[M][N - 1].sum) + " млн.")
	return 0


begin()
