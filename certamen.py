
__author__ = 'Sophie Reynolds'
import pandas as pd
import math
import random

if __name__ == "__main__":
    class People:
        def __init__(self, name, school):
            self.name = name
            self.school = school

        def toString(self):
            return self.name + " // " + self.school


    class Team(object):
        def __init__(self):
            self.list = []
            self.numPeople = 0
            self.schools = ""

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
                s += person.name + " // " + person.school + "\n"
            return s


    # pandas imports the CSV as a Data Frame object
    total_responses = pd.read_csv("responses.csv")
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
        peoplelist = []
        teamlist = []
        for i in range(len(df)):
            name = df.Name.iloc[i]
            school = df.School.iloc[i]
            person = People(name, school)
            peoplelist.append(person)

        random.shuffle(peoplelist)

        for i in range(num_teams):
            teamlist.append(Team())

        for person in peoplelist:
            team = 0
            personAdded = False;
            while not personAdded:
                if team < num_teams:
                    personAdded = teamlist[team].add(person)
                else:
                    personAdded = teamlist[team - num_teams].addIgnoreSchool(person)
                team += 1
        teams[type] = teamlist
        for i in range(len(teamlist)):
            print(type + " level, team number: " + str(i + 1))
            print(teamlist[i].toString());