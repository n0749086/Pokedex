from poke_img import PokeImg


class PokeImgHiko(PokeImg):
    def __init__(self):
        self.base_path = 'https://hikochans.com/material/iconxy/'

    def conv_poke_no(self, pokedex_no, poke_name):
        self.get_poke_no_attr(pokedex_no, poke_name)

    def get_poke_img_path(self, pokedex_no, poke_name):
        self.conv_poke_no(pokedex_no, poke_name)

        path = "{}{}.png".format(self.base_path, self.poke_info["no"])

        return path
