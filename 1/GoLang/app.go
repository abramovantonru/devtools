package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var (
	n int64 // основные переменные
	system [][]float64
	roots []float64
	i int64 // вспомогательные переменные
	j int64
	k float64
)

/**
 * Главный поток программы
 * @global {int} n
 */
func main(){
	invite() // приглашение

	n = getSystemCount() // количество систем уравнений

	initSystem() // заполнение массивов для системы

	inputSystem() // ввод системы
	printSystem() // поиск корней

	if !searchRoots(){ // поиск корней
		return
	}

	showAnswer() // показать ответ
}

/**
 * Приглашение
 * Очищает экран, выводит приглашение
 */
func invite() {
	reset()
	fmt.Println("Программа для решения систем уравнений методом Гаусса.")
}

/**
 * Очищает консоль
 */
func reset()  {
	fmt.Println("\033[H\033[2J")
}

/**
 * Рисует разделитель
 */
func delimiter()  {
	fmt.Println("---------------------")
}

/**
 * Ввод системы
 * @global {array} system
 * @global {int} n
 * @global {int} i
 * @global {int} j
 */
func inputSystem()  {
	fmt.Println("Заполните систему числами для нахождения корней.")
	fmt.Println("Все неверно введенные данные будут считаться как '0.00'!")
	for i = 0; i < n; i++{
		for j = 0; j <= n; j++{
			system[i][j] = getSystemsElement(i, j)
		}
	}
}

/**
 * Инициализация массивов для системы
 * @global {array} system
 * @global {array} roots
 * @global {int} n
 * @global {int} i
 */
func initSystem() {
	system = make([][]float64, n)
	for i := range system {
		system[i] = make([]float64, n + 1)
	}
	roots = make([]float64, n)
}

/**
 * Обработка введенной строки
 * Число ? вернуть число : вернуть 0.00
 * @param string
 * @return float
 */
func getFloat(string string) float64{
	i, _ := strconv.ParseFloat(string, 64)
	return i
}

/**
 * Обработка введенной строки
 * Натуральное число ? вернуть число : вернуть 0
 * @param string
 * @return integer or boolean
 */
func getInt(string string) int64{
	i, _ := strconv.ParseInt(string, 0, 64)
	return i
}

/**
 * Получение элемента системы с индексами [i,j]
 * Число ? вернуть число : вернуть 0.00
 * @param i
 * @param j
 * @returns float or self
 */
func getSystemsElement(i int64, j int64) float64{
	reader := bufio.NewReader(os.Stdin)
	fmt.Print(fmt.Sprintf("Введите элемент системы [%d;%d] = ", i , j))
	input, _ := reader.ReadString('\n')
	input = strings.Replace(input, "\n", "", -1)
	float := getFloat(input)
	return float
}

/**
 * Получение количества уравнений системы
 * Натуральное число ? венуть число : вернуть ошибку и еще один запрос ввода количества уравнений системы.
 * @returns integer or self
 */
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

/**
 * Рисует заполненную систему
 * @global {array} system
 * @global {int} i
 * @global {int} j
 * @var {string} line
 */
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

/**
 * Смена строк
 * @global {array} system
 * @global {int} i
 * @global {int} k
 * @param {int} j
 */
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

/**
 * Безопасное деление
 * @param a
 * @param b
 * @returns boolean || number
 */
func division(result *float64, a float64, b float64) bool{
	if b == 0{
		return false
	}else{
		*result = a / b
		return true
	}
}

/**
 * Поиск корней методом Гаусса
 * @global {array} system
 * @global {array} roots
 * @global {int} n
 * @global {int} i
 * @global {int} j
 * @global {int} k
 * @var {int} item
 * @returns boolean
 */
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

/**
 * Показывает ответ по массиву
 * @global {array} roots
 * @global {int} i
 */
func showAnswer(){
	fmt.Println("Ответ: ")
	delimiter()
	for i := range roots{
		fmt.Println(fmt.Sprintf("x%d = %6.2f", i + 1, roots[i]))
	}
	delimiter()
}
