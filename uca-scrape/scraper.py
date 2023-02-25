#level.dept.number.name
#"undergrad"."CSCI".3381."Object-Oriented Software Development with Java"
 
import requests
from bs4 import BeautifulSoup
import re

class Course:
    dept:str
    number:str
    name:str
    desc:str
    reqs:list
    classification:str
    supertype:str
    credithours:str
    coreslist:list
    def __init__(self, dept: str, number: str, name: str, desc: str, reqs: list, cores:list) -> None:
        #String --> "CSCI", "MATH", etc
        self.dept = dept
        #String --> "3381", "2230", etc 
        self.number = number
        #String --> "OOSD w/ Java", "Discrete Math"
        self.name = name
        #String --> "You do stuff with Java", "You do stuff with Discrete Math"
        self.desc = desc
        #List of strings --> ["CSCI 1234", "MATH 1234"]
        self.reqs = reqs
        if " " in self.number:
            self.number = self.number[1:]
        if "U" in self.number:
            self.number = self.number[4:]
        if int(self.number[0]) == 1:
            self.classification = "freshman"
            self.supertype = "undergrad"
        elif int(self.number[0]) == 2:
            self.classification = "sophomore"
            self.supertype = "undergrad"
        elif int(self.number[0]) == 3:
            self.classification = "junior"
            self.supertype = "undergrad"
        elif int(self.number[0]) == 4:
            self.classification = "senior"
            self.supertype = "undergrad"
        elif int(self.number[0]) == 5 or int(self.number[0]) == 6:
            self.classification = "grad"
            self.supertype = "grad"
        elif int(self.number[0]) == 0:
            self.classification = "IEP"
            self.supertype = "IEP"
        if self.number[1] == "V":
            self.credithours = "variable"
        elif int(self.number[1]) == 1:
            self.credithours = "1"
        elif int(self.number[1]) == 2:
            self.credithours = "2"
        elif int(self.number[1]) == 3:
            self.credithours = "3"
        elif int(self.number[1]) == 4:
            self.credithours = "4"
        elif int(self.number[1]) == 5:
            self.credithours = "5"
        elif int(self.number[1]) == 6:
            self.credithours = "6"
        elif int(self.number[1]) == 7:
            self.credithours = "7"
        elif int(self.number[1]) == 8:
            self.credithours = "8"
        elif int(self.number[1]) == 9:
            self.credithours = "9"
        elif int(self.number[1]) == 0:
            self.credithours = "0"
        if type(cores) == list:
            for thing in cores:
                self.coreslist.append(thing)
        elif type(cores) == str:
            self.coreslist = []
            self.coreslist.append(cores)

class Directory:
    classes:list
    def __init__(self) -> None:
        self.classes = []
    def addCourse(self, Course):
        self.classes.append(Course)

def hasnum(thing: str):
    numstatus = False
    for thingthing in thing:
        if thingthing.isdigit():
            numstatus = True
    return numstatus

