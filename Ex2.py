def loadResults():
    ReadMarathon = open("marathon.csv")
    runners = []
    for eachLine in ReadMarathon:
        info = eachLine.split(",")
        s = {}
        s['number'] = info[0]
        s['time'] = info[1]
        s['name'] = info[2]
        s['surname'] = info[3]
        runners.append(s)
    return runners

def displayTime(runnerList,RunnerNum):
    found = False
    for J in runnerList:
        if int(J['number']) == RunnerNum:  
            print(J['name'])
            print(J['surname'])
            print(J['time'])
            found = True
            
    if found == False:
        print("This competitor does not exist")
        
    
         
        
search = "yes"
while search == "yes": 
    marathonR=loadResults()
    NumRunner = int(input("Enter the number of the runner: "))
    displayTime(marathonR,NumRunner)    
    search = input("Would you like to search another player? ") 
