#Name: TrainFormationRandomiser
#
#Date: 03-02-2019 17:33
#
#Version: 1.0
#
#Description: This program creates randomised train formations after giving it a bunch of parameters.
#
#Further information: I got bored running the same train + rolling stock combinations all the time, this truly is Autism crystallized.
#=========================================================#

#arrays containing info

    #Manufacturer, modelnr, name, era, company, length, type, power]
testArrayLocomotives = [
    ["Märklin", 3000, "BR 89-010", 3, "Deutsche Bundesbahn", 8, "Goods Locomotive", "Steam"],
    ["Märklin", 3055, "NS 1212", 4, "Nederlandse Spoorwegen", 15, "Goods & Passenger Locomotive", "Electric"],
    ["Märklin", 3324, "NS 1624", 4, "Nederlandse Spoorwegen", 17, "Goods & Passenger Locomotive", "Electric"],
    ["Märklin", 37001, "BR 212 212-5", 3, "Technische Hilfswerke", 10, "Goods Locomotive", "Diesel-Electric"]
]

testArrayRollingstock = [
    ["Märklin", 4070, "TEE Personenwagen ", 4, "Deutsche Bundesbahn", 20, "Passenger"],
    ["Märklin", 4123, "Umbauwagen 2nd class", 3, "Deutsche Bundesbahn", 8, "Passenger"],
    ["Märklin", 4124, "Umbauwagen 1 & 2nd class", 3, "Deutsche Bundesbahn", 8, "Passenger"],
    ["Märklin", 4145, "Schwerlastwagen", 3, "Deutsche Reichsbahn(until 1945)", 8, "Goods"],
    ["Märklin", 4169, "Stake wagon", 5, "Deutsche Bundesbahn", 5, "Goods"],
    ["Märklin", 4164, "Prussian Landesbahn Carriage", 2, "KPEV", 8,"Passenger"],
]

#print loks
for lok in testArrayLocomotives:
    print(lok[2] + " Era: " + str(lok[3]))

#print rollingstocks
for rollingstock in testArrayRollingstock:
    print(rollingstock[2] + " Era: " + str(rollingstock[3]))

#GUI

