
def safe_add(container, value):
	if value != "" and value[-1] == '\r':
		value = value[:-1]

	container.append(value)

def parse(filepath):
	f = open(filepath, "r")
	content=f.read()
	f.close()
	content_len = len(content)
	i = 0
	entries = []
	entry = []
	value = ""
	quoting = 0
	while i < content_len:
		char = content[i]
		i = i + 1

		if quoting:
			if char == '"':
				quoting = 0
			else:
				value = value + char
		else:
			if char == '"':
				quoting = 1
			elif char == ',':
				safe_add(entry, value)
				value = ""
			elif char == '\n':
				safe_add(entry, value)
				value = ""
				entries.append(entry)
				entry = []
			else:
				value = value + char

	if value != "":
		safe_add(entry, value)
		entries.append(entry)

	return entries
