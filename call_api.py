import json, requests


base_url = "http://127.0.0.1:5000/"

while(True):
    opt = input("1. Add Event \n2. Get all Events \n3. Get Single Event \n4. Update an Event \n5. Delete Event \n6. Stop \n\n Choose a option : ")
    if(opt == '1'):
        url = base_url + "event"
        data = {}
        data['name'] = input("Enter the Event Name :")
        data['address'] = input("Enter the Venue Address : ")
        data['country'] = input("Enter the Country : ")
        data['description'] = input("Enter the event description : ")

        json_data = json.dumps(data)
    
        res = requests.post(url = url, json = json_data)
        print(res.text)



    elif(opt == '2'):
        url = base_url + "all-events"
        res = requests.get(url = url)
        print(json.loads(res.text))



    elif(opt == '3'):
        id = input("Enter the Event ID : ")
        url = base_url + "event/" + id
        res = requests.get(url = url)
        print(res.text)




    elif(opt == '4'):
        id = input("Enter the Event ID : ")
        url = base_url + "event/" + id

        data = {}
        data['name'] = input("Enter the Event Name :")
        data['address'] = input("Enter the Venue Address : ")
        data['country'] = input("Enter the Country : ")
        data['description'] = input("Enter the event description : ")

        res = requests.put( url = url, json = json.dumps(data))
        print(res.text)



    elif(opt == '5'):
        id = input("Enter the Event ID : ")
        url = base_url + "event/" + id

        res = requests.delete(url = url)
        print(res.text)


    else:
        break


