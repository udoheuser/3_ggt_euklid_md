input_first_number = """
MDTextField:
    hint_text: "Erste Zahl"
    helper_text: "integer only"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.4, 'center_y': 0.7}
    size_hint_x: None
    width:140
"""

input_second_number = """
MDTextField:
    hint_text: "Zweite Zahl"
    helper_text: "integer only"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.6, 'center_y': 0.7}
    size_hint_x: None
    width:140
"""

button_calculate = """
MDRectangleFlatButton:
    text='Run'
    pos_hint={'center_x': 0.5, 'center_y': 0.6}
    on_release=self.show_data
"""