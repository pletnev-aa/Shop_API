curl -X 'POST' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
'http://0.0.0.0:8000/api/shop/' \
-d '{"name":"TestShop","city":"TestCity","street":"TestStreet","number":"5","opening_time":"09:00","closing_time":"22:00"}'