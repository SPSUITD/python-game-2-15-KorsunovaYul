import arcade
import arcade.gui
from arcade import load_texture
from arcade.gui.widgets import UITexturePane

class Button(arcade.gui.UIBoxLayout):
    def __init__(self):
        red_style = {
            "font_name": ("Epilepsy Sans",),
            "font_size": 10,
            "font_color": (243, 212, 214),
            "border_width": 4,
            "border_color": None,
            "bg_color": (252, 65, 74),

            # used if button is pressed
            "bg_color_pressed": (243, 212, 214),
            "border_color_pressed": None,  # also used when hovered
            "font_color_pressed": (252, 65, 74),
        }

        start_button = arcade.gui.UIFlatButton(text="НАЧАТЬ ИГРУ", width=400, height=100, style=red_style)
        x = [start_button]


        super().__init__(children=x)

    def on_click(self):
        print("Button clicked!")


class MyView(arcade.View):
    def __init__(self):
        super().__init__()
        self.dialog = Dialog(self)

    def on_draw(self):
        arcade.start_render()
        self.dialog.render()

class Dialog(arcade.gui.UIBoxLayout):
    def __init__(self, window):
        self.window = window
        bg_tex = load_texture("1/label.png")

        red_style = {
            "font_name": ("Epilepsy Sans",),
            "font_size": 25,
            "font_color": (243, 212, 214),
            "border_width": 4,
            "border_color": None,
            "bg_color": (252, 65, 74),

            # used if button is pressed
            "bg_color_pressed": (243, 212, 214),
            "border_color_pressed": None,  # also used when hovered
            "font_color_pressed": (252, 65, 74),
        }

        dalee_button = arcade.gui.UIFlatButton(text="ДАЛЕЕ", width=120, height=50, style=red_style)

        self.ui_back_label = arcade.gui.UITextArea(
            text="Птички ветер, проверка кода лалалл лалалалал аллалалал алалалллл лллаллалал",
            width=700,
            height=200,
            font_size=20,
            font_name="Epilepsy Sans",
            text_color=(0, 44, 60)
        ).with_space_around(30, 30, 30, 30)

        @dalee_button.event("on_click")
        def on_click_dalee_button(event):
            # Изменяем текст в существующем объекте UITextArea
            self.ui_back_label.text = "Новый текст после нажатия на кнопку"
            # После изменения текста вызываем перерисовку окна
            self.window.dispatch_event('on_draw')

        v_box = [UITexturePane(self.ui_back_label.with_space_around(right=20), tex=bg_tex), dalee_button.with_space_around(top=-50)]
        super().__init__(children=v_box)

