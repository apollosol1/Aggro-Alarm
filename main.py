from time import strftime
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import os


kv = """
BoxLayout:
    orientation: 'vertical'
    MyClock:
        font_size: 50
        id:my_clock
    Button:       
        text: 'Set Alarm'
        on_press: aggro_alarm.screen_manger.current = "SetAlarmPage"
"""


class MyClock(Label):
    pass


class SetAlarmButton(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_alarm = Button(text="Set Alarm")
        # self.set_alarm.bind(on_press=)
        self.add_widget(Label())
        self.add_widget(self.set_alarm)


class MainApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.SetAlarmPage = SetAlarmPage()
        self.screen_manager = ScreenManager()
        self.home_screen = Builder.load_string(kv)

    def build(self):
        screen = Screen(name='Home')
        screen.add_widget(self.home_screen)
        self.screen_manager.add_widget(screen)

        screen = Screen(name="SetAlarmPage")
        screen.add_widget(self.SetAlarmPage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def on_start(self):
        t = strftime("%I:%M:%S %p")
        self.root.ids.my_clock.text = t
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, dt):
        t = strftime("%I:%M:%S %p")
        self.root.ids.my_clock.text = t


class SetAlarmPage(Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Alarm 1:"))
        self.A1 = TextInput(multiline=False)
        self.add_widget(self.A1)


if __name__ == "__main__":
    aggro_alarm = MainApp()
    aggro_alarm.run()
