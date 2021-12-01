from flask import Flask, jsonify, request

app = Flask(__name__)

# Characters
# Wheel of Time
db = []

log = []


# def AddLog(data):
#     pos=-1
#     max=data['timestamp']
#     for i in len(db):
#         if(db[i]['clientid']==data['clientid'] and (data['timestamp']-db[i]['timestamp'])<=max):
#             pos=i
#             max=(data['timestamp']-db[i]['timestamp'])
#     print(pos)
#     if (pos==-1):
#         return data
#     set1=set(db[pos].items())
#     set2=set(data.items())
#     log = dict({'clientid':data['clientid'],'timestamp':data['timestamp']})
#     log.update(set1^set2)


@app.route('/')
def getTitle():
    return "Flask is running\nWelcome to The Wheel of Time"


# Using the GET method
@app.route("/database", methods=['GET'])
def getCharacters():
    return jsonify({'Logs': log})


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
    findLog(data)
    # db.append(data)
    return jsonify({'Got your data': "True"})


def findLog(data):
    if len(log) == 0:
        print("log empty - creating log")
        # log 0
        temp = dict({'clientid': data['clientid'], 'data': data['data'], 'timestamp': data['timestamp']})
        log.append(temp)
    else:
        flag = 0
        for i in log:
            if i['clientid'] == data['clientid']:
                print("id present")
                # Algorithm to add difference to be implemented here
                findChanges()
                flag = 1
                break

        if flag == 0:
            # Adding new client
            print("not present")
            # log 0 for the new client id
            lst1 = []
            dct = {'timestamp': data['timestamp'], 'data': data['data']}
            lst1.append(dct)
            temp = dict({'clientid': data['clientid'], 'data': lst1})
            log.append(temp)


def findChanges():
    pass


if __name__ == '__main__':
    app.run(debug=False)
