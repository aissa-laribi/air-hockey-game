from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '675') 
Config.set('graphics', 'resizable', '0')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import level1

class HockeyGameScreenManager(ScreenManager):
    pass

class GameSingle(Screen):
    pass


kv = Builder.load_file('single_menu.kv')


class HockeyApp(App):
    def build(self):
        return kv

if __name__=="__main__":
    HockeyApp().run()