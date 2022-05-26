Shuffle Playlist

Django with DRF used for API backend
DRF swagger UI for API doc



STEPS TO RUN

1.docker-compose build
2.docker-compose up




TYPES OF USERS -> ADMIN USER & STANDARD USER


/api/v1/docs for documentation

Authentication -> Token 


1. Requesting Admin User Token

curl -X POST "http://localhost:4000/api-token-auth/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"demo-user\",  \"password\": \"1234\"}"

Response
200 
{"token":"9729082e78c58f750bfc277d368510920bfc00bd"}    


2. Creating standard user
curl -X POST "http://localhost:4000/api/v1/user/" -H "Authorization: Token 9729082e78c58f750bfc277d368510920bfc00bd" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"standard-user\",  \"email\": \"standard-user@sample.com\",  \"password\": \"12345\"}"

Response
201
{"username":"standard-user","email":"standard-user@sample.com"} 


3. Requesting standard user token
curl -X POST "http://localhost:4000/api-token-auth/" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"username\": \"standard-user\",  \"password\": \"12345\"}
"

Response 
200
{"token":"24935465e18e8b7f32a049f0771f1d87473bdf7b"} 



Listing all USERS, CRUD -> SONGS etc requires admin user privileges

UserPlaylist/ playlist CRUD and shuffle requires authenticated user



Playlist & UserPlaylist both must be added.
Shuffle will return status 200 on completion. 

Shuffle changes the order in which songs are listed in every playlist. 
