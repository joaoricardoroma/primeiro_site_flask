from flask import Flask, render_template
from bs4 import BeautifulSoup
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

    return render_template("pokemons.html", data=[])


@app.route('/pokemon/<int:id>')
def pokemon(id):
    html_text = requests.get("https://www.pokemon.com/br/pokedex/bulbasaur").text
    soup = BeautifulSoup(html_text, "html.parser")
    name = soup.find("div", class_="pokedex-pokemon-pagination-title").text
    data = {
        "name": "bulbasaur"
    }
    return render_template("pokemon.html", data=data, name=name)