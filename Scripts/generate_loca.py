languages = ["Spanish", "English", "EnglishUS", "French", "Italian", "German", "Chinese"]

def getLanguagesHeader():
    strLang = "Key,"
    for language in languages:
        strLang = strLang + language + ","
    return strLang[:-1] + "\n"
    
def getMenuLanguagesHeader():
    menuLanguages = ["English", "Spanish", "EnglishUS", "French", "Italian", "German", "Chinese"]
    strLang = ""
    for language in menuLanguages:
        strLang = strLang + language + ","
    return strLang[:-1] + "\n"

######################### MENU #########################
texts = {}
f = open("../../Localization/menu.csv", "w")
f.write(getMenuLanguagesHeader())
for language in languages:
    if language != "English":
        menu = {}
        execfile("../../DATA/Menu/" + language + ".py")
        texts[language] = ForeingDict

for key in texts[languages[0]].keys():
    text = ''
    for language in languages:
        if language != "English":
            if key in texts[language].keys():
                text = text + ',"' + texts[language][key] + '"'
            else:
                text = text + ','
    f.write('"' + key + '"' + text + '\n')

######################### LEVELS #########################
for i in range(1, 18):
    f=open("../../Localization/M" + str(i) + ".csv", "w")
    texts = {}
    f.write(getLanguagesHeader())
    for language in languages:
        Textos = {}
        execfile("../../DATA/Text/"+ language + "/M" + str(i) + ".py")
        texts[language] = Textos
    
    for key in texts[languages[0]].keys():
        text = ''
        for language in languages:
            if texts[language].has_key(key):
                currentText = texts[language][key][4]
                currentText = string.replace(currentText, '"', '')
                text = text + '"' + currentText + '",'
            else:
                text = text + ','
        f.write(key + ',' + text + '\n')
    f.close()
    
######################### Tutor #########################
f=open("../../Localization/tutor.csv", "w")
texts = {}
f.write(getLanguagesHeader())
for language in languages:
    Textos = {}
    execfile("../../DATA/Text/"+ language + "/tutor.py")
    texts[language] = Textos
    
for key in texts[languages[0]].keys():
    text = ''
    for language in languages:
        if texts[language].has_key(key):
            currentText = texts[language][key]
            sentences = ""
            for sentence in currentText:
                sentences = sentences + sentence + '\n'
            text = text + '"' + sentences[:-1] + '",'
        else:
            text = text + ','
    f.write(key + ',' + text + '\n')
f.close()

######################### ObjIds #########################
texts = {}
f=open("../../Localization/objIds.csv", "w")
f.write(getLanguagesHeader())
for language in languages:
    execfile("../../DATA/ObjIds/" + language +".py")
    texts[language] = Reference.DefaultSelectionData
    Reference.DefaultSelectionData = {}
for key in texts[languages[0]].keys():
    text = ''
    for language in languages:
        text = text + "," + texts[language][key][2]
    f.write(key + text + "\n")
f.close()

######################### Combos #########################
def resetArray():
    return  {
              "Knight_N"   : {},
              "Barbarian_N": {},
              "Amazon_N"   : {},
              "Dwarf_N"    : {},
              "Default"    : {},
            }

texts = {}
f=open("../../Localization/combos.csv", "w")
f.write(getLanguagesHeader())
for language in languages:
    ComboNames = resetArray()
    execfile("../../DATA/Text/" + language + "/Combos.py")
    texts[language] = ComboNames

for key in texts[languages[0]].keys():
    for key2 in texts[languages[0]][key].keys():
        text = ''
        for language in languages:
            text = text + "," + texts[language][key][key2]
        f.write(key + " " + key2 + text + "\n")
f.close()

######################### Casa #########################
characters = ["Bar", "Kgt", "Amz", "Dwf"]

def fillData():
    data = {}
    for char in characters:
        for i in range(1, 5):
            data[('TextInfoChar' + char + str(i))] = globals()['TextInfoChar' + char + str(i)]
    return data

f=open("../../Localization/casa.csv", "w")
f.write(getLanguagesHeader())
texts = {}
for language in languages:
    execfile("../../DATA/Text/" + language + "/casa.py")
    texts[language] = fillData()

for key in texts[languages[0]].keys():
    text = ''
    for language in languages:
        text = text + texts[language][key] + '","'
    text = text[:-3]
    f.write(key + ',"' + text + '"\n')
f.close()

######################### map2D #########################
levels = ["Monolith", "MONOLITH", "Tabriz", "TABRIZ", "Khazel", "KHAZEL", "Marakamda", "MARAKAMDA", "MINE", "Mine", "TellHa", "TELLHA", "QUEENST", "QueensT", "Karum", "KARUM", "SHALATUWAR", "Shalatuwar", "ORLOK", "Orlok", "NEMRUT", "Nemrut", "NEJEV", "Nejev", "ALFARUM", "Alfarum", "XATHRA", "Xathra", "Ianna", "IANNA", "DALGURAK", "DalGurak", "CHAOS", "Chaos"]

def fillData2Dmap():
    data = {}
    for level in levels:
        data[level] = globals()[level]
    return data

f=open("../../Localization/map2D.csv", "w")
f.write(getLanguagesHeader())
texts = {}
for language in languages:
    MapList = {}
    execfile("../../DATA/Text/" + language + "/map2D.py")
    texts[language] = fillData2Dmap()

for key in texts[languages[0]].keys():
    text = ''
    for language in languages:
        text = text + texts[language][key] + '","'
    text = text[:-3]
    f.write(key + ',"' + text + '"\n')
f.close()
