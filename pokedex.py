import csv
import pickle

class Pokedex:
    poke_list = []
    poke_name_list = []

    def __init__(self):
        self.poke_name_list, self.poke_list = pickle.load(open("poke.pkl", "rb"))
        # with open("pokemon_status.csv") as f:
        #     reader = csv.reader(f)
        #     next(reader)
        #     for row in reader:
        #         self.poke_list.append(row)
        #         self.poke_name_list.append(row[1])
        # with open("poke.pkl", "wb") as f:
        #     l = [self.poke_name_list, self.poke_list]
        #     pickle.dump(l, f)

    def get_poke_name_list(self):
        return self.poke_name_list

if __name__ == "__main__":
    poke = Pokedex()