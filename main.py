from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder




class HockeyGameScreenManager(ScreenManager):
    pass

kv= Builder.load_file("home.kv")

class HockeyGameApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    HockeyGameApp().run()
