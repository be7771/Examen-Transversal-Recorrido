import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "PG78tfojSxibIZUjf75GLjA6zwHLxjsD" #Replace con la clave de MapQuest

while True:
    orig = input("Lugar Inicio: ")
    if orig == "quit" or orig == "s":
        break
    dest = input("Destino: ")
    if dest == "quit" or dest == "s":
        break
    url = main_api + urllib.parse.urlencode ({"key" :key, "from" :orig, "to" :dest})

    json_data = requests.get (url) .json ()
    print("URL:" + (url))
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API status:" + str(json_status) + " = Successful route call \n")
        print("Direcciones")
        print("Direccion desde " + (orig) + " hasta " + (dest))
        print("Kilómetros:" + str ("{:.2f}" .format((json_data ["route"] ["distance"]) *1.61)))
        print("Tiempo de viaje: " + (json_data["route"]["formattedTime"]))
        
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " ("+ str ("{:.2f}" .format((each["distance"]) *1.61)) +" Km)")
    elif json_status == 402:
        print("API status:" + str(json_status) + " = Invalid user input \n")
    elif json_status == 611:
        print("API status:" + str(json_status) + " = Missing entry \n")
    else:
        print("API status:" + str(json_status) + " = Error. \n")