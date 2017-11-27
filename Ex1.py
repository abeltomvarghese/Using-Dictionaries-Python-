def loadResults():
    ReadMarathon = open("marathon.csv")
    runners = []
    for eachLine in ReadMarathon:
        info = eachLine.split(",")
        s = {}
        s['number'] = info[0]
        
        s['name'] = info[2]
        s['surname'] = info[3]
        s['time'] = info[1]
        runners.append(s)


loadResults()
