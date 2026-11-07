from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager


# Главное меню
class MenuScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Вертикальный контейнер с отступами
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Надпись с названием игры
        title_label = Label(text='MY CLICKER', font_size='32sp')

        # Кнопка Play
        play_button = Button(text='Play', font_size='24sp')
        play_button.bind(on_press=self.go_to_game)

        # Добавляем виджеты в layout, а layout на экран
        layout.add_widget(title_label)
        layout.add_widget(play_button)
        self.add_widget(layout)

    def go_to_game(self, instance):
        # Переключаемся на экран с именем 'game'
        self.manager.current = 'game'


# Игровой экран
class GameScreen(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Надпись о начале игры
        game_label = Label(text='Game started!', font_size='28sp')

        # Кнопка Back
        back_button = Button(text='Back', font_size='24sp')
        back_button.bind(on_press=self.go_to_menu)

        layout.add_widget(game_label)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_to_menu(self, instance):
        # Возвращаемся на экран с именем 'menu'
        self.manager.current = 'menu'


# Основной класс приложения
class ClickerApp(App):

    def build(self):
        # Создаем менеджер экранов и добавляем в него оба экрана
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm


# Запуск приложения
if __name__ == '__main__':
    ClickerApp().run()
