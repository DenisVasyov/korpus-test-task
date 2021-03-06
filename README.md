# korpus-test-task

---

Репозиторий содержит реализацию тестового задания для курса по машинному обучению от KORPUS. Задание доступно по [ссылке](https://docs.google.com/document/d/1Z1t9ZUCrv8MDDbh4StbOJDmPIbS6S9PXi3K2OydFcEM/edit).

#### Требования:

-----

Программа разработана на `Python 3.8.0`. Все необходимые библиотеки можно установить следующим образом: `pip install -r requirements.txt`.

#### Описание репозитория:

* `chrome_manager.py` предназначен для управления `selenium` веб-драйвером;
* `parse_weather.py` содержит метод `get_weather` класса `WeatherParser`, предназначенный для парсинга массива значений температуры за нужные сутки;
* `ssl_handler.py` предназначен для устранения возможных проблем с SSL сертификатом (с большой вероятностью вам он без надобности);
* `recommend.py` предназначен непосредственно для запуска программы и содержит методы для принятия решения на основании среднечасовой температуры за выбранные сутки.

#### Справка по работе:

-----

* Запустите `python -m recommend --help` для получения справки;
* Для вывода результата запустите `python -m recommend` с аргументом `--weekday` для выбора дня недели, в который проходят соревнования. Значение `--weekday` по умолчанию: Вс.
