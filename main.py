from kivy.app import App
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, DictProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from navigation_screen_manager import NavigationScreenManager

from requests import get as requests_get
from json import loads as json_loads

class MyScreenManager(NavigationScreenManager):
    pass

class EcoEngageApp(App):
    manager = ObjectProperty(None)
    gov_schemes_image_src = StringProperty('')
    quiz_score = NumericProperty(0)

    #variables for aqi value:
    aqi_json = DictProperty()
    aqi_level = StringProperty('')
    station = NumericProperty(0)
    station_name = StringProperty('') # AND TIME RECORDED
    dominentpol = StringProperty('')
    aqi_co = StringProperty('')
    aqi_no2 = StringProperty('')
    aqi_o3 = StringProperty('')
    aqi_pm10 = StringProperty('')
    aqi_pm25 = StringProperty('')
    aqi_so2 = StringProperty('')
    aqi_display_text = StringProperty('')

    def get_default_aqi_info(self):
        try:
            url = 'https://api.waqi.info/feed/here/?token=29ef5d4f5756505e8ed43acb19607c2a8702d0a2'
            response = requests_get(url)
            self.aqi_json = json_loads(response.text)
            if self.aqi_json['status'] == 'ok':

                try:
                    self.aqi_level = str(self.aqi_json['data']['aqi'])
                except:
                        self.aqi_level = '-'
                try:
                        self.station_name = self.aqi_json['data']['city']['name']+'\nTime Recorded: '+self.aqi_json['data']['time']['s']
                except:
                        self.station_name = '-'
                try:
                        self.dominentpol = self.aqi_json['data']['dominentpol']
                except:
                        self.dominentpol = '-'
                try:
                        self.aqi_co = str(self.aqi_json['data']['iaqi']['co']['v'])
                except:
                        self.aqi_co = '-'
                try:
                        self.aqi_no2 = str(self.aqi_json['data']['iaqi']['no2']['v'])
                except:
                        self.aqi_no2 = '-'
                try:
                        self.aqi_o3 = str(self.aqi_json['data']['iaqi']['o3']['v'])
                except:
                        self.aqi_o3 = '-'
                try:
                        self.aqi_pm10 = str(self.aqi_json['data']['iaqi']['pm10']['v'])
                except:
                        self.aqi_pm10 = '-'
                try:
                        self.aqi_pm25 = str(self.aqi_json['data']['iaqi']['pm25']['v'])
                except:
                        self.aqi_pm25 = '-'
                try:
                        self.aqi_so2 = str(self.aqi_json['data']['iaqi']['so2']['v'])
                except:
                        self.aqi_so2 = '-'
                self.aqi_display_text = '[size=30sp]AQI LEVEL = [b]{aqi}[/b][/size]\n[size=20sp]Dominant Pollutant: {dom}\nCO =        {co}\nNO2 =      {no2}\nPM 10 =   {pm10}\nPM 2.5 =  {pm25}\nSO2 =       {so2}[/size]'.format(aqi=self.aqi_level, dom = self.dominentpol, co = self.aqi_co, no2 =self.aqi_no2, pm10 = self.aqi_pm10, pm25 = self.aqi_pm25, so2 = self.aqi_so2)
            else:
                self.aqi_level = 'Some Error Occured, Try Later'

        except:
            self.aqi_level = 'No Internet Connection!'

    def get_aqi_info(self):
        try:
            url = 'https://api.waqi.info/feed/@{station}/?token=29ef5d4f5756505e8ed43acb19607c2a8702d0a2'.format(station = str(self.station))
            response = requests_get(url)
            self.aqi_json = json_loads(response.text)
            if self.aqi_json['status'] == 'ok':
                try:
                    self.aqi_level = str(self.aqi_json['data']['aqi'])
                except:
                        self.aqi_level = '-'
                try:
                        self.station_name = self.aqi_json['data']['city']['name']+'\nTime Recorded: '+self.aqi_json['data']['time']['s']
                except:
                        self.station_name = '-'
                try:
                        self.dominentpol = self.aqi_json['data']['dominentpol']
                except:
                        self.dominentpol = '-'
                try:
                        self.aqi_co = str(self.aqi_json['data']['iaqi']['co']['v'])
                except:
                        self.aqi_co = '-'
                try:
                        self.aqi_no2 = str(self.aqi_json['data']['iaqi']['no2']['v'])
                except:
                        self.aqi_no2 = '-'
                try:
                        self.aqi_o3 = str(self.aqi_json['data']['iaqi']['o3']['v'])
                except:
                        self.aqi_o3 = '-'
                try:
                        self.aqi_pm10 = str(self.aqi_json['data']['iaqi']['pm10']['v'])
                except:
                        self.aqi_pm10 = '-'
                try:
                        self.aqi_pm25 = str(self.aqi_json['data']['iaqi']['pm25']['v'])
                except:
                        self.aqi_pm25 = '-'
                try:
                        self.aqi_so2 = str(self.aqi_json['data']['iaqi']['so2']['v'])
                except:
                        self.aqi_so2 = '-'
                self.aqi_display_text = '[size=30sp]AQI LEVEL = [b]{aqi}[/b][/size]\n[size=20sp]Dominant Pollutant: {dom}\nCO =        {co}\nNO2 =      {no2}\nPM 10 =   {pm10}\nPM 2.5 =  {pm25}\nSO2 =       {so2}[/size]'.format(aqi=self.aqi_level, dom = self.dominentpol, co = self.aqi_co, no2 =self.aqi_no2, pm10 = self.aqi_pm10, pm25 = self.aqi_pm25, so2 = self.aqi_so2)
            else:
                self.aqi_level = 'Some Error Occured, Try again'

        except:
            self.aqi_level = 'No Internet Connection. Try again'

    def build(self):
        self.manager = MyScreenManager()
        return self.manager

EcoEngageApp().run()
#cd /mnt/c/users/asilk/Python_VSCODE/ENIR_PROJECT/versions/buildozer_test