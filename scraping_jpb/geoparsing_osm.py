from plpygis import Geometry
import csv

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

def polygons(cidade="cg"):
	if (cidade == "cg"):
		arq = csv.DictReader(open("./dados/features_campina_ln.csv", "r", encoding='utf-8'))
	elif (cidade == "jp"):
		arq = csv.DictReader(open("./dados/features_jp_ln.csv", "r", encoding='utf-8'))
	elif (cidade == "pb"):
		arq = csv.DictReader(open("./dados/features_paraiba_ln.csv", "r", encoding='utf-8'))
	
	fields = ["osm_id", "fclass", "name", "type", "coordenates"]
	f = csv.writer(open('./processamento/gazetteer/'+ cidade + '_ln.csv', 'w', encoding='utf-8'))
	f.writerow(fields)

	for p in arq:
		coord = converterGeometryPolygon(p['geometry'])
		t = [ p['osm_id'].__str__(), p["fclass"].__str__(), p["name"].__str__(), p["type"].__str__(), coord ]
		f.writerow(t)

def points(cidade="cg"):
	if (cidade == "cg"):
		arq = csv.DictReader(open("./dados/features_campina_pt.csv", "r", encoding='utf-8'))
	elif (cidade == "jp"):
		arq = csv.DictReader(open("./dados/features_jp_pt.csv", "r", encoding='utf-8'))
	elif (cidade == "pb"):
		arq = csv.DictReader(open("./dados/features_paraiba_pt.csv", "r", encoding='utf-8'))

	fields = ["osm_id", "fclass", "name", "type", "coordenates"]
	f = csv.writer(open('./processamento/gazetteer/' + cidade + '_pt.csv', 'w', encoding='utf-8'))
	f.writerow(fields)

	for p in arq:
		coord = converterGeometryPoint(p['geometry'])
		t = [ p['osm_id'].__str__(), p["fclass"].__str__(), p["name"].__str__(), p["type"].__str__(), coord ]
		f.writerow(t)

polygons(cidade="pb")