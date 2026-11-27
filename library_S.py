import json
def import_json(fname):
	f = open(fname,"rt",encoding = "utf-8")
	data = json.load(fname)
	print(len(data))


