import random

def convertTOleet(message):
    leetMessage= ""
    leetDict = { "a" : ["@","4","/-\\"], "c" : ["("], "d" : ["|)"], "e" : ["3"],
                 "f" : ["pH"], "g" : ["9"], "h" : ["]-[","#"], "i" : ["1","!","|"], "k" : ["]<"],
                 "o" : ["0"], "s" : ["5","$"], "t" : ["7","+"], "u" : ["|_|"], "v" : ["\\/"], "z" : ["2"] }

    for char in message:
        if (char.lower() in leetDict.keys()) and (random.random() <=0.70):
            possibleReplacements = leetDict.get(char.lower(),"")
            leetMessage += random.choice(possibleReplacements)

        else:
            leetMessage += char

    return leetMessage


mssg = input("Enter the message: ")
leetSpeak = convertTOleet(mssg)
print("Leetspeak for {} is \n{}".format(mssg, leetSpeak))
