# OTUS
Python QA Engineer 2022

<details>
<summary>homework1 - Автоматизация тестирования: введение.</summary>

**Домашнее задание:** Настраиваем окружение

**Цель:** Прислать свой первый Pull Request в рамках курса

**Описание/Пошаговая инструкция выполнения домашнего задания:**
- Зарегистрироваться на гитхабе
- Создать репо
- Создать веточку
- Залить в ветку первый код с выводом "hello, world"
- Сделать pull request
- Прислать pull request
   
**Критерии оценки:**
- PR прислан
- Есть README.md
- Есть .gitignore
- Нет лишних файлов
</details>

<details>
<summary>homework2 - Погружение в Python. ООП</summary>

**Домашнее задание:** ООП и Pytest на практике

**Цель:** Научиться писать код в ООП стиле и покрывать его тестами.

**Описание/Пошаговая инструкция выполнения домашнего задания:**
- Создать базовый класс геометрической фигуры (Figure). 
- Реализовать классы геометрических фигур Треугольник, Прямоугольник, Квадрат, Круг (Triangle, Rectangle, Square, Circle).

Каждый класс должен располагаться в отдельном файле с соответствующим названием (например class Triangle => Triangle.py).
Все файлы с классами должны находиться в папке src/ в корне репозитория.
Треугольник должен задаваться тремя сторонами, если треугольник создать нельзя то класс должен вернуть None

1 Часть.

Каждая фигура должна иметь атрибуты:
name - название фигуры,
area (вычисляемое!) - площадь, 
perimeter (вычисляемое!) - периметр (сумма длин сторон или длину окружности)

Все вычисляемые свойства должны вычисляться по формулам для соответствующих геометрических фигур (никакого хардкода значений).
Каждая фигура должна реализовать метод add_area(figure) который должен принимать другую геометрическую фигуру и возвращать сумму площадей этих фигур. 
Если передана не геометрическая фигура, то нужно выбрасывать ошибку (raise ValueError) и сообщать что передан неправильный класс.

Опционально (необязательно): 
Запретить создавать экземпляры базового класса Figure.

Пример работы с одним из классов фигуры:

square = Square(10) # Так создаем квадрат со стороной 10
square.area
100
triangle = Triangle(13, 14, 15) # Так создаем треугольник со сторонами 13, 14, 15
triangle.area
84
triangle.add_area(square)
184

2 Часть.
Написать тесты с использованием pytest на эти классы. 
Глубину покрытия и объем определить самостоятельно, но минимум проверить реализацию всех указанных требований для каждого класса.

Все тесты должны располагаться в папке tests/ в корне репозитория.

**Критерии оценки:**
- Будет оцениваться глубина использования парадигмы ООП.
- Встроенные декораторы, наследование, отсутствие дублирования кода.
- Если какой-то метод выполняет одно и тоже во всех классах наследниках, то он должен принадлежать родительскому классу.
- Задание сдавать в формате pull-request.
- Соблюдение минимального кодстайла.
- Никаих print'ов, закомментированного кода и лишних файлов быть не должно.
</details>

<details>
<summary>homework3 - Работа с тестовыми данными</summary>

**Домашнее задание:** Работа с тестовыми данными

**Цель:** Научиться работать с различными типами файлов.

**Описание/Пошаговая инструкция выполнения домашнего задания:**
Работа с тестовыми данными

Скачать файлы: https://github.com/konflic/front_example/blob/master/data/books.csv и https://github.com/konflic/front_example/blob/master/data/users.json.
Написать скрипт, который из двух данных файлов будет читать данные и на их основании создаст result.json файл со структурой: https://github.com/konflic/front_example/blob/master/data/reference.json.
Идея в том что нужно раздать все книги из csv файла пользователям из списка. Книги складываются в виде словарей в массив books у каждого пользователя.
Книг изначально больше чем пользователей, поэтому раздавать нужно по принципу "максимально поровну", т.е. если книг, например 10. а пользователей 3 то распределение будет таким - 4 3 3 (один получит оставшуюся книгу).
Итоговая структура должна соответствовать стандарту json и парситься соответствующей библиотекой.

