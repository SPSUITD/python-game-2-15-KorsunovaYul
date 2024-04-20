"""
Platformer Game
"""
import arcade
from animazia import Player

class MyGame(arcade.Window):
    def __init__(self):
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.SCREEN_TITLE = "Platformer"

        self.CHARACTER_SCALING = 1
        self.TILE_SCALING = 1

        self.PLAYER_MOVEMENT_SPEED = 5
        self.GRAVITY = 0

        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, self.SCREEN_TITLE, fullscreen=True)

        self.scene = None
        self.player_sprite = None
        self.player_sprite_list = None
        self.hitbox = None
        self.physics_engine = None
        self.camera = None
        self.gui_camera = None
        self.tile_map = None
        self.background_color = (252, 65, 74, 0)

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
        }
        self.tile_map = arcade.load_tilemap(map_name, self.TILE_SCALING, layer_options)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # я добавляю лишний спрайт для того, чтобы взять у него хитбокс и присвоить другому спрайту

        image_source = "1/hitbox.png"
        self.hitbox = arcade.Sprite(image_source, self.CHARACTER_SCALING)
        self.hitbox.center_x = 300
        self.hitbox.center_y = 190

        self.player_sprite = Player()
        self.player_sprite.center_x = 300
        self.player_sprite.center_y = 190
        self.player_sprite.hit_box = self.hitbox.hit_box

        self.scene.add_sprite("Player", self.player_sprite)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.walls = [self.scene["stena"], self.scene["znaki"], self.scene["mebel"], self.scene["graniza"], self.scene["graniza2"]]

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=self.GRAVITY, walls=self.walls,
        )

    def on_draw(self):

        self.clear()

        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        self.gui_camera.use()


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
            self.set_fullscreen(not self.fullscreen)

            width, height = self.get_size()
            self.set_viewport(0, width, 0, height)

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