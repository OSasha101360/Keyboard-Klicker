from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition


class MenuScreen(Screen):
    def go_to_game(self):
        # Настраиваем плавный переход влево длительностью 0.35 сек
        self.manager.transition = SlideTransition(direction='left', duration=0.35)
        self.manager.current = 'game'


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.clicks = 0

    def on_click_target(self):
        self.clicks += 1
        self.ids.game_label.text = f'Clicks: {self.clicks}'

    def go_to_menu(self):
        # При возврате меняем направление перехода вправо
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