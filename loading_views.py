import arcade
from pervoe_okno import Perv_okno
from Chast_1 import chast_1
from Chast_2 import chast_2
from Chast_3 import chast_3
from Final_1 import final_1
from Final_2 import final_2
from Final_3 import final_3
from konzovki import Konzovki


class LoadingView(arcade.View):
    def __init__(self):
        super().__init__()

    def setup(self):
        self.window.views['pervoe_okno'] = Perv_okno()
        self.window.views['chast_1'] = chast_1()
        self.window.views['chast_2'] = chast_2()
        self.window.views['chast_3'] = chast_3()
        self.window.views['final_1'] = final_1()
        self.window.views['final_2'] = final_2()
        self.window.views['final_3'] = final_3()
        self.window.views['konzovki'] = Konzovki()
        self.window.views['loading_views'] = self


    def on_draw(self):
        arcade.start_render()
        self.window.show_view(self.window.views['pervoe_okno'])
        self.window.views['pervoe_okno'].setup()