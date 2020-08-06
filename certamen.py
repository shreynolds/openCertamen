begnames = ['ACTIUM', 'ATHENAE', 'AULIS', 'ALEXANDRIA', 'BEROLINUM', 'BRUNDISIUM', 'CANNAE', 'CARTHAGO', 'DELPHI', 'GENAVA', 'HERCULANEUM',
            'LONDINIUM', 'LUTETIA', 'OLYMPIA', 'OSTIA', 'POMPEII', 'ROMA', 'SPARTA','STABIAE', 'SYRACUSAE','THEBES','TIRYNS',
            'MYCENAE','ARGOS','CUMAE']
intnames = ['AEDUI', 'ALLOBROGES', 'AMBARRI', 'AMBIANI', 'AQUITANI', 'ATREBATES', 'ANDECAVI', 'ARVERNI', 'BELGAE', 'BELLOVACI',
            'BITURIGES', 'BOII', 'CARNUTES', 'CENOMANI', 'EBURONES', 'HELVETII', 'INSUBRES', 'LINGONES', 'MEDULLI', 'MENAPII',
            'MORINI', 'NERVII', 'PARISII', 'PICTONES', 'RAURICI', 'REMI', 'SALASSI', 'SANTONES', 'SEQUANI', 'TIGURINI', 'TREVERI',
            'TURONES', 'VENETI']
advnames = ['AHENOBARBI', 'CAESARES', 'DOLABELLAE', 'CINNAE', 'FLACCI', 'CORNELII', 'HIRTII', 'HORATII', 'HYGINI', 'IUVENALES',
            'LICINII', 'LIVII', 'LUCIANI', 'LUCRETII', 'MARTIALES', 'POLLIONES', 'MUMMII', 'OVIDII', 'PHAEDRI', 'PLAUTI', 'PROPERTII',
            'QUINTILIANI', 'SENECAE', 'SUETONII', 'TACITI', 'TERENTII', 'TIBULLI', 'VALERII', 'VARI', 'VARONES', 'VERGILII', 'VITRUVII',
            'SARDINIA', 'CORSICA', 'BITHYNIA', 'PONTUS']
names = dict()
names['beg'] = begnames
names['int'] = intnames
names['adv'] = advnames

totalrooms = ['room1', 'room2', 'room3', 'room4', 'room5', 'room6', 'room7', 'room8', 'room9', 'room10', 'room11',
              'room11', 'room12', 'room13', 'room14', 'room15', 'room16', 'room17', 'room18', 'room19', 'room20',
              'room21', 'room22', 'room23', 'room24', 'room25', 'room26', 'room27', 'room28', 'room29', 'room30']
level_rooms = dict()

__author__ = 'Sophie Reynolds'
import pandas as pd
import math
import random
from itertools import permutations

htmlwrite = ""

if __name__ == "__main__":
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    class People:
        def __init__(self, name, school):
            self.name = name
            self.school = school

        def toString(self):
            return self.name + " // " + self.school


    class Team(object):
        def __init__(self, name):
            self.list = []
            self.numPeople = 0
            self.schools = ""
            self.name = name

        def add(self, person):
            if self.numPeople < 4 and person.school not in self.schools:
                self.list.append(person)
                self.schools += person.school
                self.numPeople += 1
                return True
            else:
                return False

        def addIgnoreSchool(self, person):
            if self.numPeople < 4:
                self.list.append(person)
                self.numPeople += 1
                return True
            else:
                return False

        def toString(self):
            s = ""
            for person in self.list:
                s += person.name + " // " + person.school + "<br> \n"
            return s

        def toStringNoSchool(self):
            s = ""
            for person in self.list:
                s += "-- " + person.name + "<br> \n"
            return s



    # pandas imports the CSV as a Data Frame object
    total_responses = pd.read_csv("responses.csv")
    total_responses.drop_duplicates(subset=['Name'], inplace=True) #remove if people submitted twice
    beg = total_responses[total_responses.Level == "Beginner (MS1, MS2, HS1)"]
    int = total_responses[total_responses.Level == "Intermediate (MS3, HS2)"]
    adv = total_responses[total_responses.Level == "Advanced (HS3, HS-Adv)"]

    responses = dict()
    responses['beg'] = beg
    responses['int'] = int
    responses['adv'] = adv

    teams = dict()

    for type in ['beg', 'int', 'adv']:
        df = responses[type]
        num_teams = math.ceil(len(df) / 4)
        print(type)
        print(num_teams)
       #num_teams must be divisible by 3
        if num_teams%3 == 1:
            num_teams += 2
        elif num_teams%3 == 2:
            num_teams += 1
        print(num_teams)
        numrooms = num_teams / 3
        numrooms = math.floor(numrooms)
        level_rooms[type] = totalrooms[0:numrooms]
        totalrooms = totalrooms[numrooms:]
        peoplelist = []
        teamlist = []
        for i in range(len(df)):
            name = df.Name.iloc[i]
            school = df.School.iloc[i]
            person = People(name, school)
            peoplelist.append(person)

        random.shuffle(peoplelist)
        random.shuffle(names[type])
        for i in range(num_teams):
            name = names[type][i]
            teamlist.append(Team(name))

        for person in peoplelist:
            start_team = random.randint(0, num_teams - 1)
            team = start_team
            personAdded = False
            reachedStart = False
            while not personAdded:
                if team == start_team - 1:
                    reachedStart = True
                if not reachedStart:
                    personAdded = teamlist[team].add(person)
                else:
                    personAdded = teamlist[team - num_teams].addIgnoreSchool(person)
                if team < num_teams - 1:
                    team += 1
                else:
                    team = 0

        teams[type] = teamlist
        htmlwrite += "<h1>" + type + " teams </h1>"
        table = "<table> <tr>"
        counter = 0
        for i in range(len(teamlist)):
            table += "<td> <b>" + teamlist[i].name + "</b> <br>" + teamlist[i].toStringNoSchool() + "</td>"
            counter+=1
            if counter == 8:
                table += "</tr><tr>"
                counter = 0
        table += "</table>"

        htmlwrite += table


    #Teams are made -- now for the rooming assignments

"""
    for type in ['beg', 'int', 'adv']:
        teamList = teams[type]
        teamNameList = []
        for team in teamList:
            teamNameList.append(team.name)
        for round in [1, 2, 3]:
            print(type)
            print("Round " + str(round))
            print(teamNameList)
            random.shuffle(teamNameList)
            print(teamNameList)
            groups = list(chunks(teamNameList, 3))  #this works OK, but could come up with better math way
            for roomnum in range (0, len(level_rooms[type])):
                print(level_rooms[type][roomnum])
                print(groups[roomnum])

        #print(list(permutations(teamNameList)))
        """




    html_head = """<!DOCTYPE html> <html>
<head>
<title>Teams</title>
<style>
table, th, td {
  border: 3px solid black;
  border-collapse: collapse;
  padding: 15px;
}
td {
  width:12.5%;
}
</style>
</head>

<body>"""
    html_end = """</body>

</html>"""

    myfile = open("teams.html", "w")
    myfile.write(html_head + htmlwrite + html_end)
    myfile.close()
