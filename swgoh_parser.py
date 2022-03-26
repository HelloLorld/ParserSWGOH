import requests
import json
import xlsxwriter


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
        dictWithGalacticPowerAndUnits = {}
        jsonReqPlayer = getJsonInfoOfPlayer(id=allyCode)
        dictWithGalacticPowerAndUnits['galactic_power'] = jsonReqPlayer['data']['galactic_power']
        dictWithGalacticPowerAndUnits['units'] = jsonReqPlayer['units']
        dictOfPlayers[jsonReqPlayer['data']['name']
                      ] = dictWithGalacticPowerAndUnits
    return dictOfPlayers


# Записываем все данные в Excel
def writeDataIntoExcelTable(dictOfPlayers={}, path=""):
    f = open('config_units.txt', 'r', encoding='UTF-8')
    data = f.read()
    unitsTuple = tuple(data.split('\n'))
    
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('Units.xlsx')
    worksheet = workbook.add_worksheet()
    row = 0
    col = 0

    worksheet.write(row, col, 'Nickname')
    worksheet.write(row, col + 1, 'Galactic power')
    col += 2
    for unit in unitsTuple:
        worksheet.write(row, col, unit)
        col += 1
    
    row += 1
    col = 0
    for player in dictOfPlayers.keys():
        worksheet.write(row, col, player)
        col += 1
        worksheet.write(row, col, dictOfPlayers[player]['galactic_power'] ) 
        col += 1
        for unit in unitsTuple:
            try:
                worksheet.write(row, col, getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit))
            except:
                worksheet.write(row, col, 'Нет')
            col += 1
        row += 1
        col=0
    workbook.close()

def getStringOfGearAndRelic(dictOfPlayers={}, player='', unit=''):
    gearLvl = dictOfPlayers[player]['units'][unit]['gear_level']
    if gearLvl == 13:
        return str(gearLvl) + '+' + str(dictOfPlayers[player]['units'][unit]['relic_tier'])
    else:
        return str(gearLvl)


def arrOfUnitsToDict(units=[]):  # Массив персонажей переделываем в словарь
    dictOfUnits = {}
    for unit in units:
        gearLvl = unit['data']['gear_level']
        lvlOfUnit = {}
        lvlOfUnit['gear_level'] = gearLvl
        lvlOfUnit['relic_tier'] = unit['data']['relic_tier']-2
        dictOfUnits[unit['data']['name']] = lvlOfUnit
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
            dictWithGalacticPowerAndUnits = {}
            dictWithGalacticPowerAndUnits['galactic_power'] = jsonPlayerInfo['data']['galactic_power']
            dictWithGalacticPowerAndUnits['units'] = jsonPlayerInfo['units']
            dictOfPlayers[jsonPlayerInfo['data']
                          ['name']] = dictWithGalacticPowerAndUnits
        for key in dictOfPlayers.keys():
            dictOfPlayers[key]['units'] = arrOfUnitsToDict(
                dictOfPlayers[key]['units'])
        print(dictOfPlayers)
        writeDataIntoExcelTable(dictOfPlayers=dictOfPlayers, path=pathForSave)
        return 0
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
