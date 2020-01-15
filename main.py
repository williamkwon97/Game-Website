from flask import render_template, request
from create_db import app, db, Game, Genre, Company, create_games
import subprocess

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/games/')
@app.route('/games/<game_id>')
def games(game_id = None):
  if game_id is None:
    games = db.session.query(Game).join((Genre, Game.genres)).join((Company, Game.companies)).all()
    return render_template('games.html', games = games)

  game = db.session.query(Game).filter(Game.game_id == (int(game_id))).join((Genre, Game.genres)).join((Company, Game.companies)).first()
  return render_template('game_details.html', game = game)


@app.route('/genres/')
@app.route('/genres/<genre_id>')
def genres(genre_id = None):
  if genre_id is None:
    genres = db.session.query(Genre).join((Game, Genre.games)).all()
    return render_template('genres.html', genres = genres)

  genre = db.session.query(Genre).filter(Genre.genre_id == (int(genre_id))).join((Game, Genre.games)).first()
  return render_template('genre_details.html', genre = genre)


@app.route('/companies/')
@app.route('/companies/<company_id>')
def companies(company_id = None):
  if company_id is None:
    companies = db.session.query(Company).join((Game, Company.games)).all()
    return render_template('companies.html', companies = companies)

  company = db.session.query(Company).filter(Company.company_id == (int(company_id))).join((Game, Company.games)).first()
  return render_template('company_details.html', company = company)


@app.route('/search/')
def search():
  search_str = request.args.get('search_str')
  print("SEARCH STRING:", search_str)
  if search_str is None:
    return render_template('search.html', games = [], companies = [], genres = [])

  games = db.session.query(Game).filter(Game.name.ilike("%" + search_str + "%")).all()
  companies = db.session.query(Company).filter(Company.name.ilike("%" + search_str + "%")).all()
  genres = db.session.query(Genre).filter(Genre.name.ilike("%" + search_str + "%")).all()
  return render_template('search.html', games = games, companies = companies, genres = genres)

@app.route('/about/')
def about():
	return render_template('about.html')

@app.route('/test/')
def test():
    p = subprocess.Popen(["coverage", "run", "--branch", "test.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE)
    out, err = p.communicate()
    output=err+out
    output = output.decode("utf-8") #convert from byte type to string type
    
    return render_template('test.html', output = "<br/>".join(output.split("\n")))

if __name__ == "__main__":
  app.run()
