import csv
from bodyFatEntry import bodyFatEntry
import datetime

def validateDate(date):
    if len(date[0]) != 2 or (int(date[0]) < 1 or  int(date[0]) > 31):
        return False
    
    if len(date[1]) != 2 or (int(date[1]) < 1 or  int(date[1]) > 12):
        return False

    if len(date[2]) != 4 or int(date[2]) < 2000:
        return False
    
    return True

def getDate():
    date = datetime.datetime.now()
    while True:
        userInput = input('Enter date (DD-MM-YYYY) or press T to get todays date: ')
        if userInput == 'T' or userInput =='t':
            break
        
        date = userInput.split('-')
        
        if(not validateDate(date)):
            print("Please enter date in correct format (DD-MM-YYYY)")
            continue

        date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        break

    return date.strftime("%d-%m-%Y")

def getMeasurement(bodyPart):
    ordinalNumbers = ['1st', '2nd', '3rd']

    measurement = 0
    for x in range(3):
        measurement += float(input(f'Enter {ordinalNumbers[x]} {bodyPart} measurement: '))
    print('\n')
    return measurement / 3

def readFile():
    entries = []
    try:
        with open("entries.csv") as stream:
            reader = csv.reader(stream)

            for row in reader:
                entries.append(bodyFatEntry(*row))
        entries = sorted(entries, key=lambda bodyFatEntry: bodyFatEntry.date)
    except FileNotFoundError:
        pass

    return entries

def writeToFile(entries):
    with open("entries.csv", "w", newline='') as stream:
        writer = csv.writer(stream)
        writer.writerows(entries)

def newEntry(entries):
    print('NEW ENTRY')
    date = getDate()
    age = input("Enter your age: ")
    weight = input("Enter your weight(kg): ")
    thigh = getMeasurement('Thigh')
    chest = getMeasurement('Chest')
    abs = getMeasurement('Abs')

    entries.append(bodyFatEntry(date, age, weight, thigh, chest, abs))
    return sorted(entries, key=lambda bodyFatEntry: bodyFatEntry.date)


def printEntryTable(entries):
    th = '{:<12}{:<5}{:<10}{:<10}{:<10}{:<10}{}'.format(
        'Date',
        'Age',
        'Weight',
        'Thigh',
        'Chest',
        'Abs',
        'BF%'
    )

    if (len(entries) == 0):
        print('\nNo entries found\n')
        return

    print(f'\n{th}')
    for entry in entries:
        print(entry)
    print('\n')

def mainMenu():
    while True:
        print('Main Menu')
        print('1. New Entry')
        print('2. See Entries')
        print('Q. Quit')
        
        userSelection = input('Selection: ')
        if userSelection == 'q' or userSelection == 'Q':
            return 'q'
        
        if userSelection != '1' and userSelection != '2':
            print('Please enter valid selection\n')
            continue
        
        return userSelection
    
def main():
    entries = readFile()
    
    print('********************************')
    print('Body Fat Percentage Tracker')
    print('********************************')
    selection = ''

    while selection != 'q':
        selection = mainMenu()

        if selection == '1':
            entries = newEntry(entries)
            writeToFile(entries)

        if selection == '2':
            printEntryTable(entries)

main()
