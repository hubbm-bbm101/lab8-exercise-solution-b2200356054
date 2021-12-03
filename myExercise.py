import sys
namelist = sys.argv[2].split(",")
with open("{}".format(sys.argv[1]), "r+") as inputfile:
    records = dict()    
    for lines in inputfile:
        records[lines.split(":")[0]] = lines.split(":")[1]
    for people in namelist:
        try:
            print("Name:{}, University:{}".format(people, records[people]))
        except KeyError:
            print("No record of {} was found.".format(people))