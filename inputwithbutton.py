# https://github.com/attreyabhatt/KivyMD-Basics/tree/master/6%20-%20Binding%20Input%20and%20button
# derived from author: Attreya Bhatt
# see also: https://youtu.be/VqLpDaTRGLo

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
import helpers


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        screen = Screen()

        # self.title = MDLabel(text='GGT-Berechnung')
        self.first_number = Builder.load_string(helpers.input_first_number)
        self.second_number = Builder.load_string(helpers.input_second_number)
        # self.button = Builder.load_string(helpers.button_calculate)
        button = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                       on_release=self.show_data)
        

        # screen.add_widget(self.title)
        screen.add_widget(self.first_number)
        screen.add_widget(self.second_number)
        screen.add_widget(button)
        return screen

    def show_data(self,obj):
        print(self.first_number.text)
        print(self.second_number.text)


DemoApp().run()
