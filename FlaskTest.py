from flask import Flask, jsonify, request
from deepdiff import DeepDiff

app = Flask(__name__)

# Characters
# Wheel of Time
db = []
log = []
dataset = []


@app.route('/')
def getTitle():
    return "Flask is running\nWelcome to The Wheel of Time"

def finddataset(cid,tme):
    c=0
    for i in dataset:
        if i['clientid']==cid:
            c+=1
            print("Client dataset found - \n\n",i['dataset'][-1])
            return (i['dataset'][-1])
    if(c==0):
        print("Client dataset not present")
        return {}

            
def findlogs(cid,tme):
    c=0
    for i in log:
        if i['clientid']==cid:
            c+=1
            print("Client logs found - \n\n")
            lst=[]
            d=0
            for j in i['log']:
                if((j['timestamp -- ']-tme)>0):
                    d+=1
                    lst.append(j)
            strng="Found "+str(d)+" logs - "
            lst1=[strng]
            lst1.append(lst)
            return lst1
        
    if(c==0):
        print("Client logs not present")
        return {}
            



@app.route("/clientcall", methods=['POST'])
def Clientoutput():
    data = request.get_json(force=True)
    clientid=data[0]
    tmestmp=data[1]
    cldata=[finddataset(clientid,tmestmp)]
    cldata.append(findlogs(clientid,tmestmp))
    return jsonify({'Your current dataset is':cldata})


# Using the GET method
@app.route("/database", methods=['GET'])
def getCharacters():
    return jsonify({'Current Dataset': dataset})


# To get character based on user choice
@app.route("/characters/<int:characterId>", methods=['GET'])
def getCharacterById(characterId):
    return jsonify({'Character': db[characterId]})


# Using the POST method
# curl -i -H "Content-Type: Application/json" -X POST http://127.0.0.1:5000/characters
# Use the above link in windows cmd
@app.route("/characters", methods=['POST'])
def addCharacter():
    character = {'id': "7", 'name': "Trollocs", 'gender': "Male",
                 'description': "Wretched, horrifying amalgams of man and beast, these towering Shadowspawn are the "
                                "core of the Dark One's army. While their appearances are varied — some with horns, "
                                "others with beaks or snarled snouts — one thing is universal: their murderous rage. "
                                "They possess a ferocious bloodlust, and can only be controlled by the equally "
                                "terrifying Fades."}

    db.append(character)
    return jsonify({'Added Character': character})


# Using the PUT method to update database
# curl -i -H "Content-Type: Application/json" -X PUT http://127.0.0.1:5000/characters/4
@app.route("/characters/<int:characterId>", methods=['PUT'])
def updateCharacter(characterId):
    db[characterId]['description'] = "This is the updated description for the character selected"
    return jsonify({'Characters': db[characterId]})


# Using the DELETE method to delete a character
# curl -i -H "Content-Type: Application/json" -X DELETE http://127.0.0.1:5000/characters/3
@app.route("/characters/<int:characterId>", methods=['DELETE'])
def deleteCharacter(characterId):
    db.remove(db[characterId])
    return jsonify({'Result': True})


@app.route("/database", methods=['POST'])
def print_post():
    data = request.get_json(force=True)
    # Algorithm to be implemented here of log
    addDatabase(data)
    findChanges(data)
    # db.append(data)
    return jsonify({'Got your data': "True"})


def addDatabase(data):
    if len(dataset) == 0:
        print("Dataset Empty, creating id dataset")
        lst2 = []
        dst = {'dataset -- ': data['data']}
        lst2.append(dst)
        temp = {'clientid': data['clientid'], 'dataset': lst2}
        dataset.append(temp)
    else:
        flag = 0
        for i in dataset:
            if i['clientid'] == data['clientid']:
                print("dataset id present, adding to existing id")
                dst = {'dataset -- ': data['data']}
                i['dataset'].append(dst)
                flag = 1
                break

        if flag == 0:
            # Adding new client dataset
            print("dataset id not present, creating id dataset")
            lst1 = []
            dst = {'dataset -- ': data['data']}
            lst1.append(dst)
            temp = dict({'clientid': data['clientid'], 'dataset': lst1})
            dataset.append(temp)


def addToLog(diff, data):
    if len(log) == 0:
        print("log empty - creating log")
        # log 0
        lst2 = []
        dct = {'timestamp -- ': data['timestamp'], 'dateTime -- ': data['dateTime'], 'log -- ': diff}
        lst2.append(dct)
        temp = {'clientid': data['clientid'], 'log': lst2}
        log.append(temp)
    else:
        flag = 0
        for i in log:
            if i['clientid'] == data['clientid']:
                print("client id %d present in log, updating log\n" % (int(i['clientid'])))
                logFile = {'timestamp -- ': data['timestamp'], 'dateTime -- ': data['dateTime'], 'log -- ': diff}
                i['log'].append(logFile)
                flag = 1
                break

        if flag == 0:
            # Adding new client
            print("Log id not present, creating log id")
            # log 0 for the new client id
            lst1 = []
            dct = {'timestamp -- ': data['timestamp'], 'dateTime -- ': data['dateTime'], 'log -- ': diff}
            lst1.append(dct)
            temp = dict({'clientid': data['clientid'], 'log': lst1})
            log.append(temp)

    print(log)


def findChanges(data):
    for i in dataset:
        if i['clientid'] == data['clientid']:
            print("In findChanges: %d id found\n" % (int(data['clientid'])))
            clientDataList = i['dataset']
            if len(clientDataList) > 1:
                dct1 = clientDataList[-1]['dataset -- ']  # current dataset
                dct2 = clientDataList[-2]['dataset -- ']  # previous dataset

                diff = DeepDiff(dct2, dct1)
                addToLog(diff, data)
                break
            else:
                break


if __name__ == '__main__':
    app.run(debug=False)
