import csv
from faker import Faker
from random import randint

fake = Faker()

# Genera dati finti per gli utenti
def generate_fake_users(num_users):
    users = []
    for _ in range(num_users):
        name = fake.first_name()
        surname = fake.last_name()
        username = fake.user_name()
        email = fake.email()
        phone = fake.phone_number()
        password = fake.password()
        users.append((name, surname, username, email, phone, password))
    return users

# Genera dati finti per gli indirizzi
def generate_fake_addresses(num_addresses, num_users):
    addresses = []
    for _ in range(num_addresses):
        street = fake.street_address()
        postal_code = fake.postcode()
        fk_city_id = randint(1, num_addresses)  # Simula una foreign key per il campo fk_city_id
        fk_user_id = randint(1, num_users)  # Simula una foreign key per il campo fk_user_id
        addresses.append((street, postal_code, fk_city_id, fk_user_id))
    return addresses

# Crea un file CSV per gli utenti
def create_user_csv(filename, num_users):
    users_data = generate_fake_users(num_users)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'surname', 'username', 'email', 'phone', 'password'])
        writer.writerows(users_data)

# Crea un file CSV per gli indirizzi
def create_address_csv(filename, num_addresses, num_users):
    addresses_data = generate_fake_addresses(num_addresses, num_users)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['street', 'postal_code', 'fk_city_id', 'fk_user_id'])
        writer.writerows(addresses_data)

# Numero di utenti e indirizzi da generare
NUM_USERS = 100
NUM_ADDRESSES = 100

create_user_csv('users.csv', NUM_USERS)
create_address_csv('addresses.csv', NUM_ADDRESSES, NUM_USERS)
