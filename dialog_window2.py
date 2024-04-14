"""
Example code showing how to use the OKMessageBox
"""
import arcade
import arcade.gui
from arcade import load_texture
from arcade.gui.widgets import UITextArea, UIInputText, UITexturePane


class MyWindow(arcade.Window):

    def __init__(self):
        super().__init__(800, 600, "OKMessageBox Example", resizable=True)
        arcade.set_background_color(arcade.color.COOL_GREY)

        # Create and enable the UIManager
        self.manager = arcade.gui.UIManager()
        self.manager.enable()


        # Create a box group to align the 'open' button in the center
        self.v_box = arcade.gui.UIBoxLayout()

        red_style = {
            "font_name": ("Epilepsy Sans",),
            "font_size": 20,
            "font_color": (243, 212, 214),
            "border_width": 4,
            "border_color": None,
            "bg_color": (252, 65, 74),

            # used if button is pressed
            "bg_color_pressed": (243, 212, 214),
            "border_color_pressed": None,  # also used when hovered
            "font_color_pressed": (252, 65, 74),
        }

        open_dialog_button = arcade.gui.UIFlatButton(x=340, y=200, width=150, height=50, text="Диалог", style=red_style)
        self.v_box.add(open_dialog_button)

        # Add a hook to run when we click on the button.
        open_dialog_button.on_click = self.on_click_open
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center",
                anchor_y="bottom",
                child=self.v_box)
        )

    def on_click_open(self, event):

        self.v_box = arcade.gui.UIBoxLayout()

        dialog_style = {
            "font_name": ("Epilepsy Sans",),
            "font_size": 20,
            "font_color": (0, 44, 60),
            "border_width": 4,
            "border_color": (252, 65, 74),
            "bg_color": (243, 212, 214),
            "align": "right",

            # used if button is pressed
            "bg_color_pressed": (243, 212, 214),
            "border_color_pressed": (252, 65, 74),  # also used when hovered
            "font_color_pressed": (252, 65, 74),
        }

        dialog_button = arcade.gui.UIFlatButton(width=700, height=200, text="А небо голубое",
                                                style=dialog_style)

        self.v_box.add(dialog_button)


        self.manager.add(
                arcade.gui.UIAnchorWidget(
                    anchor_x="center",
                    anchor_y='bottom',
                    child=self.v_box),
        )

    def on_draw(self):
        self.clear()
        self.manager.draw()


window = MyWindow()
arcade.run()