def scrape():

    UCA = Directory()

    #undergrad
    ubulletinmainURL = "https://uca.edu/ubulletin/courses/"
    ubulletinmain = requests.get(ubulletinmainURL)
    print("Got ubulletin")
    ubulletinsoup = BeautifulSoup(ubulletinmain.content, 'html5lib')
    print("Parsed ubulletin")
    ubpages = []

    for link in ubulletinsoup.findAll('a', attrs={'href': re.compile("^http://uca.edu")}):
        if "http://uca.edu/ubulletin/courses/" in link.get('href'):
            ubpages.append(link.get('href'))

    del ubpages[0]

    for pageurl in ubpages:
        instance = requests.get(pageurl)
        instancesoup = BeautifulSoup(instance.content, 'html5lib')
        print("Got " + instancesoup.title.string)
        title = instancesoup.find(class_="entry-title")
        if "(" in repr(title):
            start = repr(title).index('(')
            end = repr(title).index(')', start+1)
            deptstring = repr(title)[start+1:end]
        else: deptstring = "RADG"
        main = instancesoup.find(class_="entry-content")
        #For each Course, we need to get the: number, name, description, cores, prereqs (classification, supertype, and classification can be calculated afterwards)
        for classtag in main.children:
            if "<strong>" not in repr(classtag) or "<strong>\xa0</strong>" in repr(classtag) or "<em>" in repr(classtag) or "<h2" in repr(classtag) or "th-box info" in repr(classtag) or hasnum(repr(classtag)) is False:
                continue
            start2 = repr(classtag).find("<strong>") + len("<strong>")
            end2 = repr(classtag).find("</strong>")
            substring = repr(classtag)[start2:end2]
            number = substring[0:4]
            name = substring[5:]
            if "[UD UCA Core:" in repr(classtag):
                corestart = repr(classtag).find("[UD UCA Core:") + len("[UD UCA Core:")
                coreend = repr(classtag).find("]")
                cores = repr(classtag)[corestart:coreend]
                if "," in cores:
                    cores.split(",")
                    for thing in cores:
                        thing = "UD " + cores
                cores = "UD " + cores
            elif "[LD UCA Core:" in repr(classtag):
                corestart = repr(classtag).find("[LD UCA Core:") + len("[LD UCA Core:")
                coreend = repr(classtag).find("]")
                cores = repr(classtag)[corestart:coreend]
                if "," in cores:
                    cores.split(",")
                    for thing in cores:
                        thing = "LD " + cores
                cores = "LD " + cores
            else: cores = "none"
            if "Prerequisite:" in repr(classtag):
                prestart = repr(classtag).find("Prerequisite:") + len("Prerequisite:")
                if "[" in repr(classtag):
                    preend = repr(classtag).find("[")
                else: preend = repr(classtag).find("</p>")
                reqlist = repr(classtag)[prestart:preend]
            elif "Prerequisites:" in repr(classtag):
                prestart = repr(classtag).find("Prerequisites:") + len("Prerequisites:")
                if "[" in repr(classtag):
                    preend = repr(classtag).find("[")
                else: preend = repr(classtag).find("</p>")
                reqlist = repr(classtag)[prestart:preend]
            else: reqlist = "none"
            start3 = repr(classtag).find("</strong>") + len("</strong>")
            if "Prerequisite" not in repr(classtag) and "[" in repr(classtag):
                end3 = repr(classtag).find("[")
            elif "Prerequisite" in repr(classtag):
                end3 = repr(classtag).find("Prerequisite")
            end3 = repr(classtag).find("</p>")
            description = repr(classtag)[start3:end3]
            newclass = Course(deptstring, number, name, description, reqlist, cores)
            UCA.addCourse(newclass)
            print("Adding " + newclass.dept + " " + newclass.number + " - " + newclass.name + ": " +  "classification is " + newclass.classification + ", supertype is " + newclass.supertype + ", credit hours are " + newclass.credithours + ", prereqs are " + newclass.reqs)

            
    #grad
    gbulletinmainURL = "https://uca.edu/gbulletin/courses/"
    gbulletinmain = requests.get(gbulletinmainURL)
    print("Got gbulletin")
    gbulletinsoup = BeautifulSoup(gbulletinmain.content, 'html5lib')
    print("Parsed gbulletin")
    gbpages = []

    for link in gbulletinsoup.findAll('a', attrs={'href': re.compile("^http://uca.edu")}):
        if "http://uca.edu/gbulletin/courses/" in link.get('href'):
            gbpages.append(link.get('href'))

    for pageurl in gbpages:
        instance = requests.get(pageurl)
        instancesoup = BeautifulSoup(instance.content, 'html5lib')
        print("Got " + instancesoup.title.string)

print("\n\nSTARTING\n\n")
scrape()
print("\n\nSTOPPING\n\n")