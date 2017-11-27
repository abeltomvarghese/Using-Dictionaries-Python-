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

def displayRunners(ListRun):
    for J in ListRun:
        if J['time'] < "2:00:00":
            print(J['name'])
            print(J['surname'])            
    


marathonR=loadResults()
displayRunners(marathonR)
    
