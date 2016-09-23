from flask import Flask, render_template
import random
import csv 

hi = open("occupations.csv", "rb")
reader = csv.reader(hi)
dic = {}
L = []

def listify(L, readin):
    for occupation in readin:
        L.append(occupation)
    return L[1:len(L)-1]

def addToDict(L,D):
    for item in L:
        D[item[0]] = int(float(item[1]) * 10)
    return D


#out of 998
def modList(dic):
    master = []
    for key in dic:
         master += [key]*dic[key]
    return master

def randomizer(alist):
    random.shuffle(alist)
    #this is optional because the chances dont change but it does increase randomness
    return alist[random.randint(0,len(alist)-1)] 

L = listify(L,reader)
dic = addToDict(L, dic)

#=========================================FLASK STUFF================================
app = Flask(__name__) #create Flask object

@app.route("/") #assign following fxn to run when root route requested
def hello_world():
    return "I don't speak Cheese or Spanish!"

khal = [0,1,1,2,3,5,8]

@app.route("/occupations")
def test_tmplt():
    return render_template( 'occu-table.html', heading="Occupations", 
    	paragraph="Occupations that you may or may not want to join and some numbers you may or may not want to see", 
    	collection=L, 
    	warning="Warning: by generating an occupation, you waive your right to sue Occu-table Corporations for any debt, divorces, and family destruction.",
    	generate="You're destined to work in " + randomizer(modList(dic)))
    
if __name__ == "__main__":
    #enable debugging, auto-restarting of server when this file is modified
    #app.debug = True 
    app.run()