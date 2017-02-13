const readlineSync = require('readline-sync'); // модуль для синхронного чтения ввода с клавиатуры

var
	n, system, roots, // основные переменные
	i, j, k; // вспомогательные переменные

/**
 * Главный поток программы
 * @var {int} n
 * @return {int} code
 */
function main(){
	invite(); // приглашение
	
	n = getSystemsCount(); // количество систем уравнений

	initSystem(); // заполнение массивов для системы
	
	inputSystem(); // ввод системы
	printSystem(); // заполненная система
	
	if(!searchRoots()) // поиск корней
		return 0;

	showAnswer(); // показать ответ

	return 1;
}

/**
 * Инициализация массивов для системы
 * @global {array} system
 * @global {array} roots
 * @global {int} n
 * @global {int} i
 */
function initSystem() {
	system = new Array(n); // система
	roots = new Array(n); // корни

	for(i = 0; i < n; i++)
		system[i] = new Array(n);
}

/**
 * Очищает консоль
 */
console.reset = function () {
	return process.stdout.write('\033c');
};

/**
 * Рисует разделитель
 */
console.delimiter = function(){
	console.log('---------------------');
};

/**
 * Приглашение
 * Очищает экран, выводит приглашение
 */
function invite() {
	console.reset();
	console.log('Программа для решения систем уравнений методом Гаусса.');
}

/**
 * Обработка введенной строки
 * Число ? вернуть число : вернуть false
 * @param string
 * @return float or boolean
 */
function getFloat(string){
	var int = parseFloat(string);
	if(!isNaN(int) || int == 0)
		return int;
	else
		return false;
}

/**
 * Обработка введенной строки
 * Натуральное число ? вернуть число : вернуть false
 * @param string
 * @return integer or boolean
 */
function getInt(string) {
	var int = parseInt(string);
	if(!isNaN(int))
		return int;
	else
		return false;
}

/**
 * Ввод системы
 * @global {array} system
 * @global {int} n
 * @global {int} i
 * @global {int} j
 */
function inputSystem() {
	console.log('Заполните систему числами для нахождения корней.');
	for(i = 0; i < n; i++)
		for(j = 0; j <= n; j++)
			system[i][j] = getSystemsElement(i, j); // заполнение системы пользователем
}

/**
 * Получение элемента системы с индексами [i,j]
 * Число ? вернуть число : вернуть ошибку и еще один запрос ввода элемента системы.
 * @param i
 * @param j
 * @returns float or self
 */
function getSystemsElement(i, j){
	var element = getFloat(readlineSync.question('Введите элемент системы [' + i + ';' + j + '] = '));
	if(element !== false)
		return element;
	else{
		console.log('Не верно указан элемент системы! Попробуйте еще раз.');
		return getSystemsElement(i, j);
	}
}

/**
 * Получение количества уравнений системы
 * Натуральное число ? венуть число : вернуть ошибку и еще один запрос ввода количества уравнений системы.
 * @returns integer or self
 */
function getSystemsCount() {
	var count = getInt(readlineSync.question('Введите число уравнений системы (Примечание: больше одного) = '));
	if(count <= 1){
		console.log('Не верно указано число уравнений! Попробуйте еще раз.');
		return getSystemsCount();
	}
	else
		return count;
}

/**
 * Рисует заполненную систему
 * @global {array} system
 * @global {int} i
 * @global {int} j
 * @var {string} line
 */
function printSystem() {
	console.log('Ваша система: ');
	console.delimiter();
	for(i = 0; i < system.length; i++){
		var line = '';
		for(j = 0; j < system[i].length; j++)
			line += ' ' + system[i][j] + ' ';
		console.log(line);
	}
	console.delimiter();
}

/**
 * Смена строк
 * @global {array} system
 * @global {int} i
 * @global {int} k
 * @param {int} j
 */
function swapRows(j) {
	for(i = j + 1;i < n; i++) {
		if(system[i][j] !== 0) {
			for(j = 0; j <= n; j++) {
				k = system[i - 1][j];
				system[i - 1][j] = system[i][j];
				system[i][j] = k;
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
function division(a, b){
	if(b == 0)
		return false;
	else
		return a / b;
}

/**
 * Поиск корней методом Гаусса
 * @global {array} system
 * @global {array} roots
 * @global {int} n
 * @global {int} i
 * @global {int} j
 * @global {float} k
 * @var {int} item
 * @returns boolean
 */
function searchRoots() {
	var result = null;
	for(var item = 0; item < (n - 1); item++) {
		if (system[item][item] == 0)
			swapRows(item);

		for (j = n; j >= item; j--) {
			result = division(system[item][j], system[item][item]);
			if(result === false){
				console.log('Ответ: Система не имеет корней!');
				return false;
			}else{
				system[item][j] = result;
			}
		}
		
		for (i = item + 1; i < n; i++)
			for (j = n; j >= item; j--)
				system[i][j] -= system[item][j] * system[i][item];
	}

	result = division(system[n - 1][n], system[n - 1][n - 1]);
	if(result === false){
		console.log('Ответ: Система не имеет корней!');
		return false;
	}else{
		roots[n - 1] = result;
	}

	for (i = n - 2; i >= 0; i--) {
		k = 0;
		for (j = n - 1; j > i; j--)
			k = system[i][j] * roots[j] + k;
		roots[i] = system[i][n] - k;
	}
	return true;
}

/**
 * Показывает ответ по массиву
 * @global {array} roots
 * @global {int} i
 */
function showAnswer() {
	console.log('Ответ:');
	console.delimiter();
	for(i = 0; i < roots.length; i++)
		console.log('x' + (i + 1) + ' = ' + parseFloat(roots[i].toFixed(2)));
	console.delimiter();
}

main();
