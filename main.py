import json

class Local:
    def __init__(self):
        self.numero_local = "0"
        self.type_local = ""



class Etudiant:
    def __init__(self, p_nom : str="", p_local:Local=Local()):
        self.nom = p_nom
        self.Local = p_local


L1 = Local()
L2 = Local()
L1.numero_local = 100
L1.type_local = "Technique"
L2.numero_local = 200
L2.type_local = "Normal"
list_loc = [L1, L2]
E = Etudiant("Dylan", L1)


print(E.nom, E.Local.type_local, E.Local.numero_local)

try:
    with open(".\serialiser.json", "w") as F:
        json.dump(E.__dict__, F)
except:
    print("Erreur écriture")



# Json string
import jsonpickle

Json_string = jsonpickle.encode(E)
print(Json_string)

#Serialisation à un fichier json

with open("test.json", "w") as F:
    F.write(Json_string)

#Deserialisation à partir du fichier json

with open("test.json", "r") as F:
    Json_string1 = F.readline()

E2 = jsonpickle.decode(Json_string1)
print(E2.nom, E2.Local.numero_local)
