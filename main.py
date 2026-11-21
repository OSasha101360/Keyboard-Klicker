from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition


class MenuScreen(Screen):
    def go_to_game(self):
        self.manager.transition = SlideTransition(direction='left', duration=0.35)
        self.manager.current = 'game'


class GameScreen(Screen):
    clicks = NumericProperty(0)

    def register_click(self):
        self.clicks += 1

    def go_to_menu(self):
        self.manager.transition = SlideTransition(direction='right', duration=0.35)
        self.manager.current = 'menu'


class ClickerApp(App):
    def build(self):
        Builder.load_file('clicker.kv')
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm


if __name__ == '__main__':
    ClickerApp().run()