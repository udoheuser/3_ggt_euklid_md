title_label = """
MDLabel:
    text: "GGT-Berechnung"
    font_style: "H4"
    pos_hint:{'center_x': 0.5, 'center_y': 0.9}
    size_hint_x: None
    width:300
"""

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

result_label = """
MDLabel:
    text: "(Ergebnis)"
    font_style: "H6"
    pos_hint:{'center_x': 0.6, 'center_y': 0.5}
    size_hint_x: None
    width:300
"""

# https://github.com/attreyabhatt/KivyMD-Basics/tree/master/11%20-%20Navigation%20Drawer
navigation_bar = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: "Navigation"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]
                    Widget:
        MDNavigationDrawer:
            id: nav_drawer
"""