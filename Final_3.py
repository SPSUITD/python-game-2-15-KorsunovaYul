import arcade
import arcade.gui
from dialog_3 import final_dialog
import csv

class final_3(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.zapis()
        arcade.set_background_color((252, 65, 74))

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
    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()
    def on_draw(self):
        self.clear()
        self.manager.draw()
    def on_update(self, delta_time: float):
        print('buba')
        if self.v_box.children == []:
            self.clear()
            self.window.show_view(self.window.views['pervoe_okno'])
            self.window.views['pervoe_okno'].setup()

    def zapis(self):
        with open("konzovki/zapis.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["3"])


