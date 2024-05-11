import arcade
from animazia import Ded
import math
import arcade.gui
from dialog_1 import Open_Dialog, Dialog, Vibor





class chast_1(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.CHARACTER_SCALING = 1
        self.TILE_SCALING = 1

        self.PLAYER_MOVEMENT_SPEED = 5
        self.GRAVITY = 0

        self.scene = None
        self.player_sprite = None
        self.player_sprite_list = None
        self.hitbox = None
        self.physics_engine = None
        self.camera = None
        self.gui_camera = None
        self.tile_map = None
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        self.background_color = (252, 65, 74, 0)
        self.vstrecha = 1
        self.dialog = 1

        self.camera = arcade.Camera()
        self.gui_camera = arcade.Camera()
        map_name = "1/fon.json"
        layer_options = {
            "stena": {
                "use_spatial_hash": True,
            },
            "mebel": {
                "use_spatial_hash": True,
            },
            "znaki": {
                "use_spatial_hash": True,
            },
            "graniza2": {
                "use_spatial_hash": True,
            },
            "graniza": {
                "use_spatial_hash": True,
            },
            "personagi": {
                "use_spatial_hash": True,
            },
        }
        self.tile_map = arcade.load_tilemap(map_name, self.TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        pole = arcade.Sprite("1/razgovornoe_pole.png", 1)
        pole.center_x = 250
        pole.center_y = 1020
        self.scene.add_sprite("Pole", pole)


        self.player_sprite = arcade.Sprite('1/ella/sidit.png', 1)
        self.player_sprite.center_x = 220
        self.player_sprite.center_y = 1170

        self.scene.add_sprite("Player", self.player_sprite)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        ded = self.tile_map.object_lists["Ded"]
        for my_object in ded:
            cartesian = self.tile_map.get_cartesian(
                my_object.shape[0], my_object.shape[1]
            )
            self.ded = Ded()
            self.ded.center_x = math.floor(
                (cartesian[0] + 0.5) * self.tile_map.tile_width
            )
            self.ded.center_y = math.floor(
                (cartesian[1] + 0.3) * (self.tile_map.tile_height * self.TILE_SCALING)
            )
            self.ded.boundary_top = 1150
            self.oborot = 0
            self.scene.add_sprite("Ded", self.ded)


        open_dialog_button = Open_Dialog()
        self.v_box.add(open_dialog_button)

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="bottom",
                child=self.v_box)
        )


    def on_draw(self):

        self.clear()
        self.camera.use()
        self.scene.draw()
        self.gui_camera.use()
        self.manager.draw()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.ESCAPE:
            if key == arcade.key.ESCAPE:
                arcade.exit()

        if key == arcade.key.E:
            Open_Dialog().on_click()


    def center_camera_to_player(self):

        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)

        if screen_center_x < 0:
            screen_center_x = 0

        if screen_center_y < 0:
            screen_center_y = 0

        player_centered = screen_center_x, screen_center_y

        self.camera.move_to(player_centered)

    def on_update(self, delta_time):
        self.clear()
        self.center_camera_to_player()
        self.scene.update_animation(
            delta_time,
            [
                "stena",
                "znaki",
                "mebel",
                "graniza",
                "graniza2"
            ],
        )

        self.player_collision_list = arcade.check_for_collision_with_lists(
            self.player_sprite,
            [
                self.scene["Pole"],
            ],
        )
        for collision in self.player_collision_list:
            if self.scene["Pole"] in collision.sprite_lists:
                if self.dialog == 1:
                    if self.vstrecha == 1:
                        self.v_box.clear()
                        self.v_box = Dialog()

                        self.manager.add(
                            arcade.gui.UIAnchorWidget(
                                anchor_x="center",
                                anchor_y='bottom',
                                child=self.v_box),
                        )
                        self.vstrecha = 0
                    if self.vstrecha == 0 and self.v_box.children == []:
                        self.dialog = 2
                elif self.dialog == 2:
                    self.ded.update()
                    if self.ded.top < self.ded.boundary_top and self.oborot == 0:
                        self.ded.change_y = 3
                    if self.ded.top > self.ded.boundary_top and self.oborot == 0:
                        self.oborot = 1
                    if self.oborot == 1:
                        self.ded.change_y = -3
                    if self.ded.center_y == 525:
                        self.dialog = 3
                elif self.dialog == 3:
                    if self.vstrecha == 0:
                        self.v_box.clear()
                        self.v_box = Vibor()
                        self.v_box.children[0].child.on_click = self.on_click_vibor1
                        self.v_box.children[1].child.on_click = self.on_click_vibor2
                        self.manager.add(
                            arcade.gui.UIAnchorWidget(
                                anchor_x="center",
                                anchor_y="center",
                                child=self.v_box)
                        )
                        self.vstrecha = 1

        if self.player_collision_list == []:
            self.vstrecha = 0
            self.v_box.clear()

    def on_click_vibor1(self, event):
        print('1 кнопка естттт')
        self.v_box.clear()
        self.clear()
        self.dialog = 0
        game_view = self.window.views['final_1']
        game_view.setup()
        self.window.show_view(game_view)

    def on_click_vibor2(self, event):
        print('2 кнопка естттт')
        self.v_box.clear()
        self.clear()
        self.dialog = 0
        game_view = self.window.views['chast_2']
        game_view.setup()
        self.window.show_view(game_view)


