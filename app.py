from storage import Pokemon
from flask import Flask, render_template

import requests



app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", messages=False)


@app.route('/contato')
def contact():
    return 'contato'


@app.route('/pokemons')
def pokemons():

    r = requests.get("https://pokeapi.co/api/v2/pokemon?limit=15&offset=20")
    result_api = r.json()
    pokemons = []
    for pokemon_api in result_api["results"]:
        r = requests.get(pokemon_api['url'])
        detail = r.json()
        pokemons.append(detail)

    return render_template("pokemons.html", data=pokemons)

@app.route('/pokemon/<int:id>')
def pokemon(id):
    r = requests.get("https://pokeapi.co/api/v2/pokemon/{id}/".format(id=id))
    data = r.json()
    return render_template("pokemon.html", data=data)
