#Donald Snyder 1/26/24 SDEV 220
#Gradebook
#This program will accept a student's name and GPA and test if the
#student qualifies for the Dean's List or the Honor Roll

#These are the global variables
studentName = ""
studentGPA = 0.000
honorRoll = 3.25
deanList = 3.5



#This houses the loop
if __name__ == '__main__':
    
    #This series of if else/while loops gather the input then tell the user the results until
    #the user enters the quit command
    studentName = input("\nEnter the student's name or ZZZ to quit: ")
    while studentName != "ZZZ":
        studentGPA = float(input("\nEnter the student's GPA to see if the student qualifies for the Honor Roll or Dean's List: "))
        if studentGPA >= deanList:
            print(f'\n{studentName} made the Deans List.')
        else:
            if studentGPA >= honorRoll:
                print(f'\n{studentName} made the Honor Roll.')
            else:
                print(f'\n{studentName} did not make the Deans List or the Honor Roll.')
        studentName = input("\nEnter the student's name or ZZZ to quit: ")        
                
    quit()