import csv
import string
import Bladex
import sys
import os
import Reference

# The CSV must have the first line containing the language names
# Set the desired language here:
languages = ["Spanish", "English", "EnglishUS", "French", "Italian", "German", "Russian", "Chinese"]

LanguageToImport = "undefined"

def get_entry_from_key(content, key):
	for entry in content:
		if entry[0] == key:
			return entry

	return None

def generate_menu():
	print LanguageToImport
	if LanguageToImport == "English":
		return
	content = csv.parse("../../Localization/menu.csv")
	output_file=open("../../Data/Menu/" + LanguageToImport + "_.py", "w")
	language_column_index = content[0].index(LanguageToImport)
	output_file.write("ForeingDict = {\n")

	for entry in content:
		output_file.write("    \"" + entry[0] + "\" : \"" + entry[language_column_index] + "\",\n")

	output_file.write("}")
	output_file.close()

def generate_tutor():
	content = csv.parse("../../Localization/tutor.csv")
	Textos = {}
	execfile("../../Data/Text/EnglishUS/tutor.py")
	original_content = Textos
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/tutor.py", "w")
	language_column_index = content[0].index(LanguageToImport)

	for key in original_content.keys():
		entry = get_entry_from_key(content, key)
		if entry == None:
			print "Warning: Missing key " + key
		else:
			translation = entry[language_column_index]
			lines = string.split(translation, "\n")
			output_file.write("Textos['" + key + "'] = (\n")

			for line in lines:
				output_file.write("\t\"" + line + "\",\n")

			output_file.write(")\n")

	output_file.close()

def generate_objIds():
	content = csv.parse("../../Localization/objIds.csv")
	Reference.DefaultSelectionData = {}
	execfile("../../Data/ObjIds/EnglishUS.py")
	original_content = Reference.DefaultSelectionData
	output_file=open("../../Data/ObjIds/" + LanguageToImport + ".py", "w")
	language_column_index = content[0].index(LanguageToImport)

	for key in original_content.keys():
		entry = get_entry_from_key(content, key)
		if entry == None:
			print "Warning: Missing key " + key
		else:
			translation = entry[language_column_index]
			lines = string.split(translation, "\n")
			output_file.write("Reference.DefaultSelectionData['" + key + "'] = (" + str(original_content[key][0]) + "," + str(original_content[key][1]) + ",\"" + translation + "\")\n")

	output_file.close()

def generate_m(index):
	index = str(index)
	content = csv.parse("../../Localization/M" + index + ".csv")
	Textos = {}
	execfile("../../Data/Text/EnglishUS/M" + index + ".py")
	original_content = Textos
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/M" + index + ".py", "w")
	language_column_index = content[0].index(LanguageToImport)

	for key in original_content.keys():
		value = original_content[key]
		entry = get_entry_from_key(content, key)
		if entry == None:
			print "Warning: Missing key " + key
		else:
			translation = entry[language_column_index]
			output_file.write("Textos['" + key + "'] = (" + str(value[0]) + ",\n")
			output_file.write("\t" + str(value[1]) + "," + str(value[2]) + "," + str(value[3]) + ",\n")
			converted_value = string.replace(entry[language_column_index], "\n", "\\n")
			output_file.write("\t\"\"\"" + converted_value + "\"\"\"\n")
			output_file.write(")\n\n")

	output_file.close()


def generate_all_m():
	for i in range(1, 18):
		generate_m(i)


def generate_map2d():
	content = csv.parse("../../Localization/map2D.csv")
	MapList = {}
	execfile("../../Data/Text/EnglishUS/map2D.py")
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/map2D.py", "w")
	language_column_index = content[0].index(LanguageToImport)

	for entry in content:
		key = entry[0]
		translation = entry[language_column_index]
		output_file.write(key + " = \"" + translation + "\"\n")

	output_file.write("\n\n")
	output_file.write("# DO NOT COMMIT THIS!\n")
	output_file.write("# YOU HAVE TO COPY THE MapList TABLE HERE\n")

	output_file.close()

def generate_combos():
	content = csv.parse("../../Localization/combos.csv")
	ComboNames = {
              "Knight_N"   : {},
              "Barbarian_N": {},
              "Amazon_N"   : {},
              "Dwarf_N"    : {},
              "Default"    : {},
            }
	execfile("../../Data/Text/EnglishUS/Combos.py")
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/Combos.py", "w")
	language_column_index = content[0].index(LanguageToImport)
	original_content = ComboNames

	for key in original_content.keys():
		for key2 in original_content[key].keys():
			entry = get_entry_from_key(content, key + " " + key2)
			if entry == None:
				print "Warning: Missing key " + key
			else:
				translation = entry[language_column_index]
				output_file.write("ComboNames['" + key + "']['" + key2 + "']" + " = \"" + translation + "\"\n")

	output_file.close()


def generate_casa():
	content = csv.parse("../../Localization/casa.csv")
	execfile("../../Data/Text/EnglishUS/casa.py")
	try:
		os.mkdir("../../Data/Text/" + LanguageToImport)
	except:
		pass
	output_file=open("../../Data/Text/" + LanguageToImport + "/casa.py", "w")
	language_column_index = content[0].index(LanguageToImport)

	chars = ["Bar", "Kgt", "Amz", "Dwf" ]

	for char in chars:
		for i in range(1, 5):
			key = "TextInfoChar" + char + str(i)
			entry = get_entry_from_key(content, key)
			translation = entry[language_column_index]
			output_file.write(key + " = \"\"\"" + translation + "\"\"\"\n")

	output_file.close()


for language in languages:
	global LanguageToImport
	LanguageToImport = language
	generate_objIds()
	# generate_menu()
	# generate_tutor()
	# generate_all_m()
	# generate_map2d()
	# generate_casa()
	# generate_combos()


sys.exit(0)
