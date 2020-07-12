import imdb
from fetch_list import get_list
import sys
def write2file(l):
    '''
        Writes a list to data.txt
        
            Parameter:
                l(list): The elements of this list are written to data.txt separated by newlines
    '''
    fp=open("utils/data.txt",'w')
    for entry in l:
        fp.write(entry+"\n")
    fp.close()

def pop_list():
    '''
        Uses imdbpy package to get the 100 most popular shows on imdb
        to use as the default list of data.

            Return:
                poptitles(list of strings): List containing the titles of the 100 most popular shows on imdb
    '''
    ia=imdb.IMDb()
    pop=ia.get_popular100_tv()[:100]
    poptitles=[pop[i]['title'] for i in range(0,len(pop))]
    return poptitles
def fetch_list(listid):
    '''
        Returns list of titles depending on user input

            Parameters:
                listid(string): The id of an imdb list / or the popular keyword to get the default data

            Returns:
                pop_list(): The return value of the pop_list() function
                or 
                get_list(listid): The return value of the get_list function given the parameter listid

    '''
    if(listid=="popular"):
        return pop_list()
    else:
        return get_list(listid)
if __name__ == '__main__':
    '''
        The main function takes the command line argument to create 
        a list in data.txt if the list id is invalid it will ask for data again
    '''
    titles=fetch_list(sys.argv[1])
    while len(titles)==0:
        print("List id invalid")
        input("Enter valid list id")
    write2file(titles)