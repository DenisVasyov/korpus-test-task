import click
import numpy as np
from parse_weather import WeatherParser

def decision_handler(mean_temperature):
    """
    :param mean_temperature: Среднее значение температуры
    :return: Требуемый тип смазки
    """
    if mean_temperature <= -13:

        lube = 'Type C'

    elif -13 < mean_temperature <= -5:

        lube = 'Type B'

    elif mean_temperature > -5:

        lube = 'Type A'

    return lube

@click.command()
@click.option('--weekday',
              default='Вс',
              show_default=True,
              help='Введите день недели, в который проходят соревнования, в формате [Пн, Вт, Ср, Чт, Пт, Сб, Вс]')

def decide(weekday='Вс'):

    url = 'https://www.msn.com/ru-ru/weather/today/%D1%87%D0%B5%D0%BB%D1%8F%D0%B1%D0%B8%D0%BD%D1%81%D0%BA%D1%83%D1%80%D0%B0%D0%BB%D1%8C%D1%81%D0%BA%D0%B8%D0%B9-%D1%84%D0%B5%D0%B4%D0%B5%D1%80%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BE%D0%BA%D1%80%D1%83%D0%B3%D1%80%D0%BE%D1%81%D1%81%D0%B8%D1%8F/we-city?iso=RU&el=D3uqMyT47PcvwAzNzc1XRw%3D%3D&lat=55.180&long=61.350'
    parser = WeatherParser()
    temperature_values = parser.get_weather(url, weekday)

    mean_temperature = np.mean(temperature_values)

    lube_type = decision_handler(mean_temperature)

    print(f'\nСреднечасовая температура в {weekday} составляет {round(mean_temperature, 2)} C°. Следовательно, необходимо выбрать смазку {lube_type}.\n\nИспользованные погодные данные доступны по ссылке:\n{url}')

if __name__ == '__main__':

    decide()