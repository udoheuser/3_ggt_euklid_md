# https://github.com/attreyabhatt/KivyMD-Basics/tree/master/6%20-%20Binding%20Input%20and%20button
# derived from author: Attreya Bhatt
# see also: https://youtu.be/VqLpDaTRGLo

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

import helpers
from bizLogic import BizLogic


class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        self.theme_cls.secondary_palette = "Grey"

        # screen = Screen()
        screen = Builder.load_string(helpers.navigation_bar)

        self.label_title = Builder.load_string(helpers.title_label)
        self.first_number = Builder.load_string(helpers.input_first_number)
        self.second_number = Builder.load_string(helpers.input_second_number)
        self.label_results = Builder.load_string(helpers.result_label)
        # button_run = Builder.load_string(helpers.button_calculate)
        button_run = MDRectangleFlatButton(text='Show',
                                       pos_hint={'center_x': 0.5, 'center_y': 0.6},
                                       on_release=self.show_data)
        

        screen.add_widget(self.label_title)
        screen.add_widget(self.first_number)
        screen.add_widget(self.second_number)
        screen.add_widget(button_run)
        screen.add_widget(self.label_results)
        return screen

    def show_data(self,obj):
        print("DEBUG INFO: Inputs:\n", self.first_number.text, "\n", self.second_number.text)
        try:
            self.label_results.theme_text_color = "Primary"
            self.label_results.text = "Ergebnis: "
            self.label_results.text += BizLogic.euklid(self.first_number.text, self.second_number.text)
            print("DEBUG INFO: Results\n", self.label_results.text)
        except:
            self.do_clear()
            self.label_results.theme_text_color = "Error"
            self.label_results.text = "Error. Please use integer values only"

    # Clear input values
    def do_clear(self):
        self.first_number.text = "0"
        self.second_number.text = "0"
        self.label_results.text = ""
        # self.label_debug.text = ""

DemoApp().run()
