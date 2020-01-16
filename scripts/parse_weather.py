import sys
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from chrome_manager import manage_webdriver

class WeatherParser:

    def __init__(self):
        pass

    def _parse_soup(self):
        """
        Метод для считывания наполнения страницы
        :return: "Суп", содержащий наполнение страницы
        """
        manage_webdriver()

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        driver = webdriver.Chrome(options=options)
        driver.get(self.url)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        driver.close()

        return soup

    def _get_closest_weekday_idx(self):
        """
        :return: Порядковый номер ближайшего нужного дня недели
        """
        weekday_idxs = list()

        for day_number in range(1, 11):

            current_day_data = self.soup.find('li', attrs={'data-aop': f"day{day_number}"}).find('a')
            current_day_label = current_day_data.attrs['aria-label']

            if re.search(f"^Прогноз на {self.weekday}", current_day_label) is not None:

                weekday_idxs.append(day_number)

        weekday_idx = weekday_idxs[0]

        return weekday_idx

    def get_weather(self, url, weekday):
        """
        :param url: URL страницы с прогнозом погоды
        :param weekday: День недели, на который требуется узнать прогноз погоды
        :return: Массив из почасовых значений температуры
        """
        assert weekday in ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

        self.weekday = weekday
        self.url = url

        soup = self._parse_soup()
        self.soup = soup

        weekday_idx = self._get_closest_weekday_idx()

        hourly_weather_data = self.soup.find('li', attrs={'data-aop': f"day{weekday_idx}"}).find('a').attrs['data-hourly']
        start_index = hourly_weather_data.find('temperatures') + 15
        end_index = hourly_weather_data.find('times') - 3

        temperature_values = hourly_weather_data[start_index:end_index].split(',')
        temperature_values = [int(temperature_value) for temperature_value in temperature_values]

        return temperature_values