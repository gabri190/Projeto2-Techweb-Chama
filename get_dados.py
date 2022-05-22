import http.client
import json

def get_players(id):
    conn = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Host': "free-nba.p.rapidapi.com",
        'X-RapidAPI-Key': "97167c7cc2mshbf62f83c1618b15p1d1cb2jsn097e721239cf"
        }

    conn.request("GET", f"/players/{id}", headers=headers)

    res = conn.getresponse()
    data = res.read()
    dict = json.loads(data.decode("utf-8"))
    return dict