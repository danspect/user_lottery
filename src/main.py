import csv
from data.database import Database
import random

db = Database()
db.create_table()

with open("users.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        db.insert_user(row)

db.commit()
print(f"Número de participantes: {db.count_rows()}")

participante_escolhido = random.randint(1, db.count_rows())

print(f"Participante vencedor: {db.get_by_id(participante_escolhido)}")
