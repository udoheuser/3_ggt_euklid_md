from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:
    padding: "10dp"

    MDTextField:
        id: text_input_1
        hint_text: "Erste Zahl (press 'Enter')"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        pos_hint: {"center_y": .8}

    MDTextField:
        id: text_input_2
        hint_text: "Zweite Zahl (press 'Enter')"
        helper_text: "There will always be a mistake"
        helper_text_mode: "on_error"
        pos_hint: {"center_y": .8}

    MDLabel:
        text: "(Ergebnis)"

    MDRaisedButton:
        text: "RUN"
        md_bg_color: 0, 0, 1, 1
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)

    def build(self):
        self.screen.ids.text_input_1.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message,
        )
        self.screen.ids.text_input_2.bind(
            on_text_validate=self.set_error_message,
            on_focus=self.set_error_message
        )
        return self.screen

    def set_error_message(self, instance_textfield):
        self.screen.ids.text_input_1.error = True
        self.screen.ids.text_input_2.error = True


Test().run()