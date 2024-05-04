import arcade
from animazia import Player, Ded
import math
import arcade.gui
from dialog_1 import Open_Dialog, Dialog
import os




class MyGame(arcade.View):
    def __init__(self):
        super().__init__()

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
        self.vstrecha = 0
        self.dialog = 0

    def setup(self):

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

        # я добавляю лишний спрайт для того, чтобы взять у него хитбокс и присвоить другому спрайту

        image_source = "1/hitbox.png"
        self.hitbox = arcade.Sprite(image_source, self.CHARACTER_SCALING)
        self.hitbox.center_x = 250
        self.hitbox.center_y = 1100

        self.player_sprite = Player()
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 1100
        self.player_sprite.hit_box = self.hitbox.hit_box

        self.scene.add_sprite("Player", self.player_sprite)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.walls = [self.scene["stena"], self.scene["znaki"], self.scene["mebel"], self.scene["graniza"], self.scene["graniza2"], self.scene["personagi"]]

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=self.GRAVITY, walls=self.walls
        )
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
            print(self.ded.center_y)
            self.ded.boundary_top = 1050
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

        # Draw our Scene
        self.scene.draw()

        self.gui_camera.use()
        self.manager.draw()


    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = self.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -self.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -self.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = self.PLAYER_MOVEMENT_SPEED

        if key == arcade.key.ESCAPE:
            if key == arcade.key.ESCAPE:
                arcade.exit()

        if key == arcade.key.E:
            Open_Dialog().on_click()

    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

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

        self.physics_engine.update()
        self.center_camera_to_player()
        self.player_sprite.update()
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
                if self.dialog == 0:
                    if self.vstrecha == 0:
                        self.v_box.clear()

                        open_dialog_button = Open_Dialog()
                        self.v_box.add(open_dialog_button)

                        self.manager.add(
                            arcade.gui.UIAnchorWidget(
                                anchor_x="center",
                                anchor_y="bottom",
                                child=self.v_box)
                        )
                        open_dialog_button.on_click = self.on_click_open
                        self.vstrecha = 1
                elif self.dialog == 1:
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


        if self.player_collision_list == []:
            self.vstrecha = 0
            self.v_box.clear()

        if self.dialog == 2:
            self.ded.update()
            if self.ded.top < self.ded.boundary_top and self.oborot == 0:
                self.ded.change_y = 3
            if self.ded.top > self.ded.boundary_top and self.oborot == 0:
                self.oborot = 1
            if self.oborot == 1:
                self.ded.change_y = -3
            if self.ded.change_y == 528:
                self.dialog = 3


#        if self.dialog == 3:


    def on_click_open(self, event):
        self.v_box.clear()
        self.dialog = 1
        print("кнопка нажата")






