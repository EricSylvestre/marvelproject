import requests
import hashlib

hash = '123456789' + '8405b2ce19e5b84264026b0d5180cf6e00cd7d7c' + '364c19885741c1b869771761119ba3d4'
api_link = f'http://gateway.marvel.com/v1/public/characters?limit=100&ts=<random_number>&apikey=<MARVEL_PUBLIC_KEY>&hash={(hashlib.md5(hash.encode())).hexdigest()}'


print(requests.get(api_link).json())