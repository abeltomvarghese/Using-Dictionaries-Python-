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

def getResults(runList):
    i = 1 
    while i <len(runList):
        Stime = runList[i]['time']
        Sname = runList[i]['name']
        Ssurname = runList[i]['surname']
        Snumber = runList[i]['number']
        
        
        j = int(i) 
        while j > 0 and runList[j-1]['time']>Stime:
            runList[j] = runList[j-1]
            j = j-1
        assert j <= 0 or runList[j-1]['time'] <=Stime
        runList[j]['time'] = Stime
        runList[j]['name'] = Sname
        runList[j]['surname'] = Ssurname
        runList[j]['number'] = Snumber
        i = i + 1 
        
    return runList
            
    
marathonR=loadResults()
results = getResults(marathonR)
print("The winner is", results[0]["surname"], results[0]["name"], results[0]["time"])
