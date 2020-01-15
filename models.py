# beginning of models.py
# note that at this point you should have created "bookdb" database (see install_postgres.txt).
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING",'postgres://postgres:abc123@localhost:5432/gamesdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to suppress a warning message
db = SQLAlchemy(app)

game_genres = db.Table('game_genres',
  db.Column('game_id', db.Integer, db.ForeignKey('games.game_id'), primary_key = True),
  db.Column('genre_id', db.Integer, db.ForeignKey('genres.genre_id'), primary_key = True)
)

game_companies = db.Table('game_companies',
  db.Column('game_id', db.Integer, db.ForeignKey('games.game_id'), primary_key = True),
  db.Column('company_id', db.Integer, db.ForeignKey('companies.company_id'), primary_key = True)
)

class Game(db.Model):
  __tablename__ = 'games'

  game_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100), nullable = False)
  rating = db.Column(db.Float(5), nullable = True)
  summary = db.Column(db.String(5000), nullable = True)
  url = db.Column(db.String(250), nullable = True)
  genres = db.relationship('Genre', secondary=game_genres, lazy='subquery',
    backref=db.backref('games', lazy=True))
  companies = db.relationship('Company', secondary=game_companies, lazy='subquery',
    backref=db.backref('games', lazy=True))

class Genre(db.Model):
  __tablename__ = 'genres'

  genre_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(250), nullable = False)
  url = db.Column(db.String(500), nullable = False)
  description = db.Column(db.String(5000), nullable = False)
  popularity = db.Column(db.Integer, nullable = True)

class Company(db.Model):
  __tablename__ = 'companies'

  company_id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(250), nullable = True)
  description = db.Column(db.String(5000), nullable = True)
  logo = db.Column(db.Integer, nullable = True)
  country = db.Column(db.Integer, nullable = True)
  date_founded = db.Column(db.String(250), nullable = True)

db.drop_all()
db.create_all()
# End of models.py
