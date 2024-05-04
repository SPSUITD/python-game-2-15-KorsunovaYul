import arcade
from pervoe_okno import Perv_okno
from Final_1 import final_1
def main():
    window = arcade.Window(fullscreen=True, title="В поисках Лили")
    window.total_score = 0
    menu_view = Perv_okno()
    window.show_view(menu_view)
    menu_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()