# -*- coding: utf-8 -*-
import os

#get and show the current work directory

print(os.getcwd())

My_Dir = os.path.join('D:\\','SandBox_Dev','Git','dev')
print(My_Dir)
os.chdir(My_Dir)
print(os.getcwd())


import random
capitals = {
        'Alabama': 'Montgomery', 
        'Alaska': 'Juneau', 
        'Arizona': 'Phoenix',
        'Arkansas': 'Little Rock',
        'California': 'Sacramento',
        'Colorado': 'Denver',
        'Connecticut': 'Hartford',
        'Delaware': 'Dover', 
        'Florida': 'Tallahassee',
        'Georgia': 'Atlanta', 
        'Hawaii': 'Honolulu', 
        'Idaho': 'Boise',
        'Illinois':'Springfield',
        'Indiana': 'Indianapolis',
        'Iowa': 'Des Moines',
        'Kansas': 'Topeka',
        'Kentucky': 'Frankfort',
        'Louisiana':'Baton Rouge',
        'Maine':'Augusta',
        'Maryland':'Annapolis',
        'Massachusetts':'Boston',
        'Michigan':'Lansing',
        'Minnesota':'Saint Paul',
        'Mississippi':'Jackson',
        'Missouri':'Jefferson City',
        'Montana': 'Helena',
        'Nebraska': 'Lincoln',
        'Nevada':'Carson City',
        'New Hampshire':'Concord',
        'New Jersey':'Trenton',
        'NewMexico':'Santa Fe',
        'New York':'Albany',
        'North Carolina':'Raleigh',
        'North Dakota':'Bismarck',
        'Ohio':'Columbus',
        'Oklahoma':'Oklahoma City',
        'Oregon':'Salem',
        'Pennsylvania':'Harrisburg', 
        'Rhode Island':'Providence',
        'South Carolina':'Columbia',
        'South Dakota':'Pierre',
        'Tennessee':'Nashville',
        'Texas':'Austin',
        'Utah':'Salt Lake City',
        'Vermont':'Montpelier',
        'Virginia':'Richmond',
        'Washington':'Olympia',
        'West Virginia':'Charleston',
        'Wisconsin':'Madison',
        'Wyoming': 'Cheyenne'
}

# Generate 35 quiz files.
for quizNum in range(35):
    quizFile = open('Capitalsquiz%s.txt' %(quiznumNum + 1),'w')
    answerKeyFile = open('Capitalsquiz_answers%s.txt' %(quiznumNum + 1),'w')

    #Write out the header for the quiz:
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capitals Quiz (From %s)' %(quizNum+1))
    quizFile.write('\n\n')

    #Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    
#Loop through all 50 states, making a question for each
for questionNum in range(50):
    #get right and wrong answers.
    correctAnswer = capitals[states[questionNum]]
    wrongAnswers = list(capitals.values())
    del wrongAnswers[wrongAnswers.index(correctAnswer)]
    wrongAnswers = random.sample(wrongAnswers,3)
    answerOptions = wrongAnswers + [correctAnswer]
    random.shuffle(answerOptions)




