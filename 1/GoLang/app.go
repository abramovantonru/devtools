package main

import (
"bufio"
"fmt"
"os"
"strconv"
"strings"
)

func reset()  {
	fmt.Println("\033[H\033[2J")
}

func delimiter()  {
	fmt.Println("---------------------")
}

var (
	n int64
	system [][]float64
	roots []float64
	i int64
	j int64
	k float64
)

func main() {
	invite()

	n = getSystemCount()
	initSystem()

	inputSystem()
	printSystem()

	if !searchRoots(){
		return
	}

	showAnswer()
}

func invite() {
	reset()
	fmt.Println("Программа для решения систем уравнений методом Гаусса.")
	fmt.Println("Для выхода используйте комбинацию клавиш 'Ctrl+C'.")
}

func inputSystem()  {
	fmt.Println("Заполните систему числами для нахождения корней.")
	fmt.Println("Все неверно введенные данные будут считаться как '0.00'!")
	for i = 0; i < n; i++{
		for j = 0; j <= n; j++{
			system[i][j] = getSystemsElement(i, j)
		}
	}
}


func initSystem() {
	system = make([][]float64, n)
	for i := range system {
		system[i] = make([]float64, n + 1)
	}
	roots = make([]float64, n)
}

func getFloat(string string) float64{
	i, _ := strconv.ParseFloat(string, 64)
	return i
}


func getInt(string string) int64{
	i, _ := strconv.ParseInt(string, 0, 64)
	return i
}

func getSystemsElement(i int64, j int64) float64{
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(fmt.Sprintf("Введите элемент системы [%d;%d] = ", i , j))
	input, _ := reader.ReadString('\n')
	input = strings.Replace(input, "\n", "", -1)
	float := getFloat(input)
	return float
}

func getSystemCount() int64{
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Введите число уравнений системы (Примечание: больше одного) = ")
	input, _ := reader.ReadString('\n')
	input = strings.Replace(input, "\n", "", -1)
	count := getInt(input)
	if count <= 1{
		fmt.Println("Не верно указано число уравнений! Попробуйте еще раз.")
		return getSystemCount()
	} else {
		return count
	}
}

func printSystem() {
	fmt.Println("Ваша система: ")
	delimiter()
	for i := range system {
		var line = ""
		for j := range system[i] {
			line += fmt.Sprintf(" %v ", 	system[i][j])
		}
		fmt.Println(line)
	}
	delimiter()
}

func swapRows(j int64){
	for i = j + 1; i < n; i++{
		if system[i][j] != 0 {
			for j = 0; j <= n; j++{
				k = system[i - 1][j]
				system[i - 1][j] = system[i][j]
				system[i][j] = k
			}
		}
	}
}

func division(result *float64, a float64, b float64) bool{
	if b == 0{
		return false
	}else{
		*result = a / b
		return true
	}
}

func searchRoots() bool {
	var item int64
	for item = 0; item < (n - 1); item++ {
		if system[item][item] == 0 {
			swapRows(item)
		}

		for j = n; j >= item; j-- {
			if !division(&system[item][j], system[item][j], system[item][item]){
				fmt.Println("Ответ: Система не имеет корней!")
				return false
			}
		}

		for i = item + 1; i < n; i++ {
			for j = n; j >= item; j-- {
				system[i][j] -= system[item][j] * system[i][item]
			}
		}

		if !division(&roots[n - 1], system[n - 1][n], system[n - 1][n - 1]){
			fmt.Println("Ответ: Система не имеет корней!")
			return false
		}

		for i = n - 2; i >= 0; i-- {
			k = 0
			for j = n - 1; j > i; j-- {
				k = system[i][j]*roots[j] + k
			}
			roots[i] = system[i][n] - k
		}
	}
	return true
}

func showAnswer(){
	fmt.Println("Ответ: ")
	delimiter()
	for i := range roots{
		fmt.Println(roots[i])
		fmt.Println(fmt.Sprintf("x%d = %6.2f", i + 1, roots[i]))
	}
	delimiter()
}