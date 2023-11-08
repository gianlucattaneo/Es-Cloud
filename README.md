# Es-Cloud - Documentazione API

## Panoramica
L'API fornisce operazioni CRUD (Create, Read, Update, Delete) per la tabella "Persona" in un database PostgreSQL. Utilizza Flask come framework per gestire le richieste HTTP e Psycopg2 come driver per PostgreSQL per effettuare le operazioni sul database.

## Build / Deploy
Il solo comando utilizzato è ```docker compose up -d``` dato che il processo di building dell'immagine della API viene eseguito automaticamente al suo interno (è necessario che il Dockerfile sia nella stessa directory del file ``` docker-compose.yml ``` ).

## Utilizzo 
### Tramite Python 
 E' possibile utlizzare il programma all'interno della cartella **/sender** eseguendo prima il comando ```pip install -r requirements.txt``` e poi eseguendo ```python req_sender.py```

### Tramite Postman
E' possibile andare ad eseguire richieste HTTP all'API come descritto in seguito


## Endpoint Disponibili
| Metodo|Endpoint|Descrizione|
|-|-|-|
|GET|/data|Restituisce tutte le Persone presenti nel db|
|GET|/data/{id}|Restituisce una singola Persona dato l'id|
|POST|/data|Inserisce nel db una nuova istanza di Persona|
|PUT|/data/{id}|Aggiorna una Persona esistente|
|DELETE|/data/{id}|Cancella una Persona dal db|
---

## Endpoint

### GET /data
- **Parametri:** Nessuno.
- **Response:**
    ```json
    [
        {"id": 1, "Nome": "Alice", "Cognome": "Rossi"},
        {"id": 2, "Nome": "Bob", "Cognome": "Verdi"}
        // Altri dati...
    ]
    ```
  
### GET /data/{id}
- **Parametri:** `id` (intero)
- **Response:**
    ```json
    {"id": 1, "Nome": "Alice", "Cognome": "Rossi"}
    ```

### POST /data
- **Parametri:** 
    - I dati devono essere inviati come JSON nel body della richiesta con i campi "Nome" e "Cognome".
- **Response:**
    ```json
    {"message": "Data created"}
    ```

### PUT /data/{id}
- **Parametri:** `id` (intero) 
    - I nuovi dati devono essere inviati come JSON nel body della richiesta con i campi "Nome" e "Cognome".
- **Response:**
    ```json
    {"message": "Data updated"}
    ```

### DELETE /data/{id}
- **Parametri:** `id` (intero)
- **Response:**
    ```json
    {"message": "Data deleted"}
    ```
