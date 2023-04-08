from polls.models import HollidayModel
from polls.hollidays_api.libs.headers import headers
from datetime import datetime
from tqdm import tqdm
import requests

class Hollydays(object):

    def __init__(self):
        self.headers = headers
        self.time = datetime.now()
        self.params = {
            "key": "48320628-2dd6-4b22-96f8-04c025597d23",
            "country": str(),
            "year": "2022",
            "language": "pt"
        }
        self.__get_all_countrys()
        self.all_hollidays = list()

    def __get_all_countrys(self) -> None:
        self.response = requests.get(
            f'https://{self.headers["authority"]}/v1/countries?pretty',
            headers=self.headers,
            params=self.params
        )
        if self.response.status_code in range(200, 300):
            self.response = self.response.json()
            self.countries = self.response.get("countries", '-')
            if self.countries != "-":
                return
        raise TypeError("There's something wrong with the API connection")

    def send_requisition(self) -> None:
        self.response = requests.get(
            f'https://{self.headers["authority"]}/v1/holidays?pretty',
            headers=self.headers,
            params=self.params
        )
        if self.response.status_code in range(200, 300):
            self.response = self.response.json()

    def __separare_information_hollidays(self) -> None:
        if type(self.response) is dict:
            for holliday in self.response['holidays']:
                date = holliday.get('date', '-')
                if date != '-':
                    date = date.split('-')
                    dict_occurrence = {
                        'description': holliday.get('name', '-'),
                        'country': self.__country_name,
                        'day': int(date[-1]),
                        'month': int(date[1]),
                        'flag': self.flag if self.flag != '-' else ''
                    }
                    if dict_occurrence not in self.all_hollidays:
                        self.all_hollidays.append(dict_occurrence)

    def get_all_hollidays(self) -> None:
        for country in tqdm(self.countries):
            self.__country_code = country['code']
            self.__country_name = country['name']
            self.params['country'] = self.__country_code
            self.flag = country.get('flag', '-')
            self.send_requisition()
            self.__separare_information_hollidays()

    def check_database(self, country: str, month: int, day: int) -> bool:
        try:
            self.results = HollidayModel.objects.get(
                country=country,
                month=month,
                day=day
            )
            return True
        except HollidayModel.DoesNotExist:
            return False
    
    def database_insert_holliday(self) -> None:
        self.sended = 0
        for holliday in self.all_hollidays:
            if self.check_database(
                holliday["country"],
                holliday["month"],
                day=holliday["day"]
            ):
                continue
            self.post = HollidayModel(
                description=holliday["description"],
                country=holliday["country"],
                month=holliday["month"],
                day=holliday["day"],
                flag=holliday["flag"]
            )
            self.post.save()
            self.sended += 1
        print(f'Holidays sended: {self.sended}')
        print(f'Already in database: {len(self.all_hollidays) - self.sended}')
