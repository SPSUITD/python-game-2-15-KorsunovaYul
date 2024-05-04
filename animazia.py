"""
Platformer Game
"""
import arcade

class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.UPDATES_PER_FRAME = 5
        self.STANDING_FRAME = 20

        self.scale = 1
        self.cur_texture = 0


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

    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        self.cur_texture += 1

        # Figure out if we should face left or right
        if self.change_x < 0 and self.change_y == 0:
            if self.cur_texture > 3 * self.UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.vlevo_textures[self.cur_texture // self.UPDATES_PER_FRAME]
        elif self.change_x > 0 and self.change_y == 0:
            if self.cur_texture > 3 * self.UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.vpravo_textures[self.cur_texture // self.UPDATES_PER_FRAME]
        elif self.change_x == 0 and self.change_y > 0:
            if self.cur_texture > 3 * self.UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.nazad_textures[self.cur_texture // self.UPDATES_PER_FRAME]
        elif self.change_x == 0 and self.change_y < 0:
            if self.cur_texture > 3 * self.UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.vpered_textures[self.cur_texture // self.UPDATES_PER_FRAME]

        elif self.change_x == 0 and self.change_y == 0:
            if self.cur_texture >= 10 * self.STANDING_FRAME:
                if self.cur_texture > 14 * self.STANDING_FRAME:
                    self.cur_texture = 10 * self.STANDING_FRAME
                self.texture = self.stoyka_textures[(self.cur_texture // self.STANDING_FRAME)-10]

class Ded(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.UPDATES_PER_FRAME = 10

        self.scale = 1
        self.cur_texture = 0


        self.nazad_textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"1/dr_personagi/DedNazad/{i}.png")
            self.nazad_textures.append(texture)

        self.vpered_textures = []
        for i in range(1, 5):
            texture = arcade.load_texture(f"1/dr_personagi/DedVpered/{i}.png")
            self.vpered_textures.append(texture)

        # By default, face right.
        self.texture = arcade.load_texture(f"1/dr_personagi/DedVpered/1.png")

    def update(self, delta_time: float = 1 / 60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        self.cur_texture += 1

        if self.change_x == 0 and self.change_y > 0:
            if self.cur_texture > 3 * self.UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.nazad_textures[self.cur_texture // self.UPDATES_PER_FRAME]
        elif self.change_x == 0 and self.change_y < 0:
            if self.cur_texture > 3 * self.UPDATES_PER_FRAME:
                self.cur_texture = 0
            self.texture = self.vpered_textures[self.cur_texture // self.UPDATES_PER_FRAME]
