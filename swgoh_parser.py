from datetime import datetime
import requests
import json
import xlsxwriter


class NotFoundPlayer(Exception):  # Исключение о том, что игрок не был найден
    pass


def getJsonInfoOfPlayer(id=0):  # Запрос информации об игроке
    req = requests.get('https://swgoh.gg/api/player/' + str(id))
    print(req.status_code)
    if req.status_code == 200:
        jsonReqPlayer = json.loads(req.text)
        return jsonReqPlayer


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
    workbook = xlsxwriter.Workbook(path + 'statistics_'+ datetime.now().strftime("%d_%m_%Y_%H_%M_%S")+ '.xlsx')
    #workbook = xlsxwriter.Workbook('Units.xlsx')
    worksheet = workbook.add_worksheet()
    cell_format_style =workbook.add_format()
    cell_format_style.set_pattern(1)
    cell_format_style.set_border(style=2)
    cell_format_style.set_bg_color('#ffffff')
    cell_format_style.set_align('center')


    cell_format_yellow = workbook.add_format()
    cell_format_yellow.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_yellow.set_bg_color('#ffff00')
    cell_format_yellow.set_border(style=2)
    cell_format_yellow.set_align('center')

    cell_format_green = workbook.add_format()
    cell_format_green.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_green.set_bg_color('#92d050')
    cell_format_green.set_border(style=2)
    cell_format_green.set_align('center')

    cell_format_darkgreen = workbook.add_format()
    cell_format_darkgreen.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_darkgreen.set_bg_color('#00b050')
    cell_format_darkgreen.set_border(style=2)
    cell_format_darkgreen.set_align('center')

    cell_format_pink = workbook.add_format()
    cell_format_pink.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_pink.set_bg_color('#fde9d9')
    cell_format_pink.set_border(style=2)
    cell_format_pink.set_align('center')

    cell_format_blue = workbook.add_format()
    cell_format_blue.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_blue.set_bg_color('#00b0f0')
    cell_format_blue.set_border(style=2)
    cell_format_blue.set_align('center')

    cell_format_lightgreen = workbook.add_format()
    cell_format_lightgreen.set_pattern(1)  # This is optional when using a solid fill.
    cell_format_lightgreen.set_bg_color('#c4d79b')
    cell_format_lightgreen.set_border(style=2)
    cell_format_lightgreen.set_align('center')
    worksheet.set_row(0, 20)
    worksheet.set_column('A:AR', 20)
    row = 0
    col = 0

    worksheet.write(row, col, 'Nickname',cell_format_style)
    worksheet.write(row, col + 1, 'Galactic power',cell_format_style)
    col += 2
    for unit in unitsTuple:
        worksheet.write(row, col, unit, cell_format_style)
        col += 1
    
    row += 1
    col = 0
    for player in dictOfPlayers.keys():
        worksheet.write(row, col, player,cell_format_style)
        col += 1
        worksheet.write(row, col, dictOfPlayers[player]['galactic_power'],cell_format_style ) 
        col += 1
        for unit in unitsTuple:
            try:
                if getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) in ['13+8','13+9'] : 
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_blue)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) == '13+7' : 
                   worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_darkgreen)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) in ['13+4','13+5','13+6','13+3','13+2','13+1','13'] : 
                   worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_green)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) == '12': 
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_lightgreen)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) == '11': 
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit),cell_format_yellow)
                elif getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit) !=0 :
                    worksheet.write(row, col,  getStringOfGearAndRelic(dictOfPlayers=dictOfPlayers, player=player, unit=unit), cell_format_pink)
            except:
                worksheet.write(row, col, 'Нет', cell_format_pink)
            col += 1
        row += 1
        col=0
        worksheet.write_formula(row, col+1, '=sum(B2:B' + str(len(dictOfPlayers)+1) + ')', cell_format_style)

        
    workbook.close()


def getStringOfGearAndRelic(dictOfPlayers={}, player='', unit=''):
    gearLvl = dictOfPlayers[player]['units'][unit]['gear_level']
    if gearLvl == 13:
        return str(gearLvl) + '+' + str(dictOfPlayers[player]['units'][unit]['relic_tier'])
    else:
        stars = dictOfPlayers[player]['units'][unit]['stars']
        if stars == 7:
            return str(gearLvl)
        else:
            return str(gearLvl) + '(' + str(stars) +'*)'


def arrOfUnitsToDict(units=[]):  # Массив персонажей переделываем в словарь
    dictOfUnits = {}
    for unit in units:
        gearLvl = unit['data']['gear_level']
        lvlOfUnit = {}
        lvlOfUnit['gear_level'] = gearLvl
        lvlOfUnit['relic_tier'] = unit['data']['relic_tier']-2
        lvlOfUnit['stars'] = unit['data']['rarity']
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
