from flask import Flask, render_template
import os
from pokedex import Pokedex

app = Flask(__name__)

@app.route('/')
def get_poke_info():
    pokedex = Pokedex()
    poke_name = pokedex.get_poke_name_list()
    return render_template('poke_info.html', title=poke_name[0] + "のステータス", name=poke_name[0])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
