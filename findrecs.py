import requests

def get_recs(title,key):
    r=requests.get(f"https://tastedive.com/api/similar?q=show:{title}&k={key}")
    results=r.json()["Similar"]["Results"]
    recs=[]
    maxl=10
    if(len(results)<10):
        maxl=len(results)
    for i in range(0,maxl):
        name=results[i]['Name']
        recs.append(name)
    return recs


def create_csv():
    fields=""
    fields+="title,"
    for i in range(1,11):
        if(i!=10):
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
        recs=get_recs(title,"373322-DiRecTre-D1E4Z4FG")
        if(len(recs)>0):
            append_csv(title,recs)
