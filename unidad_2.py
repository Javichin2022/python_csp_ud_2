from faker import Faker
import random

fake = Faker()

personas = {}

for n in range (15):
    personas[n+1] = {"nombre": fake.name(), "direccion": fake.address(), "correo_electronico": fake.email(), "telefono": fake.phone_number()}

print(personas)

print()

print(f"El usuario llamado {personas[random.randint(1, 15)]["nombre"]} es el afortunado.")
