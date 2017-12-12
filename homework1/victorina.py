""" program 'victorina' """

list_of_quastion = {
				1 : "Что в python является объектом ? ",
				2 : "Какой это тип данных: '4.0' ? ",
				3 : "Какой будет ответ у данного вырожения: 10 / 5 = ? ",
				4 : "Что выведет эта функция: print(bool(-1)) ? ",
				5 : "Как называется стандарт кодирования символов используемый в Python3 ? ",
				6 : "Какая встроенная функция в Python3 служит для вывода данных на экран ? ",
				7 : "Какой условный оператор в Python используется для проверки истиности вырожения ? ",
				8 : "Какой цикл в Python используется для переборки итераторов ? ",
				9 : "Какое число будет выведено последним ?:\nn = 10\nwhile n > 5:\n\tprint(n)\n\tn = n - 1",
				10 : "Какая функция в Python служит для пользовательского ввода ?",
				}

list_of_answers = {
				1 : 'all', 2 : 'float', 3 : '2.0', 4 : 'true', 5 : 'unicode', 6 : 'print()',
				7 : 'if', 8 : 'for', 9 : '6', 10 : 'input()',
				}

print("Добро пожаловать в игру 'Victorina by Python\n")
print("Условия игры:")
print("\t - oтветы пишите на английском\n\t - регистр значения не играет\n")

correct_answer = 0				
for key in list_of_quastion:
	if input(list_of_quastion[key]).lower() == list_of_answers[key]:
		print("Правильно!\n")
		correct_answer += 1
	else:
		print("Неверно\n")

if 4 < correct_answer < 7:
	wishes = "Хорошо!"
elif 6 < correct_answer < 10:
	wishes = "Очень хорошо!"
elif correct_answer == 10:
	wishes = "Отлично!"
elif 1 <= correct_answer <= 4:
	wishes = "Не плохо"
elif correct_answer == 0:
	wishes = "Вы не дали ни одного правильного ответа =(" 


print("Вы дали {} правильных ответов, {}".format(correct_answer, wishes))
