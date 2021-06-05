import requests
from selectorlib import Extractor

class Temperature:

    def __init__(self, country, city):
        self.country = country.replace(" ", "-").lower()
        self.city = city.replace(" ", "-").lower()

    def get(self):
        try:
            r = requests.get(f"https://www.timeanddate.com/weather/{self.country}/{self.city}")
            c = r.text  # Source code of the file
            extractor = Extractor.from_yaml_file("temperature.yaml")
            raw_temp = float(extractor.extract(c)['temp'].replace("\xa0°C", ""))
            return raw_temp
        except ValueError:
            return "You have entered a wrong country"
