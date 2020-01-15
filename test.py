import os
import sys
import unittest
from models import db, Game, Genre, Company

class DBTestCases(unittest.TestCase):
  def test_self_1(self):
    self.assertTrue(True)

  def test_game_insert_1(self):

    s = Game(game_id='20', name = 'The Game')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Game).filter_by(game_id = '20').one()
    self.assertEqual(str(r.game_id), '20')
    self.assertEqual(str(r.name), 'The Game')
    db.session.query(Game).filter_by(game_id = '20').delete()
    db.session.commit()

  def test_game_insert_2(self):

    s = Game(game_id='99', name = '99th Game', rating = '4.3', summary = 'I love this game')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Game).filter_by(game_id = '99').one()
    self.assertEqual(str(r.game_id), '99')
    self.assertEqual(str(r.rating), '4.3')
    self.assertEqual(str(r.summary), 'I love this game')
    db.session.query(Game).filter_by(game_id = '99').delete()
    db.session.commit()

  def test_game_insert_3(self):

    s = Game(game_id='3823', name = 'The Best Game Ever', rating = '10.0', summary = 'Never played a better game.')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Game).filter_by(game_id = '3823').one()
    self.assertEqual(str(r.game_id), '3823')
    self.assertEqual(str(r.rating), '10.0')
    self.assertEqual(str(r.summary), 'Never played a better game.')
    db.session.query(Game).filter_by(game_id = '3823').delete()
    db.session.commit()


  def test_game_insert_4(self):

    s = Game(game_id='1234', name = '123th Game', rating = '4.7')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Game).filter_by(game_id = '1234').one()
    self.assertEqual(str(r.game_id), '1234')
    self.assertEqual(str(r.name), '123th Game')
    self.assertEqual(str(r.rating), '4.7')
    db.session.query(Game).filter_by(game_id = '1234').delete()
    db.session.commit()

  def test_game_insert_5(self):

    s = Game(game_id='23', name = 'Shooting', url = 'google.com')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Game).filter_by(game_id = '23').one()
    self.assertEqual(str(r.game_id), '23')
    self.assertEqual(str(r.name), 'Shooting')
    self.assertEqual(str(r.url), 'google.com')
    db.session.query(Game).filter_by(game_id = '23').delete()
    db.session.commit()

  def test_game_insert_6(self):

    s = Game(game_id='25', name = 'Shooting', url = '')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Game).filter_by(game_id = '25').one()
    self.assertEqual(str(r.game_id), '25')
    self.assertEqual(str(r.name), 'Shooting')
    self.assertEqual(str(r.url), '')
    db.session.query(Game).filter_by(game_id = '25').delete()
    db.session.commit()

  def test_genre_insert_1(self):

    s = Genre(genre_id='9999', name = 'GenreTest', url = 'google.com', description = 'what a cool genre')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Genre).filter_by(genre_id = '9999').one()
    self.assertEqual(str(r.genre_id), '9999')
    self.assertEqual(str(r.name), 'GenreTest')
    self.assertEqual(str(r.url), 'google.com')
    self.assertEqual(str(r.description), 'what a cool genre')
    db.session.query(Genre).filter_by(genre_id = '9999').delete()
    db.session.commit()

  def test_genre_insert_2(self):

    s = Genre(genre_id='5291', name = 'NoGenre', url = 'sup.com', description = 'best genre')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Genre).filter_by(genre_id = '5291').one()
    self.assertEqual(str(r.genre_id), '5291')
    self.assertEqual(str(r.name), 'NoGenre')
    self.assertEqual(str(r.url), 'sup.com')
    self.assertEqual(str(r.description), 'best genre')
    db.session.query(Genre).filter_by(genre_id = '5291').delete()
    db.session.commit()

  def test_genre_insert_3(self):

    s = Genre(genre_id='1928', name = 'IsThisWorking', url = 'work.com', description = 'this should work')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Genre).filter_by(genre_id = '1928').one()
    self.assertEqual(str(r.genre_id), '1928')
    self.assertEqual(str(r.name), 'IsThisWorking')
    self.assertEqual(str(r.url), 'work.com')
    self.assertEqual(str(r.description), 'this should work')
    db.session.query(Genre).filter_by(genre_id = '1928').delete()
    db.session.commit()

  def test_genre_insert_4(self):

    s = Genre(genre_id='6574', name = 'AnothaOne', url = 'thekey.com', description = 'just another genre')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Genre).filter_by(genre_id = '6574').one()
    self.assertEqual(str(r.genre_id), '6574')
    self.assertEqual(str(r.name), 'AnothaOne')
    self.assertEqual(str(r.url), 'thekey.com')
    self.assertEqual(str(r.description), 'just another genre')
    db.session.query(Genre).filter_by(genre_id = '6574').delete()
    db.session.commit()

  def test_genre_insert_5(self):

    s = Genre(genre_id='8323', name = 'compsci', url = 'computer.com', description = 'comp genre')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Genre).filter_by(genre_id = '8323').one()
    self.assertEqual(str(r.genre_id), '8323')
    self.assertEqual(str(r.name), 'compsci')
    self.assertEqual(str(r.url), 'computer.com')
    self.assertEqual(str(r.description), 'comp genre')
    db.session.query(Genre).filter_by(genre_id = '8323').delete()
    db.session.commit()
	
  def test_company_insert_1(self):

    s = Company(company_id='626', name = 'stitch corp', country = '22', description = 'a new company')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Company).filter_by(company_id = '626').one()
    self.assertEqual(str(r.company_id), '626')
    self.assertEqual(str(r.name), 'stitch corp')
    self.assertEqual(str(r.country), '22')
    self.assertEqual(str(r.description), 'a new company')
    db.session.query(Company).filter_by(company_id = '626').delete()
    db.session.commit()

  def test_company_insert_2(self):

    s = Company(company_id='6789', name = 'soulja inc', country = '77', description = 'soulja boy tell em')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Company).filter_by(company_id = '6789').one()
    self.assertEqual(str(r.company_id), '6789')
    self.assertEqual(str(r.name), 'soulja inc')
    self.assertEqual(str(r.country), '77')
    self.assertEqual(str(r.description), 'soulja boy tell em')
    db.session.query(Company).filter_by(company_id = '6789').delete()
    db.session.commit()
	
  def test_company_insert_3(self):

    s = Company(company_id='365', name = 'pizza pie', country = '85', description = 'its hot')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Company).filter_by(company_id = '365').one()
    self.assertEqual(str(r.company_id), '365')
    self.assertEqual(str(r.name), 'pizza pie')
    self.assertEqual(str(r.country), '85')
    self.assertEqual(str(r.description), 'its hot')
    db.session.query(Company).filter_by(company_id = '365').delete()
    db.session.commit()
	
  def test_company_insert_4(self):

    s = Company(company_id='999', name = 'final co', country = '105', description = 'is it the last?')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Company).filter_by(company_id = '999').one()
    self.assertEqual(str(r.company_id), '999')
    self.assertEqual(str(r.name), 'final co')
    self.assertEqual(str(r.country), '105')
    self.assertEqual(str(r.description), 'is it the last?')
    db.session.query(Company).filter_by(company_id = '999').delete()
    db.session.commit()

  def test_company_insert_5(self):

    s = Company(company_id='69', name = 'uno mas', country = '219', description = 'es el final')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Company).filter_by(company_id = '69').one()
    self.assertEqual(str(r.company_id), '69')
    self.assertEqual(str(r.name), 'uno mas')
    self.assertEqual(str(r.country), '219')
    self.assertEqual(str(r.description), 'es el final')
    db.session.query(Company).filter_by(company_id = '69').delete()
    db.session.commit()

  def test_company_insert_6(self):

    s = Company(company_id='70', name = 'uno mas', country = '219', description = '')
    db.session.add(s)
    db.session.commit()
    r = db.session.query(Company).filter_by(company_id = '70').one()
    self.assertEqual(str(r.company_id), '70')
    self.assertEqual(str(r.name), 'uno mas')
    self.assertEqual(str(r.country), '219')
    self.assertEqual(str(r.description), '')
    db.session.query(Company).filter_by(company_id = '70').delete()
    db.session.commit()

if __name__ == '__main__':
  unittest.main()
