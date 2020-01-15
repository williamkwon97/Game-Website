import json

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn


def find_existing_companies():
  companies = load_json('companies.json')
  company_ids = []

  for company in companies['Companies']:
    company_ids.append(company['id'])

  return company_ids

def find_all_companies():
  games = load_json('games.json')
  existing_ids = find_existing_companies()
  missing_ids = []

  for game in games['Games']:
    companies = game['involved_companies']

    for company_id in companies:
      missing_ids.append(company_id)

  missing_ids_dedup = list(set(missing_ids))
  return missing_ids_dedup

def find_missing_companies():
  games = load_json('games.json')
  existing_ids = find_existing_companies()
  missing_ids = []

  for game in games['Games']:
    companies = game['involved_companies']

    for company_id in companies:
      if (company_id not in existing_ids) and (company_id not in missing_ids):
        missing_ids.append(company_id)

  missing_ids_dedup = list(set(missing_ids))
  return missing_ids_dedup

def find_existing_games():
  games = load_json('games.json')
  game_ids = []

  for game in games['Games']:
    game_ids.append(game['id'])

  return game_ids

def find_missing_games():
  companies = load_json('companies.json')
  existing_ids = find_existing_games()
  missing_ids = []

  for company in companies['Companies']:
    if 'developed' in company:
      games = company['developed']
      for game_id in games:
        if (game_id not in existing_ids) and (game_id not in missing_ids):
          missing_ids.append(game_id)

  missing_ids_dedup = list(set(missing_ids))
  return missing_ids_dedup

def split_list(l):
  idx = 0
  groups = []
  while idx < len(l):
    group = []
    for i in range(10):
      if idx >= len(l):
        break
      group.append(l[idx])
      idx += 1
    groups.append(group)
  return groups

def format_groups(g):
  print("where", end = " ")
  for group in g:
    print("id = ", tuple(group), "|", end=" ")

def print_curl(g):
  for group in g:
    print("curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' -d 'fields name, rating, genres, involved_companies, url, summary; limit 50; where id = ", tuple(group), ";' 'https://api-v3.igdb.com/games/' >> newgames.json", sep="")

def main():
  """
  grouped_cos = split_list(find_missing_companies())
  print("EXISTING:", find_existing_companies())
  print("MISSING:", grouped_cos)
  format_groups(grouped_cos)

  print("ALL")
  print(find_all_companies())
  print(len(find_all_companies()))

  print("-----")
  """
  print_curl(split_list(find_missing_games()))

main() 
