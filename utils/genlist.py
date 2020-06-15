import imdb
def write2file(l):
    fp=open("data.txt",'w')
    for entry in l:
        fp.write(entry+"\n")
    fp.close()

def fetch_list():
    ia=imdb.IMDb()
    pop=ia.get_popular100_tv()
    poptitles=[pop[i]['title'] for i in range(0,len(pop))]
    return poptitles

if __name__ == '__main__':
    write2file(fetch_list())