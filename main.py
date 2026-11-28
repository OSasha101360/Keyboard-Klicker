from kivy.config import Config

# Устанавливаем компактный портретный размер окна до импорта Window
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', '1')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager


class MenuScreen(Screen):
    def go_to_game(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'game'

    def go_to_settings(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'settings'


class SettingsScreen(Screen):
    volume = NumericProperty(50)

    def go_to_menu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

    def go_to_game(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'game'


class GameScreen(Screen):
    clicks = NumericProperty(0)

    def register_click(self):
        self.clicks += 1

    def reset_clicks(self):
        self.clicks = 0

    def go_to_menu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

    def go_to_settings(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'settings'


class ClickerApp(App):
    def build(self):
        Builder.load_file('clicker.kv')
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if __name__ == '__main__':
    ClickerApp().run()