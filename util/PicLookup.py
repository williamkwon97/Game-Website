import json

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

def find_companies():
  companies = load_json('companies.json')
  company_logos = []

  for company in companies['Companies']:
    if 'logo' in company:
      company_logos.append(company['logo'])

  return company_logos


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


"""
$ curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' -d 'fields *; where id = 29;' 'https://api-v3.igdb.com/company_logos/' | jq -r '.[].url'
    //images.igdb.com/igdb/image/upload/t_thumb/l9xwk37ap6xzjp4imoyh.jpg
$ curl 'https://images.igdb.com/igdb/image/upload/t_thumb/l9xwk37ap6xzjp4imoyh.jpg' --output blizzard.jpg
"""

def print_curl(g):
  for group in g:
    print("curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' -d 'fields *; limit 50; where id = ", tuple(group), ";' 'https://api-v3.igdb.com/company_logos/' | jq '.[] | (.id|tostring) + \" \" + .url' >> company_image_urls", sep="")

def main():
  print ('rm company_image_urls')
  print_curl(split_list(find_companies()))

main() 
