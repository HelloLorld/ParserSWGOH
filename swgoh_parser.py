import requests
import json


class NotFoundPlayer(Exception):  # Исключение о том, что игрок не был найден
    pass


def getJsonInfoOfPlayer(id=0):  # Запрос информации об игроке
    try:
        req = requests.get('https://swgoh.gg/api/player/' + str(id))
        print(req.status_code)
        if req.status_code == 200:
            jsonReqPlayer = json.loads(req.text)
            return jsonReqPlayer
    except requests.RequestException as e:
        print(e)


def getInfoAboutGuild(id=''):  # Запрос информации о гильдии
    try:
        req = requests.get('https://swgoh.gg/api/guild-profile/' + id)
        if req.status_code == 200:
            jsonReqGuild = json.loads(req.text)
            return jsonReqGuild['data']['members']
    except requests.RequestException as e:
        print(e)


# Получение информации по всем игрокам из гильдии
def getInfoAboutAllPlayers(allyCodes=[]):
    dictOfPlayers = {}
    for allyCode in allyCodes:
        jsonReqPlayer = getJsonInfoOfPlayer(id=allyCode)
        dictOfPlayers[jsonReqPlayer['data']['name']] = jsonReqPlayer['units']
    return dictOfPlayers


def writeDataIntoExcelTable(dictOfPlayers={}, path=""):
    pass


def arrOfUnitsToDict(units=[]):  # Массив персонажей переделываем в словарь
    dictOfUnits = {}
    for unit in units:
        gearLvl = unit['data']['gear_level']
        if gearLvl != 13:
            dictOfUnits[unit['data']['name']] = str(gearLvl)
        else:
            dictOfUnits[unit['data']['name']] = str(gearLvl) + ' + ' + str(unit['data']['relic_tier']-2)
    return dictOfUnits


def getInfoFromSWGOH(id=0, needGuild=False, pathForSave=""):  # Основная функция
    jsonPlayerInfo = getJsonInfoOfPlayer(id=id)
    if jsonPlayerInfo != None:
        dictOfPlayers = {}
        if needGuild:
            allyCodes = []
            members = getInfoAboutGuild(jsonPlayerInfo['data']['guild_id'])
            for member in members:
                allyCodes.append(member['ally_code'])
            dictOfPlayers = getInfoAboutAllPlayers(allyCodes=allyCodes)
        else:
            dictOfPlayers[jsonPlayerInfo['data']
                          ['name']] = jsonPlayerInfo['units']
        for key in dictOfPlayers.keys():
            dictOfPlayers[key] = arrOfUnitsToDict(dictOfPlayers[key])
        print(dictOfPlayers)
        writeDataIntoExcelTable(dictOfPlayers=dictOfPlayers, path=pathForSave)

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
