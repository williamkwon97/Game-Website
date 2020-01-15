
"""
$ curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' -d 'fields *; where id = 29;' 'https://api-v3.igdb.com/company_logos/' | jq -r '.[].url'
    //images.igdb.com/igdb/image/upload/t_thumb/l9xwk37ap6xzjp4imoyh.jpg
$ curl 'https://images.igdb.com/igdb/image/upload/t_thumb/l9xwk37ap6xzjp4imoyh.jpg' --output blizzard.jpg
"""
COMPANY = 'company_image_urls'

def read_file(fn):
  f = open(fn, 'r').read()
  lst = f.split('\n')
  pairs = []
  for row in lst:
    pair = row.strip('\"').split(" ")
    pairs.append(pair)
  return pairs

def create_url_pairs(pairs):
  clean_pairs = []
  for row in pairs:
    if len(row) > 1:
      new_row = []
      new_row.append(str(row[0]))
      new_row.append('https:' + row[1])
      clean_pairs.append(new_row)
  return clean_pairs

def write_curls(pairs):
  for pair in pairs:
    print("curl '", pair[1], "' --output ", pair[0],  ".jpg", sep='')

def main():
  pairs = read_file(COMPANY)
#  print(pairs)
  clean_pairs = create_url_pairs(pairs)
#  print(clean_pairs)
  write_curls(clean_pairs)

main() 
