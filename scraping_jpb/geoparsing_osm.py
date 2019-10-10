from plpygis import Geometry
import csv

def converterGeometryPoint(geometry):
    g = Geometry(geometry)
    coord = g.geojson['coordinates']
    return [coord[1], coord[0]]

arq = csv.DictReader(open("./dados/features_campina_pt.csv", "r", encoding='utf-8'))

num = 5
for p in arq:
    if (num == 0):
        break
    coord = converterGeometryPoint(p['geometry'])
    print(coord)
    num -= 1