**Критерии оценки:**
- Задание оформить отдельным pull-request'ом (https://www.youtube.com/watch?v=swWqJBFpaNY)
- В репозитории отсутствуют лишние файлы
- Соблюдается минимальный кодстайл (встроенный в PyCharm)
- В личном кабинете или репозитории приложен файл result.json с итоговым результатом.
- Исходные файлы копировать не нужно.
</details>

<details>
<summary>homework4 - DDT в тестировании API</summary>

**Домашнее задание:** Тестирование API

**Цель:** Поучиться тестировать API сервисов на основе их документации.

**Описание/Пошаговая инструкция выполнения домашнего задания:**
Тестирование каждого api оформить в отдельном тестовом модуле.

Тестирование REST сервиса 1
Написать минимум 5 тестов для REST API сервиса: https://dog.ceo/dog-api/.
Как минимум 2 из 5 должны использовать параметризацию.
Документация к API есть на сайте. 
Тесты должны успешно проходить.

Тестирование REST сервиса 2
Написать минимум 5 тестов для REST API сервиса: https://www.openbrewerydb.org/.
Как минимум 2 из 5 должны использовать параметризацию.
Документация к API есть на сайте.
Тесты должны успешно проходить.

Тестирование REST сервиса 3.
Написать минимум 5 тестов для REST API сервиса: https://jsonplaceholder.typicode.com/.
Как минимум 2 из 5 должны использовать параметризацию.
Документация к API есть на сайте. 
Тесты должны успешно проходить.

Реализуйте в отдельном модуле (файле) тестовую функцию которая будет принимать 2 параметра:
url - должно быть значение по умолчанию https://ya.ru
status_code - значение по умолчанию 200
Параметры должны быть реализованы через pytest.addoption.
Можно положить фикcтуру и тестовую функцию в один файл.
Основная задача чтобы ваш тест проверял по переданному урлу статус ответа тот который передали, 
т.е. по адресу https://ya.ru/sfhfhfhfhfhfhfhfh должен быть валидным ответ 404

пример запуска pytest test_module.py --url=https://mail.ru --status_code=200

**Критерии оценки:**
- Все перечисленные пункты сдавать одним pull-request'ом
- Для всех файлов соблюдается минимальный код сатйл (встроенный форматтер PyCharm'а)
- Под тесты каждого сервиса заведён отдельный файл
</details>

<details>
<summary>homework5 - Ожидания элементов</summary>

**Домашнее задание:** Написание простых автотестов и основы Selenium

**Цель:** Научиться настраивать окружение для Selenium тестов, написать тесты, настроить ожидания к проекту. Научиться писать простые selenium скрипты.

**Описание/Пошаговая инструкция выполнения домашнего задания:**
Часть 1

1.1. Написать фикстуру для запуска разных браузеров (firefox, chrome, opera, по желанию - safari, edge, yandex). 

1.2. Выбор браузера должен осуществляться путем передачи аргумента командной строки pytest. 

1.3. По завершению работы тестов должно осуществляться закрытие браузера.

1.4. Добавить опцию командной строки, которая указывает базовый URL opencart.

Часть 2

2.1 Написать тесты проверяющие элементарное наличие элементов на разных страницах приложения opencart

2.2 Реализовать минимум пять тестов (одни тест = одна страница приложения)

2.3 Использовать методы явного ожидания элементов

Покрыть нужно:

- Главную
- Каталог
- Карточку товара
- Страницу логина в админку /admin
- Страницу регистрации пользователя (/index.php?route=account/register)
- Какие именно элементы проверять определить самостоятельно, но не меньше 5 для каждой страницы

**Критерии оценки:**
- Весь написанный код оформлен в формате pull-request'a
- Соблюдается минимальный кодстай (встроенный форматтер PyCharm'a)
- Реализованы все проверки перечисленные в задании
- Отсутствуют лишние файлы и папки (.idea/, pycache, и т.д.)
</details>


6) homework6 - Паттерн PageObject
7) homework7 - Отчёты Allure
8) homework8 - Анализ логов веб-сервера
9) homework9 - Работа с сетью II (socket)
10) homework10 - Работа с ОС Linux с помощью Python 
11) homework11 - Оркестрация и взаимодействие контейнеров 
12) homework12 - Подготовка тестового окружения