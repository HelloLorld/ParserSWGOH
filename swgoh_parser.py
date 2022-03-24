import requests
import json


class NotFoundPlayer(Exception):
    pass


def getJsonInfoOfPlayer(id=0):
    try:
        req = requests.get('https://swgoh.gg/api/player/' + str(id))
        print(req.status_code)
        if req.status_code == 200:
            jsonReqPlayer = json.loads(req.text)
            return jsonReqPlayer
        # print(jsonReq['units'])
    except requests.RequestException as e:
        print(e)


def getInfoAboutGuild(id=''):
    try:
        req = requests.get('https://swgoh.gg/api/guild-profile/' + id)
        if req.status_code == 200:
            jsonReqGuild = json.loads(req.text)
            return jsonReqGuild['data']['members']
    except requests.RequestException as e:
        print(e)


def getInfoFromSWGOH(id=0, needGuild=False, pathForSave=""):
    jsonPlayerInfo = getJsonInfoOfPlayer(id=id)
    if jsonPlayerInfo != None:
        if needGuild:
            members = getInfoAboutGuild(jsonPlayerInfo['data']['guild_id'])
            for member in members:
                print(member['player_name'])
    else:
        raise NotFoundPlayer("Мы не смогли найти игрока")


def main():
    # id = int(input('Enter id: '))
    # print("You need mana?")
    # needGuild = False
    # if (input().lower().find("y") != -1):
    #     needGuild = True
    try:
        getInfoFromSWGOH(id=785425257, needGuild=True)
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
