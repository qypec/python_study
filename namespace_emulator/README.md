# Namespace emulator

Реализуйте программу, которая будет эмулировать работу с пространствами имен. Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:
* `create <namespace> <parent>` –  создать новое пространство имен с именем `<namespace>` внутри пространства `<parent>`
* `add <namespace> <var>` – добавить в пространство `<namespace>` переменную `<var>`
* `get <namespace> <var>` – получить имя пространства, из которого будет взята переменная `<var>` при запросе из пространства `<namespace>`, или `None`, если такого пространства не существует

#### Формат входных данных:

В первой строке дано число __n (1 ≤ n ≤ 100)__ – число запросов.
В каждой из следующих n строк дано по одному запросу.
Запросы выполняются в порядке, в котором они даны во входных данных.
Имена пространства имен и имена переменных представляют из себя строки длины не более __10__, состоящие из строчных латинских букв.

#### Формат выходных данных:

Для каждого запроса __get__ выведите в отдельной строке его результат.

#### Пример:
##### Sample Input:
```
9
add global a
create foo global
add foo b
get foo a
get foo c
create bar foo
add bar a
get bar a
get bar b
```
##### Sample Output:
```
global
None
bar
foo
```