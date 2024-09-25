import requests
import json

API_KEY = None

class Account:
    def __init__(self, PUUID, name, tag_line):
        self.PUUID = PUUID
        self.name = name
        self.tag_line = tag_line

class Player(Account):
    def __init__(self, PUUID, name, tag_line, damage_to_champions, champion_id, kills, deaths, assists):
        super().__init__(PUUID, name, tag_line)
        self.damage_to_champions = damage_to_champions
        self.champion_id = champion_id
        self.kills = kills
        self.deaths = deaths
        self.assists = assists

class Match:
    """
        Should save: 
        1- match ID
        2- type of match
        3- 10 players data in 2 list each 5 players in a list (red team list, blue team list) -- players will be saved in player object
    """

    def __init__(self, match_ID):
        self.ID = match_ID
        self.loaded = False

    # it should first search the database for the content of it
    # if not found in the database then should request from the api and load the data of the match
    def load_match(self):
        pass

# make the request to the api
# returns an account object (returns null if not found)
def get_summoner(name, tag_line):
    pass

# search database for the accounts returns a list of the account object (empty list if none)
def load_accounts():
    pass

# load the matches from database first
# if not found then fetch the last 10 games from the api
# return a list of match object
def load_match_history(user_id):
    pass

# takes account object
# fetch api to get top 3 champions mastery
# return a list of the top 3 champions
def load_champions_mastery(user):
    pass

# save this account details in the database and add it to the list
def add_track(account, accounts_list):
    pass

# remove the account from the database and from the list
def remove_track(account, accounts_list):
    pass

def main():
    return

if __name__ == "__main__":
    main()