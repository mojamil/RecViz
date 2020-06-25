import imdb
from fetch_list import get_list
import sys
def write2file(l):
    fp=open("utils/data.txt",'w')
    for entry in l:
        fp.write(entry+"\n")
    fp.close()

def pop_list():
    ia=imdb.IMDb()
    pop=ia.get_popular100_tv()[:100]
    poptitles=[pop[i]['title'] for i in range(0,len(pop))]
    return poptitles
def fetch_list(listid):
    if(listid=="popular"):
        return pop_list()
    else:
        return get_list(listid)
if __name__ == '__main__':
    titles=fetch_list(sys.argv[1])
    while len(titles)==0:
        print("List id invalid")
        input("Enter valid list id")
    write2file(titles)