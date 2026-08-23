from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CounterApp(App):
    def build(self):
        self.count = 0
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text="Count: 0", font_size=40)
        layout.add_widget(self.label)

        button = Button(text="Tap Me", font_size=30)
        button.bind(on_press=self.increment)
        layout.add_widget(button)

        return layout

    def increment(self, instance):
        self.count += 1
        self.label.text = f"Count: {self.count}"

if __name__ == '__main__':
    CounterApp().run()