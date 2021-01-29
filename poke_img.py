class PokeImg(object):
    def __init__(self):
        pass

    def get_poke_no_attr(self, poke_no, poke_name):
        poke_info = {
            'no': 1,
            'mega': False,
            'region': '',
            'forme': ''
        }

        poke_no_attr = poke_no.split("-")

        if len(poke_no_attr) != 1:
            pass
        else:
            poke_info["no"] = poke_no_attr[0]

        return poke_info
