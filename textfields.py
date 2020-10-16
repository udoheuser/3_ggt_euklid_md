from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.behaviors import TouchBehavior
from kivymd.uix.button import MDRaisedButton

from bizLogic import BizLogic

KV = '''
BoxLayout:
    padding: "10dp"

    MDLabel:
        text: "GGT-Berechnung"
        pos_hint: {"center_y": .9}

    MDTextField:
        id: text_input_1
        hint_text: "Erste Zahl (press 'Enter')"
        helper_text: "integer values allowed only"
        helper_text_mode: "on_error"
        pos_hint: {"center_y": .8}

    MDTextField:
        id: text_input_2
        hint_text: "Zweite Zahl (press 'Enter')"
        helper_text: "integer values allowed only"
        helper_text_mode: "on_error"
        pos_hint: {"center_y": .8}

    MyButton:
        id: btn_result
        text: "Run"
        md_bg_color: 0, 0, 1, 1
        pos_hint: {"center_y": .2}
        on_press: root.do_action()

    MDLabel:
        id: label_results
        text: "(Ergebnis)"
        pos_hint: {"center_y": .2}
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.screen.ids.text_input_1.bind(
            on_text_validate=self.set_error_message,
            # on_focus=self.on_text
            # on_text=self.screen.ids.text_input_1.text
        )
        self.screen.ids.text_input_2.bind(
            on_text_validate=self.set_error_message,
            # on_focus=self.on_text
            # on_text=self.screen.ids.text_input_2.text
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_input_1.error = True
        self.screen.ids.text_input_2.error = True

    def do_action(self):
        # Ergebnisberechnung (lineare und rekursive Variante)
        try:
            self.label_results.text = BizLogic.euklid(self.text_input1.text, self.text_input2.text)
        except:
            pass
            # valid_input = False
            # Controller.do_clear(self)
            # self.label_debug.text = "WARNING: Wrong input values. Integer values and iterative version only!"


class MyButton(MDRaisedButton, TouchBehavior):
    # https://kivymd.readthedocs.io/en/latest/behaviors/touch/index.html
    def on_long_touch(self, *args):
        print("<on_long_touch> event")
        Test.screen.ids.label_results.text = "hello"
        # self.label_results.text = "hello"

    def on_double_tap(self, *args):
        print("<on_double_tap> event")
        Test.screen.ids.label_results.text = "hello"
        # self.label_results.text = "hello"

    def on_triple_tap(self, *args):
        print("<on_triple_tap> event")
        Test.screen.ids.label_results.text = "hello"
        # self.label_results.text = "hello"

Test().run()