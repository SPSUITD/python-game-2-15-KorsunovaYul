import arcade
import arcade.gui
import csv

class Konzovki(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.fon_sprite = None
        self.scene = arcade.Scene()

        self.scene = arcade.Scene()
        self.fon_sprite = arcade.Sprite("1/nach.png", 0.82)
        self.fon_sprite.center_x = 750
        self.fon_sprite.center_y = 435

        self.scene.add_sprite("Fon", self.fon_sprite)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.v_box.clear()

        self.red_style = {
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

        k1_button = arcade.gui.UIFlatButton(text="СЧАСТЛИВАЯ", width=400, height=100, style=self.red_style)
        self.v_box.add(k1_button.with_space_around(bottom=20, right=150))
        k1_button.on_click = self.on_click_k1

        k2_button = arcade.gui.UIFlatButton(text="ХОРОШАЯ", width=400, height=100, style=self.red_style)
        self.v_box.add(k2_button.with_space_around(bottom=20, right=150))
        k2_button.on_click = self.on_click_k2

        k3_button = arcade.gui.UIFlatButton(text="ПЛОХАЯ", width=400, height=100, style=self.red_style)
        self.v_box.add(k3_button.with_space_around(bottom=50, right=150))
        k3_button.on_click = self.on_click_k3

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="right",
                anchor_y="bottom",
                child=self.v_box)
        )

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ESCAPE:
            arcade.exit()

    def on_click_k1(self, event):
        if self.check_record_in_csv(["1"]):
            self.clear()
            self.window.show_view(self.window.views['final_1'])
            self.window.views['final_1'].setup()
            self.window.views['final_1'].on_update(delta_time=1/60)
            arcade.run()
        else:
            self.net_zapisi()

    def on_click_k2(self, event):
        if self.check_record_in_csv(["2"]):
            self.v_box.clear()
            self.window.show_view(self.window.views['final_2'])
            self.window.views['final_2'].setup()
            self.window.views['final_2'].on_update(delta_time=1/60)
            arcade.run()
        else:
            self.net_zapisi()


    def on_click_k3(self, event):
        if self.check_record_in_csv(["3"]):
            self.v_box.clear()
            self.window.show_view(self.window.views['final_3'])
            self.window.views['final_3'].setup()
            self.window.views['final_3'].on_update(delta_time=1/60)
            arcade.run()
        else:
            self.net_zapisi()

    def check_record_in_csv(self, record):
        with open('konzovki/zapis.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row == record:
                    return True
        return False

    def net_zapisi(self):
        self.v_box.clear()
        net_button = arcade.gui.UIFlatButton(text="ВЫ ЁЩЁ НЕ ПРОШЛИ ИГРУ НА ЭТУ КОНЦОВКУ", width=600, height=120, style=self.red_style)
        self.v_box.add(net_button)
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="center",
                child=self.v_box)
        )
        net_button.on_click = self.net_button_in_click
        arcade.run()

    def net_button_in_click(self, event):
        self.clear()
        self.window.show_view(self.window.views['pervoe_okno'])
        self.window.views['pervoe_okno'].setup()
        arcade.run()
    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.manager.draw()

