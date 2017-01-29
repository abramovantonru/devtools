const readlineSync = require('readline-sync'); // модуль для синхронного чтения ввода с клавиатуры

console.reset = function () { // Очищает консоль
	return process.stdout.write('\033c');
};

console.delimiter = function(){ // Рисует разделитель
	console.log('---------------------');
};

var
	n, system, roots, // основные переменные
	i, j, k; // вспомогательные переменные

/**
 * Главный поток программы
 * @global {array} system
 * @global {array} roots
 * @global {int} n
 * @global {int} i
 * @global {int} j
 * @var {array} answer
 * @return {int} code
 */
function main(){
	invite(); // приглашение
	
	n = getSystemsCount(); // количество систем уравнений
	
	init(); // заполнение массивов для системы
	
	for(i = 0; i < n; i++)
		for(j = 0; j <= n; j++)
			system[i][j] = getSystemsElement(i, j); // заполнение системы пользователем
	
	printSystem(); // заполненная система
	
	searchRoots(); // поиск корней
	
	var answer = getAnswer(); // подготовить ответ
	showAnswer(answer); // показать ответ
	
	return 1;
}

/**
 * Инициализация массивов для системы
 * @global {array} system
 * @global {array} roots
 * @global {int} n
 * @global {int} i
 */
function init() {
	system = new Array(n); // система
	roots = new Array(n); // корни
	
	for(i = 0; i < n; i++)
		system[i] = new Array(n);
}

/**
 * Приглашение
 * Очищает экран, выводит приглашение
 */
function invite() {
	console.reset();
	console.log('Программа для решения систем уравнений методом Гаусса.');
	console.log('Для выхода используйте комбинацию клавиш "Ctrl+C".');
}

/**
 * Обработка введенной строки
 * Число ? вернуть число : вернуть false
 * @param string
 * @return {float} number || {boolean} false
 */
function getFloat(string){
	var int = parseFloat(string);
	if(!isNaN(int))
		return int;
	else
		return false;
}

/**
 * Обработка введенной строки
 * Натуральное число ? вернуть число : вернуть false
 * @param string
 * @return {int} number || {boolean} false
 */
function getInt(string) {
	var int = parseInt(string);
	if(!isNaN(int))
		return int;
	else
		return false;
}

/**
 * Получение элемента системы с индексами [i,j]
 * Число ? венуть число : вернуть ошибку и еще один запрос ввода элемента системы.
 * @param i
 * @param j
 * @returns {float} element || {function} self
 */
function getSystemsElement(i, j){
	var element = getFloat(readlineSync.question('Введите элемент системы [' + i + ';' + j + '] = '));
	if(element)
		return element;
	else{
		console.log('Не верно указан элемент системы! Попробуйте еще раз.');
		return getSystemsElement(i, j);
	}
}

/**
 * Получение количества уравнений системы
 * Натуральное число ? венуть число : вернуть ошибку и еще один запрос ввода количества уравнений системы.
 * @returns {int} count || {function} self
 */
function getSystemsCount() {
	var count = readlineSync.question('Введите число уравнений системы (Примечание: больше одного) = ');
	if(getInt(count) <= 1){
		console.log('Не верно указано число уравнений! Попробуйте еще раз.');
		return getSystemsCount();
	}
	else {
		return (count);
	}
}

/**
 * Рисует заполненную систему
 * @global {array} system
 * @global {int} i
 * @global {int} j
 * @var {string} line
 */
function printSystem() {
	console.delimiter();
	console.log('Ваша система: ');
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
 * Поиск корней методом Гаусса
 * @global {array} system
 * @global {array} roots
 * @global {int} n
 * @global {int} i
 * @global {int} j
 * @var {int} item
 */
function searchRoots() {
	for(var item = 0; item < (n - 1); item++) {
		if (system[item][item] == 0)
			swapRows(item);
		
		for (j = n; j >= item; j--)
			system[item][j] /= system[item][item];
		
		for (i = item + 1; i < n; i++)
			for (j = n; j >= item; j--)
				system[i][j] -= system[item][j] * system[i][item];
	}
	
	roots[n - 1] = system[n - 1][n] / system[n - 1][n - 1];
	for (i = n - 2; i >= 0; i--) {
		k = 0;
		for (j = n - 1; j > i; j--)
			k = (system[i][j] * roots[j]) + k;
		roots[i] = system[i][n] - k;
	}
}

/**
 * Получает ответ, удаляя NaN значения
 * @global {array} roots
 * @global {int} i
 * @returns {array} answer
 */
function getAnswer() {
	var answer = [];
	for(i = 0; i < roots.length; i++)
		if(!isNaN(roots[i]))
			answer.push(roots[i]);
	return answer;
}

/**
 * Показывает ответ по массиву
 * @global {int} i
 * @param {array} answer
 */
function showAnswer(answer) {
	if(answer.length){
		console.log('Ответ:');
		console.delimiter();
		for(i = 0; i < answer.length; i++)
			console.log('x' + (i + 1) + ' = ' + answer[i]);
		console.delimiter();
	}else{
		console.log('Ответ: Система не имеет корней!');
	}
}

main();