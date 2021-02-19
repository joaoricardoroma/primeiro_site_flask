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
    # name1 = name.find("div").text
    # number = name.find("span", class_="pokemon-number").text

    data = {
        "name": "bulbasaur"
    }
    return render_template("pokemon.html", data=data, name=name)


html_text = requests.get("https://www.pokemon.com/br/pokedex/bulbasaur").text
soup = BeautifulSoup(html_text, "html.parser")
name = soup.find("div", class_="pokedex-pokemon-pagination-title").text
# name1 = name.find("div").text
# number = name.find("span", class_="pokemon-number").text
# nome_do_pokemon = informacoes_do_pokemon.find("div")
print(name)
