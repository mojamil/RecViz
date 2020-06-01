import csv
import json
def get_vertices():
    vertices={}
    fil=open("recs.csv","r")
    data=csv.DictReader(fil)
    for row in data:
        if row["title"] not in vertices.keys():
            vertices[row["title"]]=set()
        for entry in row.values():
            if entry!=row["title"] and entry !=None:
                vertices[row["title"]].add(entry)
                if entry in vertices.keys():
                    vertices[entry].add(row["title"])
                else:
                    vertices[entry]=set([row["title"]])
    for vertice in vertices.keys():
        vertices[vertice]=list(vertices[vertice])
    fil.close()
    return vertices
if __name__ == '__main__':
    out=json.dumps(get_vertices(),indent=4)
    jsonf=open("graph.json","w")
    jsonf.write(out)
    jsonf.close()
