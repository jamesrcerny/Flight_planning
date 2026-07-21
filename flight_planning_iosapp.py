"""Flight planning app."""
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class Demo1(MDScreen):
    pass

class Demo2(MDScreen):
    pass

class Main(MDApp):
    def build(self):
        Builder.load_file('flight_planning_iosapp.kv')
        sm = ScreenManager()

        sm.add_widget(Demo1(name = 'demo1'))
        sm.add_widget(Demo2(name = 'demo2'))

        return sm

Main().run()
