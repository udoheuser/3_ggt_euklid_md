from kivy.lang import Builder

from kivymd.app import MDApp

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

    MDLabel:
        text: "(Ergebnis)"
        pos_hint: {"center_y": .2}
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.screen.ids.text_input_1.bind(
            on_text_validate=self.set_error_message
            # on_focus=self.on_text,
            # on_text=self.screen.ids.text_input_1.text
        )
        self.screen.ids.text_input_2.bind(
            on_text_validate=self.set_error_message
            # on_focus=self.on_text
            # on_text=self.screen.ids.text_input_2.text
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_input_1.error = True
        self.screen.ids.text_input_2.error = True

    def on_text(instance, value):
        print('The widget', instance, 'have:', value)
        try:
            self.label_results.text = BizLogic.euklid(self.text_input1.text, self.text_input2.text)
        except:
            print("Abortion.")

Test().run()