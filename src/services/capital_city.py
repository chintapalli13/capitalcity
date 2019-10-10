from requests.compat import urljoin
import requests


class CountryCapitals(object):

    def __init__(self,country_code):
        self.__country_code = country_code

    def __find_capital_city(self):
        response = requests.get(self.__country_endpoint()+self.__country_code)
        if response.status_code == 200:
            return response.json()
        else:
            return {"message":"Not found"}

    def capital_city(self):
        response = self.__find_capital_city()
        resp = self.__process_response(response)
        if 'capital' in resp:
            return resp['capital']
        elif 'message' in resp:
            return resp['message']
        else:
            return None

    def __process_response(self, response):
        if isinstance(response, list):
            return response[0] if len(response)>0 else {"Not found"}
        else:
            return response

    def __country_endpoint(self):
        base_url = 'https://restcountries.eu/rest/v2/'
        if len(self.__country_code)>3:
            self.__country_code = self.__country_code+"?fullText=true"
            return urljoin(base_url, 'name/')
        else:
            return urljoin(base_url, 'alpha/')







