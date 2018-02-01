import jwt, cryptography

jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256', headers={'kid': '230498151c214b788dd97f22b85410a5'})

print(encoded)