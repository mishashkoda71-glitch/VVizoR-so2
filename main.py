from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# Настройки окна (полный экран, чтобы поверх игры)
Window.fullscreen = 'auto'

class CheatMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # Заголовок
        self.add_widget(Label(text="VVizioR | Standoff 2", font_size='30sp', bold=True))

        # Поле для ввода ключа
        self.key_input = TextInput(
            hint_text="Введите ваш ключ доступа",
            multiline=False,
            size_hint=(1, 0.2),
            font_size='20sp'
        )
        self.add_widget(self.key_input)

        # Кнопка проверки
        self.check_btn = Button(
            text="Активировать чит",
            size_hint=(1, 0.2),
            font_size='24sp',
            background_color=(0.2, 0.6, 1, 1)
        )
        self.check_btn.bind(on_press=self.check_key)
        self.add_widget(self.check_btn)

        # Статус
        self.status = Label(text="Статус: Ожидание ключа", font_size='18sp')
        self.add_widget(self.status)

    def check_key(self, instance):
        user_key = self.key_input.text.strip()
        
        # ТУТ ПОКА ЗАГЛУШКА. Позже мы заменим это на запрос к твоему серверу/боту
        # Например, если ключ равен "VVZ-TEST" (для теста)
        if user_key == "VVZ-TEST":
            self.status.text = "Статус: ✅ Доступ разрешен! Инжект..."
            self.status.color = (0, 1, 0, 1)
            # Здесь будет вызов функции инжекта в игру
        else:
            self.status.text = "Статус: ❌ Неверный ключ или не оплачен!"
            self.status.color = (1, 0, 0, 1)

class VVizioRApp(App):
    def build(self):
        return CheatMenu()

if __name__ == "__main__":
    VVizioRApp().run()
