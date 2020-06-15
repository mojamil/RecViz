import requests
from recs_tmdb import get_rec

def create_csv():
    fields=""
    fields+="title,"
    for i in range(1,6):
        if(i!=5):
            fields+=(f"rec{i},")
        else:
            fields+=(f"rec{i}\n")
    fp=open("recs.csv","w")
    fp.write(fields)
    fp.close()
def append_csv(title,recs):
    recstring=f"{title},"
    for rec in recs:
        recstring+=rec+","
    recstring=recstring[:len(recstring)-1]+"\n"
    fp=open('recs.csv',"a")
    fp.write(recstring)
    fp.close()

if __name__ == '__main__':
    create_csv()
    data=open("data.txt","r")
    titles=data.read().splitlines()
    for title in titles:
        recs=get_rec(title)
        tbr=[]
        for rec in recs:
            if rec not in titles:
                tbr.append(rec)
        for r in tbr:
            recs.remove(r)
        if(len(recs)>0):
            append_csv(title,recs)
