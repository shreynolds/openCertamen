__author__ = 'Sophie Reynolds'
import pandas as pd
import math
import random



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

rostra = dict()
rostra[12] = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [11, 8, 5, 2, 10, 7, 4, 1, 9, 6, 3, 0], [3, 7, 10, 6, 9, 0, 2, 5, 11, 1, 4, 8])
rostra[9] = ([0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 3, 6, 2, 5, 8, 1, 4, 7], [1, 5, 6, 2, 3, 7, 0, 4, 8])
rostra[18] = ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], [1, 3, 17, 2, 4, 6, 5, 7, 9, 8, 10, 12, 11, 13, 15, 0, 14, 16],
              [4, 9, 17, 5, 10, 15, 0, 8, 13, 2, 7, 12, 3, 11, 16, 1, 6, 14])

outputtext = dict()
outputtext['beg'] = ""
outputtext['int'] = ""
outputtext['adv'] = ""

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

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
            try:
                teamlist.append(Team(alphabet[i] + ":&nbsp" + name))
            except IndexError:
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
        outputtext[type] += "<h1>" + type + " teams </h1>"
        table = "<table> <tr>"
        counter = 0
        for i in range(len(teamlist)):
            table += "<td> <b>" + teamlist[i].name + "</b> <br>" + teamlist[i].toStringNoSchool() + "</td>"
            counter+=1
            if counter == 3:
                table += "</tr><tr>"
                counter = 0
        table += "</table>"

        outputtext[type] += table
        outputtext[type] += "<br> <br>"

    for type in ['beg', 'int', 'adv']:
        print(type)
        outputtext[type] += "<h1>" + type + " rooms </h1> <br>"
        teamlist = teams[type]
        rooms = level_rooms[type]
        try:
            roster = rostra[len(teamlist)]
        except:
            outputtext[type] += "This number of teams does not have a set rotation, sorry!"
            break
        table = "<table> <tr> <td> Round </td>"
        for roomnum in range(0, len(rooms)):
            table += "<td>" + rooms[roomnum] + "</td>"
        table += "</tr>"
        for round in [1, 2, 3]:
            table += "<tr> <td>" + str(round) + "</td>"
            print("Round " + str(round))
            groups = list(chunks(roster[round-1], 3))
            for roomnum in range (0, len(rooms)) :
                teamNums = groups[roomnum]
                table += "<td>" + teamlist[teamNums[0]].name + "<br>" + teamlist[teamNums[1]].name + "<br>" + teamlist[teamNums[2]].name + "</td>"
            table += "</tr>"
        outputtext[type] += table




    html_head = """<!DOCTYPE html> <html>
<head>
<title>Teams</title>
<style>
table, th, td {
  border: 3px solid black;
  border-collapse: collapse;
  padding: 15px;
}
table{
width: 50%;
}
</style>
</head>

<body>"""
    html_end = """</body>

</html>"""
    for type in ['beg', 'int', 'adv']:
        filename = type + ".html"
        myfile = open(filename, "w")
        myfile.write(html_head + outputtext[type] + html_end)
        myfile.close()
