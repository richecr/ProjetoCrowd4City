from plpygis import Geometry
import csv
import sys

# Aumentando o tamanho limite do csv.
maxInt = sys.maxsize
csv.field_size_limit(maxInt)

def converterGeometryPoint(geometry):
	g = Geometry(geometry)
	coord = g.geojson['coordinates']
	coord.reverse()
	return coord

def converterGeometryPolygon(geometry):
	g = Geometry(geometry)
	coord = g.geojson['coordinates']
	saida = []
	for c in coord[0]:
		c.reverse()
		saida.append(c)
	return saida

def converterFeature(geometry):
	g = Geometry(geometry)
	coord = g.geojson['coordinates'][0][0]
	saida = []
	for c in coord:
		c.reverse()
		saida.append(c)
	return saida

def polygons(localidade="cg"):
	if (localidade == "cg"):
		arq = csv.DictReader(open("./dados/features_campina_ln.csv", "r", encoding='utf-8'))
	elif (localidade == "jp"):
		arq = csv.DictReader(open("./dados/features_jp_ln.csv", "r", encoding='utf-8'))
	elif (localidade == "pb"):
		arq = csv.DictReader(open("./dados/features_paraiba_ln.csv", "r", encoding='utf-8'))
	
	fields = ["osm_id", "fclass", "name", "type", "coordenates"]
	f = csv.writer(open('./processamento/gazetteer/'+ localidade + '_ln.csv', 'w', encoding='utf-8'))
	f.writerow(fields)

	for p in arq:
		coord = converterGeometryPolygon(p['geometry'])
		t = [ p['osm_id'].__str__(), p["fclass"].__str__(), p["name"].__str__(), p["type"].__str__(), coord ]
		f.writerow(t)

def points(localidade="cg"):
	if (localidade == "cg"):
		arq = csv.DictReader(open("./dados/features_campina_pt.csv", "r", encoding='utf-8'))
	elif (localidade == "jp"):
		arq = csv.DictReader(open("./dados/features_jp_pt.csv", "r", encoding='utf-8'))
	elif (localidade == "pb"):
		arq = csv.DictReader(open("./dados/features_paraiba_pt.csv", "r", encoding='utf-8'))

	fields = ["osm_id", "fclass", "name", "type", "coordenates"]
	f = csv.writer(open('./processamento/gazetteer/' + localidade + '_pt.csv', 'w', encoding='utf-8'))
	f.writerow(fields)

	for p in arq:
		coord = converterGeometryPoint(p['geometry'])
		t = [ p['osm_id'].__str__(), p["fclass"].__str__(), p["name"].__str__(), p["type"].__str__(), coord ]
		f.writerow(t)

def features(localidade="cg"):
	if (localidade == "cg"):
		arq = csv.DictReader(open("./dados/features_campina.csv", mode="r"))
	elif (localidade == "jp"):
		arq = csv.DictReader(open("./dados/features_jp.csv", mode="r"))
	elif (localidade == "pb"):
		arq = csv.DictReader(open("./dados/features_paraiba.csv", mode="r"))
	
	fields = ["osm_id", "fclass", "name", "type", "coordenates"]
	f = csv.writer(open('./processamento/gazetteer/' + localidade + '.csv', 'w', encoding='utf-8'))
	f.writerow(fields)

	for p in arq:
		coord = converterFeature(p['geometry'])
		t = [ p['osm_id'].__str__(), p["fclass"].__str__(), p["name"].__str__(), p["type"].__str__(), coord ]
		f.writerow(t)

points(localidade="pb")