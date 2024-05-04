import arcade
import arcade.gui
from arcade.gui import UIOnClickEvent
from arcade import load_texture
from arcade.gui.widgets import UITexturePane
import csv


class Open_Dialog(arcade.gui.UIFlatButton):
    def __init__(self):
        super().__init__(x=340, y=200, width=200, height=100)
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

        self._text = "Диалог"
        self._style = red_style



class Dialog(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__()

        text = []
        with open('1/Dialog1.1.csv', encoding="UTF-8") as f:
            rdr = csv.reader(f, delimiter=";")
            c = 0
            for k in rdr:
                if c > 0:
                    text.append([k[0], k[1]])
                c += 1
        c = c-1

        bg_tex = load_texture("1/label.png")
        self.d = 0

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
        @dalee_button.event("on_click")
        def on_click_dalee_button(event):
            self.d += 1
            print(self.d, "тык")
            # Изменяем текст в текстовом поле при нажатии на кнопку
            if self.d < c:
                self.ui_back_label = arcade.gui.UITextArea(
                    text=f'{text[self.d][0]}\n\n{text[self.d][1]}',
                    width=700,
                    height=200,
                    font_size=20,
                    font_name="Epilepsy Sans",
                    text_color=(0, 44, 60)
                ).with_space_around(30, 30, 30, 30)
                self.children.clear()
                self.children.append(UITexturePane(self.ui_back_label.with_space_around(right=20), tex=bg_tex))
                self.children.append(dalee_button.with_space_around(top=-50))
            elif self.d == c:
                self.children.clear()


        if self.d == 0:
            self.ui_back_label = arcade.gui.UITextArea(
                text=f'{text[self.d][0]}\n\n{text[self.d][1]}',
                width=700,
                height=200,
                font_size=20,
                font_name="Epilepsy Sans",
                text_color=(0, 44, 60)
            ).with_space_around(30, 30, 30, 30)

            v_box = [UITexturePane(self.ui_back_label.with_space_around(right=20), tex=bg_tex),
                     dalee_button.with_space_around(top=-50)]
            self.children = v_box

class Vibor(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__()
        self.children = []

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

        self.vibor1_button = arcade.gui.UIFlatButton(text="Уйти из кафе по настоятельному совету деда", width=500, height=150, style=red_style)
        self.vibor2_button = arcade.gui.UIFlatButton(text="Остаться и выяснить у других посетителей кафе причину, почему дед так говорит", width=500, height=150, style=red_style)

        self.children = [self.vibor1_button.with_space_around(bottom=20), self.vibor2_button.with_space_around(bottom=20)]

class final_dialog(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__()
        text = []
        with open('1/Dialog1.2.csv', encoding="UTF-8") as f:
            rdr = csv.reader(f, delimiter=";")
            c = 0
            for k in rdr:
                if c > 0:
                    text.append([k[0], k[1]])
                c += 1
        c = c-1

        bg_tex = load_texture("1/label.png")
        self.d = 0

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
        @dalee_button.event("on_click")
        def on_click_dalee_button(event):
            self.d += 1
            print(self.d, "тык")
            # Изменяем текст в текстовом поле при нажатии на кнопку
            if self.d < c:
                self.ui_back_label = arcade.gui.UITextArea(
                    text=f'{text[self.d][0]}\n\n{text[self.d][1]}',
                    width=700,
                    height=200,
                    font_size=20,
                    font_name="Epilepsy Sans",
                    text_color=(0, 44, 60)
                ).with_space_around(30, 30, 30, 30)
                self.children.clear()
                self.children.append(UITexturePane(self.ui_back_label.with_space_around(right=20), tex=bg_tex))
                self.children.append(dalee_button.with_space_around(top=-50))
            elif self.d == c:
                self.children.clear()

        if self.d == 0:
            self.ui_back_label = arcade.gui.UITextArea(
                text=f'{text[self.d][0]}\n\n{text[self.d][1]}',
                width=700,
                height=200,
                font_size=20,
                font_name="Epilepsy Sans",
                text_color=(0, 44, 60)
            ).with_space_around(30, 30, 30, 30)

            v_box = [UITexturePane(self.ui_back_label.with_space_around(right=20), tex=bg_tex),
                     dalee_button.with_space_around(top=-50)]
            self.children = v_box