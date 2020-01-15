rm -f companies.json
rm -f games.json
rm -f genres.json

printf "{\n\"Companies\": " > companies.json

curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, developed, description, logo, country, start_date; limit 50; \
where developed != null & logo != null & description != null & country != null;' \
'https://api-v3.igdb.com/companies/' >> companies.json

#echo "BREAK" >> companies.json

#curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' -d 'fields name, developed, description, logo, country;limit 50; where id =  (45572, 44551, 48142, 67098, 3116, 3117, 51763, 65075, 22073, 48206) | id =  (76391, 19569, 19570, 41585, 41586, 34425, 56963, 56965, 4750, 4751) | id =  (28817, 28818, 43675, 43676, 69282, 69283, 33456, 57521, 57522, 61121) | id =  (45764, 11975, 11976, 11977, 40151, 40153, 40154, 43764, 32501, 32502) | id =  (32507, 32508, 40189, 40190, 40191, 32512, 40192, 40193, 40194, 32525) | id =  (32535, 32555, 40750, 40751, 32562, 32563, 32572, 32573, 22846, 22847) | id =  (22848, 32598, 76632, 32604, 32605, 7518, 7519, 7530, 7531, 46448) | id =  (32626, 25463, 32637, 7557, 72585, 47499, 32656, 32657, 32658, 32659) | id =  (19347, 32662, 18353, 47554, 57302, 64483, 72685, 72686, 24562, 24563) | id =  (24564, 24565);' 'https://api-v3.igdb.com/companies/' >> companies.json

#curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
#-d 'fields name, developed, description, logo; offset 50; limit 50; \
#where developed != null & logo != null & description != null;' \
#'https://api-v3.igdb.com/companies/' | jq '.[]' >> companies.json

printf "\n}" >> companies.json


printf "{\n\"Games\": " > games.json

curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, rating, genres, involved_companies, url, summary; limit 50; \
where rating != null & genres != null & summary != null & involved_companies != null;' \
'https://api-v3.igdb.com/games/' >> games.json

#curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
#-d 'fields name, rating, genres, involved_companies, url, summary; offset 50; limit 50; \
#where rating != null & genres != null & summary != null & involved_companies != null;' \
#'https://api-v3.igdb.com/games/' | jq '.[]' >> games.json

printf "\n}" >> games.json

printf "{\n\"Genres\": " > genres.json

curl -H 'user-key: 401df87a02a8f4c13842a135bad415a4' \
-d 'fields name, url; limit 50;' \
'https://api-v3.igdb.com/genres/' >> genres.json

printf "\n}" >> genres.json

