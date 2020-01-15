import json
import random
#from models import app, db, Game, Genre, Company
from models import app, db, Genre, Game, Company, game_genres, game_companies
from datetime import datetime

def load_json(filename):
    with open(filename, encoding = "utf8") as file:
        jsn = json.load(file)
        file.close()

    return jsn

# channel1.subscribers.append(user1)
# genre1.games.append(game1)
# game1.genres.append(genre1)

def create_games():
  games = load_json('newgames.json')

  for oneGame in games['Games']:

    game_id = oneGame['id']
    name = oneGame['name']

    if 'rating' in oneGame:
      rating = oneGame['rating']
    else:
      rating = 0.0
    if 'summary' in oneGame:
      summary = oneGame['summary']
    else:
      summary = ''
    if 'url' in oneGame:
      url = oneGame['url']
    else:
      url = ''
    if 'genres' in oneGame:
      genres = oneGame['genres']
    else:
      genres = []
    if 'involved_companies' in oneGame:
      companies = oneGame['involved_companies']
    else:
      companies = []

    newGame = Game(game_id = game_id, name = name, rating = rating, summary = summary, url = url)
    db.session.add(newGame)
    db.session.commit()

    for genre_id in genres:
      statement = game_genres.insert().values(game_id = game_id, genre_id = genre_id)
      db.session.execute(statement)
      db.session.commit()

    """
    for company_id in companies:
      try:
        statement = game_companies.insert().values(game_id = game_id, company_id = company_id)
        db.session.execute(statement)
        db.session.commit()
        print("succeeded for", game_id, company_id)
      except:
        print("failed for", game_id, company_id)
        db.session.rollback()
      """
def create_genres():
    genres = load_json('genres.json')

    for oneGenre in genres['Genres']:
        name = oneGenre['name']
        id = oneGenre['id']
        url = oneGenre['url']
        description = oneGenre['description']
        popularity = random.randint(1, 100)

        newGenre = Genre(genre_id = id, name = name, url = url, description = description, popularity = popularity)

        # After I create the book, I can then add it to my session.
        db.session.add(newGenre)
        # commit the session to my DB.
        db.session.commit()

def create_companies():
  companies = load_json('companies.json')

  for oneCompany in companies['Companies']:
    company_id = oneCompany['id']
    name = oneCompany['name']

    if 'developed' in oneCompany:
      games = oneCompany['developed']
    else:
      games = []

    description = ''
    if 'description' in oneCompany:
      description = oneCompany['description']

    logo = 0
    if 'logo' in oneCompany:
      logo = oneCompany['logo']

    if 'country' in oneCompany:
        country = oneCompany['country']

    if 'start_date' in oneCompany:
        date_founded_unix = oneCompany['start_date']
        if date_founded_unix < 86400:
            date_founded_unix = 86400
        else:
            date_founded = datetime.utcfromtimestamp(date_founded_unix).strftime('%Y-%m-%d')

    newCompany = Company(company_id = company_id, name = name, description = description, logo = logo, country = country, date_founded = date_founded)

    # After I create the book, I can then add it to my session.
    db.session.add(newCompany)
    # commit the session to my DB.
    db.session.commit()

    for game_id in games:
      try:
        statement = game_companies.insert().values(game_id = game_id, company_id = company_id)
        db.session.execute(statement)
        db.session.commit()
      except:
        db.session.rollback()

create_genres()
create_games()
create_companies()
# end of create_db.py
