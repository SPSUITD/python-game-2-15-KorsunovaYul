import arcade
import arcade.gui
from Chast_1 import chast_1
from Chast_2 import chast_2

class Perv_okno(arcade.View):
    def __init__(self):
        super().__init__()
        self.fon_sprite = None
        self.scene = arcade.Scene()

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()

        red_style = {
            "font_name": ("Epilepsy Sans",),
            "font_size": 40,
            "font_color": (243, 212, 214),
            "border_width": 4,
            "border_color": None,
            "bg_color": (252, 65, 74),

            # used if button is pressed
            "bg_color_pressed": (243, 212, 214),
            "border_color_pressed": None,  # also used when hovered
            "font_color_pressed": (252, 65, 74),
        }

        start_button = arcade.gui.UIFlatButton(text="НАЧАТЬ ИГРУ",  width=400, height=100, style=red_style)
        self.v_box.add(start_button.with_space_around(bottom=20, right=150))
        start_button.on_click = self.on_click_start

        save_button = arcade.gui.UIFlatButton(text="КОНЦОВКИ",  width=400, height=100, style=red_style)
        self.v_box.add(save_button.with_space_around(bottom=20, right=150))

        quit_button = arcade.gui.UIFlatButton(text="ВЫХОД",  width=400, height=100, style=red_style)
        self.v_box.add(quit_button.with_space_around(bottom=50, right=150))
        quit_button.on_click = self.on_click_quit

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.v_box)
        )


    def setup(self):
        self.scene = arcade.Scene()
        self.fon_sprite = arcade.Sprite("1/nach.png", 0.82)
        self.fon_sprite.center_x = 750
        self.fon_sprite.center_y = 435

        self.scene.add_sprite("Fon", self.fon_sprite)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()
    def on_click_quit(self, event):
        arcade.exit()

    def on_click_start(self, event):
        game_view = chast_1()
        self.window.show_view(game_view)
        game_view.setup()
        arcade.run()

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.manager.draw()

