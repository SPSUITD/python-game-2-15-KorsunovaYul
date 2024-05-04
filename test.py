import arcade
import arcade.gui
from arcade.gui import UIOnClickEvent
from arcade import load_texture
from arcade.gui.widgets import UITexturePane
import csv
class MyView(arcade.View):
    def __init__(self):
        super().__init__()
        self.dialog = None
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout
    def setup(self):
        self.v_box = Vibor1()
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="center",
                child=self.v_box)
        )
    def on_draw(self):
        self.clear()
        self.manager.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()

class Vibor1(arcade.gui.UIBoxLayout):
    def __init__(self):
        super().__init__()
        self.children = []

        red_style = {
            "font_name": ("Epilepsy Sans",),
            "font_size": 20,
            "font_color": (243, 212, 214),
            "border_width": 4,
            "border_color": None,
            "bg_color": (252, 65, 74),

            # used if button is pressed
            "bg_color_pressed": (243, 212, 214),
            "border_color_pressed": None,  # also used when hovered
            "font_color_pressed": (252, 65, 74),
        }

        vibor1_button = arcade.gui.UIFlatButton(text="Уйти из кафе по настоятельному совету деда", width=400, height=100, style=red_style)
        vibor2_button = arcade.gui.UIFlatButton(text="Остаться и выяснить у других посетителей кафе причину, почему дед так говорит", width=400, height=100, style=red_style)

        @vibor1_button.event("on_click")
        def on_click_vibor1_button(event):
            print("1тык")

        @vibor2_button.event("on_click")
        def on_click_vibor2_button(event):
            print("2тык")

        self.children = [vibor1_button.with_space_around(bottom=20), vibor2_button.with_space_around(bottom=20)]

def main():
    window = arcade.Window(fullscreen=True, title="В поисках Лили")
    window.total_score = 0
    menu_view = MyView()
    window.show_view(menu_view)
    menu_view.setup()
    arcade.run()

if __name__ == "__main__":
    main()

