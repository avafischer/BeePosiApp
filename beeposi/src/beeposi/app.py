"""
My first application
"""
import toga
import time
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class BeePosi(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        name_label = toga.Label(
            'Your name: ',
            style=Pack(padding=(0, 5))
        )
        self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(name_label)
        name_box.add(self.name_input)

        button = toga.Button(
            'Say Hello!',
            on_press=self.say_hello,
            style=Pack(padding=5)
        )
        label2 = toga.Label("Welcome to Bee Posi!")
        button2 = toga.Button(
            "set 10 second timer",
            on_press=self.countdown, 
            style = Pack(padding=5)

        )


        main_box.add(label2)

        main_box.add(name_box)
        main_box.add(button)
        main_box.add(button2)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def say_hello(self, widget):
        self.main_window.info_dialog("Hi,", self.name_input.value)
    def countdown(self, widget):
        time.sleep(10)
        self.main_window.info_dialog("10 seconds have passed", self.name_input.value)
def main():
    return BeePosi()