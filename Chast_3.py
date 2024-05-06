import arcade
from animazia import Player, Ded
import math
import arcade.gui
from dialog_3 import Open_Dialog, Dialog, Open_Dver
import os



class chast_3(arcade.View):
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
        self.vstrecha = 0
        self.dialog = 0
        self.peremena_persongey = 0

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
            'lilii':{
                "use_spatial_hash": True,
            },
        }
        self.tile_map = arcade.load_tilemap(map_name, self.TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)
        self.scene["lilii"].clear()

        pole_amalia = arcade.Sprite("1/razgovornoe_pole.png", 1)
        pole_amalia.center_x = 80
        pole_amalia.center_y = 800
        self.scene.add_sprite("Pole_Amalia", pole_amalia)

        pole_ded = arcade.Sprite("1/razgovornoe_pole2.png", 1)
        pole_ded.center_x = 1200
        pole_ded.center_y = 900
        self.scene.add_sprite("Pole_Ded", pole_ded)

        pole_dver = arcade.Sprite("1/razgovornoe_pole.png", 0.6)
        pole_dver.center_x = 700
        pole_dver.center_y = 1140
        self.scene.add_sprite("Pole_Dver", pole_dver)

        self.ded = Ded()
        self.ded.center_x = 5000
        self.ded.center_y = 1000
        self.scene.add_sprite("Ded", self.ded)

        # я добавляю лишний спрайт для того, чтобы взять у него хитбокс и присвоить другому спрайту

        image_source = "1/hitbox.png"
        self.hitbox = arcade.Sprite(image_source, self.CHARACTER_SCALING)
        self.hitbox.center_x = 1100
        self.hitbox.center_y = 800

        self.player_sprite = Player()
        self.player_sprite.center_x = 120
        self.player_sprite.center_y = 800
        self.player_sprite.hit_box = self.hitbox.hit_box

        self.scene.add_sprite("Player", self.player_sprite)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.walls = [self.scene["stena"], self.scene["znaki"], self.scene["mebel"], self.scene["graniza"], self.scene["graniza2"], self.scene["personagi"], self.scene["Ded"]]

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=self.GRAVITY, walls=self.walls
        )

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

        if self.player_sprite.center_x > 890:
            if self.peremena_persongey == 0:
                self.scene["personagi"].clear()
                self.ded = Ded()
                self.ded.center_x = 1180
                self.ded.center_y = 1000
                self.scene.add_sprite("Ded", self.ded)
                self.peremena_persongey += 1



        self.player_collision_list = arcade.check_for_collision_with_lists(
            self.player_sprite,
            [
                self.scene["Pole_Amalia"],
                self.scene["Pole_Ded"],
                self.scene['Pole_Dver']
            ],
        )
        for collision in self.player_collision_list:
            if collision.sprite_lists != []:
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
                if self.dialog == 1 and self.scene["Pole_Amalia"] in collision.sprite_lists:
                    if self.vstrecha == 1:
                        self.v_box.clear()
                        self.v_box = Dialog("Pole_1")

                        self.manager.add(
                            arcade.gui.UIAnchorWidget(
                                anchor_x="center",
                                anchor_y='bottom',
                                child=self.v_box),
                        )
                        self.vstrecha = 0
                    if self.vstrecha == 0 and self.v_box.children == []:
                        self.dialog = 0
                if self.dialog == 1 and self.scene["Pole_Ded"] in collision.sprite_lists:
                    if self.vstrecha == 1:
                        self.v_box.clear()
                        self.v_box = Dialog("Pole_2")

                        self.manager.add(
                            arcade.gui.UIAnchorWidget(
                                anchor_x="center",
                                anchor_y='bottom',
                                child=self.v_box),
                        )
                        self.vstrecha = 0
                    if self.vstrecha == 0 and self.v_box.children == []:
                        self.dialog = 2
                if self.dialog == 2 and self.scene["Pole_Dver"] in collision.sprite_lists:
                    if self.vstrecha == 0:
                        self.v_box.clear()

                        open_dialog_button = Open_Dver()
                        self.v_box.add(open_dialog_button)

                        self.manager.add(
                            arcade.gui.UIAnchorWidget(
                                anchor_x="center",
                                anchor_y="bottom",
                                child=self.v_box)
                        )
                        open_dialog_button.on_click = self.on_click_dver
                        self.vstrecha = 1

        if self.player_collision_list == []:
            self.vstrecha = 0
            self.v_box.clear()


        if self.dialog == 2:
            for vorota in self.scene["mebel"]:
                if vorota.center_x == 720 and (vorota.center_y == 400 or vorota.center_y == 560):
                    vorota.remove_from_sprite_lists()
            sprite_nov_vorota = arcade.Sprite("1/nov_vorota.png", 1)
            sprite_nov_vorota.center_x = 720
            sprite_nov_vorota.center_y = 400
            sprite_nov_vorota.hit_box = sprite_nov_vorota.get_hit_box()
            self.scene["mebel"].append(sprite_nov_vorota)

    def on_click_open(self, event):
        self.v_box.clear()
        self.dialog = 1
        print("кнопка нажата")

    def on_click_dver(self, event):
        game_view = self.window.views['final_3']
        game_view.setup()
        self.window.show_view(game_view)

