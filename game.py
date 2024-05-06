import arcade
from loading_views import LoadingView


class Window(arcade.Window):
    def __init__(self):
        super().__init__(fullscreen=True, title="В поисках Лили", resizable=True)
        self.views = {}

def main():
    window = Window()
    window.total_score = 0
    menu_view = LoadingView()
    menu_view.setup()
    window.show_view(menu_view)
    arcade.run()



if __name__ == "__main__":
    main()