from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

# Crea l'applicazione FastAPI
app = FastAPI()

# Configura la connessione al database
engine = create_async_engine(
    "postgresql://postgres:mysecretpassword@localhost:5432/postgres",
    echo=True,
)

# Crea il sessione
Session = sessionmaker(engine, expire_on_commit=False)

# Crea il modello di dati
class Person(BaseModel):
    id: int
    name: str
    age: int

# Definisci i metodi CRUD

@app.get("/persons")
async def get_persons():
    with Session() as session:
        persons = session.query(Person).all()
    return persons

@app.get("/persons/{id}")
async def get_person(id: int):
    with Session() as session:
        person = session.query(Person).get(id)
    return person

@app.post("/persons")
async def create_person(person: Person):
    with Session() as session:
        session.add(person)
        session.commit()
    return person

@app.put("/persons/{id}")
async def update_person(id: int, person: Person):
    with Session() as session:
        person_in_db = session.query(Person).get(id)
        person_in_db.update(person)
        session.commit()
    return person

@app.delete("/persons/{id}")
async def delete_person(id: int):
    with Session() as session:
        person = session.query(Person).get(id)
        session.delete(person)
        session.commit()
    return {"message": "Person deleted"}

# Avvia l'applicazione
if __name__ == "__main__":
    app.run(debug=True)