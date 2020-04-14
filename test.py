from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.clock import Clock
from kivy.properties import StringProperty

from time import strftime

kv = """
<Home@Screen>:
    BoxLayout:
        orientation: 'vertical'
        MyClock:
            font_size: 50
            text: self.current_time
        Button:
            text: 'Set Alarm'
            on_release: app.root.ids.sm.current = 'alarm_page'
<AlarmPage@Screen>:
    Button:
        text: 'Put alarms on this page'
        on_release: app.root.ids.sm.current = 'home_page'

BoxLayout:
    ScreenManager:
        id: sm
        Home:
            name: 'home_page'
        AlarmPage:
            name: 'alarm_page'

"""


class MyClock(Button):
    current_time = StringProperty(strftime("%I:%M:%S %p"))

    def __init__(self, **kwargs):
        Clock.schedule_interval(self.update_time, 1)
        super().__init__(**kwargs)

    def update_time(self, dt):
        self.current_time = strftime("%I:%M:%S %p")


class MainApp(App):
    def build(self):
        return Builder.load_string(kv)


if __name__ == "__main__":
    MainApp().run()
