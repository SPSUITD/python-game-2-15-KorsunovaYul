"""
Platformer Game
"""
import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Platformer"

CHARACTER_SCALING = 1

UPDATES_PER_FRAME = 5
STANDING_FRAME = 20

PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 0


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = CHARACTER_SCALING
        self.textures = []
        self.cur_texture = 0

        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.


        self.nazad_textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"1/ella/kadri/Nazad/{i}.png")
            self.nazad_textures.append(texture)

        self.vlevo_textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"1/ella/kadri/Vlevo/{i}.png")
            self.vlevo_textures.append(texture)

        self.vpravo_textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"1/ella/kadri/Vpravo/{i}.png")
            self.vpravo_textures.append(texture)

        self.vpered_textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"1/ella/kadri/Vpered/{i}.png")
            self.vpered_textures.append(texture)

        self.stoyka_textures = []
        for i in range(1, 6):
            texture = arcade.load_texture(f"1/ella/kadri/Stoyka/{i}.png")
            self.stoyka_textures.append(texture)

        # By default, face right.
        self.texture = arcade.load_texture(f"1/ella/kadri/Vpered/1.png")

    def update(self, delta_time: int = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        self.cur_texture += 1

        # Figure out if we should face left or right
        if self.change_x < 0 and self.change_y == 0:
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.vlevo_textures[self.cur_texture // UPDATES_PER_FRAME]
        elif self.change_x > 0 and self.change_y == 0:
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.vpravo_textures[self.cur_texture // UPDATES_PER_FRAME]
        elif self.change_x == 0 and self.change_y > 0:
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.nazad_textures[self.cur_texture // UPDATES_PER_FRAME]
        elif self.change_x == 0 and self.change_y < 0:
            if self.cur_texture > 3 * UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.vpered_textures[self.cur_texture // UPDATES_PER_FRAME]

        elif self.change_x == 0 and self.change_y == 0:
            if self.cur_texture >= 10 * STANDING_FRAME:
                if self.cur_texture > 14 * STANDING_FRAME:
                    self.cur_texture = 10 * STANDING_FRAME
                self.texture = self.stoyka_textures[(self.cur_texture // STANDING_FRAME)-10]


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.scene = None
        self.player_sprite = None
        self.physics_engine = None
        self.camera = None
        self.gui_camera = None

        self.player_sprite_list = None

        arcade.set_background_color(arcade.csscolor.WHITE)

    def setup(self):

        self.camera = arcade.Camera()
        self.gui_camera = arcade.Camera()
        self.scene = arcade.Scene()

        self.player_sprite_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 300
        self.player_sprite_list.append(self.player_sprite)

        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY
        )

    def on_draw(self):

        self.clear()

        self.camera.use()

        # Draw our Scene
        self.scene.draw()

        self.gui_camera.use()

        self.player_sprite_list.draw()

    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.W:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

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
        self.player_sprite_list.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()