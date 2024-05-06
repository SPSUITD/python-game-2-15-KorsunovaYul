import arcade
import arcade.gui
from dialog_2 import final_dialog
import csv

class final_2(arcade.View):
    def __init__(self):
        super().__init__()

        print('записана 2')
    def setup(self):
        self.zapis()
        self.fon_sprite = None
        self.scene = arcade.Scene()
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()

        self.v_box = final_dialog()

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="bottom",
                child=self.v_box)
        )
        self.scene = arcade.Scene()
        self.fon_sprite = arcade.Sprite("1/kon2.png", 0.82)
        self.fon_sprite.center_x = 750
        self.fon_sprite.center_y = 435

        self.scene.add_sprite("Fon", self.fon_sprite)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.manager.draw()

    def on_update(self, delta_time: float):
        print(self.v_box.children)
        if self.v_box.children == []:
            self.clear()
            self.window.views['loading_views'].setup()
            self.window.show_view(self.window.views['loading_views'])

    def zapis(self):
        with open("konzovki/zapis.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["2"])


