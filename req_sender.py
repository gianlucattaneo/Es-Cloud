import requests
import json

base_url = 'http://localhost:5000'  # Sostituisci con l'URL effettivo della tua API
stop = False

if __name__ == '__main__':
    while not stop:
        print('1 -> Get All\n2 -> Get by Id\n3 -> Insert\n4 -> Update\n5 -> Delete\n0 -> Exit\n')
        
        match  input('Operazione? --> '):
            case '1':
                response = requests.get(f'{base_url}/data')
                print('GET all data:', response.json())
                
            case '2':
                id = input('ID? --> ')
                response = requests.get(f'{base_url}/data/{id}')
                print('GET single data:', response.json())
                
            case '3':
                nome = input('Nome? --> ')
                cognome = input('Cognome? --> ')
                new_data = {'value1': nome, 'value2': cognome}
                response = requests.post(f'{base_url}/data', json=new_data)
                print('POST new data:', response.json())
                
            case '4':
                id = input('ID? --> ')
                nome = input('Nome? --> ')
                cognome = input('Cognome? --> ')
                updated_data = {'value1': nome, 'value2': cognome}
                response = requests.put(f'{base_url}/data/{id}', json=updated_data)
                print('PUT updated data:', response.json())
                
            case '5':
                id = input('ID? --> ')
                response = requests.delete(f'{base_url}/data/{id}')
                print('DELETE data:', response.json())
                
            case _:
                stop = True

        input("Press Enter to continue...")