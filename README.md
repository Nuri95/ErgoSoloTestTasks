Задание 1

Имеются два файла f1.txt и f2.txt:

В файле f1.txt содержатся уникальные строковые идентификаторы, состоящие из латинских символов разной длины, разделенные между собой символом переноса строки.
В файле f2.txt содержатся числовые значения (целочисленные), разделенные между собой символом переноса строки.

Необходимо “объединить” данные файлы в генератор, возвращающий кортежи из двух элементов: строковый идентификатор (из f1.txt) и значение - число (из f2.txt), на соответствующих позициях в файлах. Если строковому идентификатору не хватило числового значения, то значением должно быть None. Числовые значения, которым не хватило строковых идентификаторов, нужно игнорировать.

Пример:

f1.txt:<br>
aa <br>
bbb <br>
c <br>
dddd <br>
<br>
f2.txt: <br>
123 <br>
321 <br>
0 <br>
<br>
Output: <br>
( "a", 123, ) <br>
( "bbb", 321, ) <br>
( "c", 0, ) <br>
( "dddd", None, ) <br>


Задание 2

Решение должно быть в виде SQL-запроса(-ов) (без Python)!

В базе данных содержатся 3 сущности — users, courses и saves:

users [ id, name ]
courses [ id, name ]
saves [ id, user_id, course_id, lesson_no, exercise_no, data ]

Таблица users содержит информацию о пользователях.
Таблица courses содержит информацию об обучающих курсах.
Таблица saves содержит информацию о результатах прохождения различных упражнений пользователями в определенных курсах. Каждое упражнение характеризуется 3 атрибутами: course_id, lesson_no, exercise_no. В каждом уроке каждого курса может быть несколько упражнений. Пользователи могут выполнять каждое упражнение в каждом курсе более одного раза. В таблице хранится информация обо всех попытках пользователя.

Напишите SQL-запрос(-ы), результатом которого будет выборка из двух полей: "Имя пользователя" и "Количество пройденных курсов". Курс считается пройденным, если суммарно по курсу выполнено 100 различных упражнений. Факт наличия записи в таблице saves — это показатель, что соответствующее упражнение было выполнено пользователем.


Задание 3

Для иностранных клиентов требуется корректировать стоимость продукта (базовая цена в рублях) в зависимости от курса валют на текущий момент времени. По адресу http://www.cbr.ru/scripts/XML_daily.asp находятся актуальные данные ЦБ РФ о курсах валют. Необходимо получить данные по соответствующему url и извлечь курсы доллара и евро по отношению к рублю. Для идентификации валюты использовать символьные коды (USD, EUR) или цифровые коды (840, 978).

Также необходимо предусмотреть кэширование выходных данных, чтобы при многократном обращении за курсом валют, реальный запрос по url делался только с определенной частотой. Кэш должен быть реализован с помощью паттерна делегирования, чтобы сторонний разработчик мог использовать свою реализацию кэша, ничего не меняя в вашем коде. Напиши 
свой базовый вариант кэша для данной задачи, который будет кэшировать данные на заданный интервал времени.

Формат выходных данных:

{
	'USD': Decimal(59.51),
    'EUR': Decimal(63.45)
}




Задание 4

Имеется csv-файл вида (данные не упорядочены):

email,name
test1@mail.ru,username1
test2@gmail.com,username2
test3@gmail.com,username3
test4@rambler.ru,username4
test5@ya.ru,username5
...
testN@yahoo.com,usernameN

Используя данные из csv-файла необходимо создать список чанков, в которых будут содержаться группы кортежей вида (email, username) с условием, что в каждом чанке почтовые домены не должны повторяться (в каждом чанке должно аккумулироваться максимальное число email'ов с уникальными доменами).

Формат выходных данных:


    (
    (
   	 ( ...@mail.ru, username1 ),
   	 ( ...@gmail.com, username2 ),
   	 ( ...@rambler.ru, username4 ),
   	 ( ...@ya.ru, username5 ),
   	 ...,
   	 ( ...@yahoo.com, usernameN ),
    ),(

   	 ( ...@gmail.com, username3 ),
   	 ( ...@rambler.ru, ... ),
   	 ( ...@ya.ru, ... ),
   	 ...,
    ),

    ...

    (
   	 ( ...@mail.ru, ... ),
   	 ( ...@ya.ru, ... ),
    ),
)