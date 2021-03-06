import requests
from recs_tmdb import get_rec_tv

def create_csv():
    '''
        Initializes the csv to the correct format for future parsing
    '''
    fields=""
    fields+="title,"
    for i in range(1,6):
        if(i!=5):
            fields+=(f"rec{i},")
        else:
            fields+=(f"rec{i}\n")
    fp=open("utils/recs.csv","w")
    fp.write(fields)
    fp.close()
def append_csv(title,recs):
    '''
        Writes the titles and the corresponing recommendations to the csv file

            Parameters:
                title(string) : Title of show
                recs(list of strings) : The recommendations for that show
    '''
    recstring=f"{title},"
    for rec in recs:
        recstring+=rec+","
    recstring=recstring[:len(recstring)-1]+"\n"
    fp=open('utils/recs.csv',"a")
    fp.write(recstring)
    fp.close()

if __name__ == '__main__':
    create_csv()
    '''
        After initalizing the csv this script will read the list of titles
        from data.txt. It will then get all the titles from the list
        and find recommendations for those title within the given list
    '''
    data=open("utils/data.txt","r")
    titles=data.read().splitlines()
    addt=set()
    for title in titles:
        recs=get_rec_tv(title)
        if recs:
            tbr=[]
            for rec in recs:
                if rec not in titles:
                    tbr.append(rec)
                    addt.add(rec)
            for r in tbr:
                recs.remove(r)
            if len(recs)!=0:
                append_csv(title.replace(",",""),recs)
