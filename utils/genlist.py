import imdb
from fetch_list import get_list
def write2file(l):
    fp=open("data.txt",'w')
    for entry in l:
        fp.write(entry+"\n")
    fp.close()

def pop_list():
    ia=imdb.IMDb()
    pop=ia.get_popular100_tv()[:100]
    poptitles=[pop[i]['title'] for i in range(0,len(pop))]
    return poptitles
def fetch_list(listid):
    if(list==None):
        return pop_list
    else:
        return get_list(listid)
if __name__ == '__main__':
    write2file(fetch_list("ls095964455"))