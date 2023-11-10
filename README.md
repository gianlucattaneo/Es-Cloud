# Es-Cloud - Documentazione API

## Panoramica
L'API fornisce operazioni CRUD (Create, Read, Update, Delete) per la tabella "Persona" in un database PostgreSQL. Utilizza Flask come framework per gestire le richieste HTTP e Psycopg2 come driver per PostgreSQL per effettuare le operazioni sul database.

## Build / Deploy
Il solo comando utilizzato è `docker compose up -d` dato che il processo di building dell'immagine della API viene eseguito automaticamente al suo interno (è necessario che il Dockerfile sia nella stessa directory del file `docker-compose.yml` ).

Steps: 
- Aprire il terminale all'interno della cartella del progetto 
- Eseguire il comando `docker compose up -d`
- Attendere che l'esecuzione del comando termini

## Utilizzo 
### Tramite Python 
 - Aprire il terminale all'interno della cartella **/sender**
 - Creare un Virtual Environment tramite il comando  `python<versione> -m venv <nome-ambiente-virtuale>` ed attivarlo tramite il comando `source env/bin/activate` (OPZIONALE)
 - Eseguire il comando `pip install -r requirements.txt` per installare i requisiti dell'applicazione
 - Eseguire l'applicazione tramite il comando `python req_sender.py`


### Tramite Postman
E' possibile eseguire richieste HTTP all'API come descritto in seguito verso l'indirizzo **localhost:5000**


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
