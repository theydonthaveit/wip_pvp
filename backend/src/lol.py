import requests


def on_get(url):
    API = "RGAPI-21b79888-9e13-4294-8f8f-26ec0db44c3d"
    HEADERS = {
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": API,
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }

    r = requests.get(url, headers=HEADERS)

    if r.status_code == 200:
        return r.json()


def retrieve_summoner(region, summoner_name):
    URL = "https://%s.api.riotgames.com/lol/summoner/v3/summoners/by-name/%s" % (region, summoner_name)
    return on_get(URL)


print(retrieve_summoner('euw1', 'meow side'))