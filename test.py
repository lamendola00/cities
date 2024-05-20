
""" 
with open(filename, 'r') as file:
    lines = file.readlines()
    headers = lines[0]
    "print(type(lines[0]))"

headers_list = headers.replace('"', '').split(',')
print(headers_list)
"""

"""filename = "/home/lollo/Cities/worldcities.csv"

with open(filename, 'r') as file:
    lines = file.readlines()
    headers = lines[0]
    headers_list = headers.replace('"', '').split(',')
    print("HEADER", headers_list)

    for line in lines[1:5]:

        values = line.replace('"', '').split(',')

        row_tuple = tuple(values[i] for i in range(len(headers_list)))

        print(row_tuple)"""

"""filename = "/home/lollo/Cities/worldcities.csv"

with open(filename, 'r') as file:
    lines = file.readlines()
    headers = lines[0]
    headers_list = headers.replace('"', '').split(',')
    print("HEADER", headers_list)

    rows_dict = {}

    for line in lines[1:]:  
        values = line.replace('"', '').strip().split(',')
        for value, header in zip(values, headers_list):
            rows_dict[header] = value

    print(rows_dict)"""

#test1

"""filename = "/home/lollo/Cities/worldcities.csv"
with open(filename, 'r') as file:
    lines = file.readlines()


headers_line = lines[0].strip() 
data_lines = lines[1:] 

csv_dict = {header.strip(): [] for header in headers_line.split(',')}

for line in data_lines:
    values = line.strip().split(',')
    for i, value in enumerate(values):
        csv_dict[list(csv_dict.keys())[i]].append(value)

for key, values in csv_dict.items():
    print(f"{key}: {values}")


print("Città:")
for city in csv_dict["city"]:
    print(city)
"""
#test 2

"""
with open(filename, 'r') as file:
    lines = file.readlines()

headers_line = lines[0].replace('"', '')

csv_dict = {header.strip(): [] for header in headers_line.split(',')}


for line in lines[1:5]:
    values = line.strip().replace('"', '')
    values = values.split(',')
    for i, value in enumerate(values):
        csv_dict[list(csv_dict.keys())[i]].append(value)

for key, values in csv_dict.items():
    print(f"{key}: {values}")


def get_countries(filename):
    countries = []
    for key in csv_dict.keys():
        if key == "country":
            countries.extend(csv_dict[key])
    return countries
    

countries_list = get_countries(filename)

for country in countries_list:
    print(country)"""

"""with open(filename, 'r') as file:
    lines = file.readlines()
    headers = lines[0]
    rows = lines[1:10]
    "print(type(lines[0]))"

headers_list = headers.replace('"', '').split(',')

print(headers_list[4:7])
"""
"""
with open(filename, 'r') as file:
    lines = file.readlines()
    headers = lines[0].strip()  
    rows = lines[1:10] 

for row in rows:
    row_data = row.strip().replace('"', '').split(',')
    print(row_data[4:7])
"""


"""with open(filename, 'r') as file:
    lines = file.readlines()
    headers = lines[0].strip()  
    rows = lines[1:10] 

    csv_dict = {}
    for header in headers.split(','):  
        csv_dict[header] = []


    for row in rows:
        row_values = row.strip().replace('"', '').split(',')

    for i, value in enumerate(row_values):
        csv_dict[list(csv_dict.keys())[i]].append(value)


    for row in rows:
        row_data = row.strip().replace('"', '').split(',')
        print({eval(list(csv_dict.keys())[4]): row_data[4], eval(list(csv_dict.keys())[5]): row_data[5], eval(list(csv_dict.keys())[6]): row_data[6]})
"""


FILENAME = "/home/lollo/Cities/worldcities.csv"



def read_csv(filename):

    csv_data = [] 

    with open(filename, 'r') as file:
        lines = file.readlines()
        
        headers = lines[0].strip().replace('"', '').split(',')

        for row in lines[1:]:
            row_values = row.strip().replace('"', '').split(',')

            if len(row_values) != len(headers):
                continue

            if not row_values:
                continue

            row_dict = {}
            for i, value in enumerate(row_values):
                row_dict[headers[i]] = value
            

            csv_data.append(row_dict)
            

    return csv_data



"""def filter_data_by_country(data):
    

    filtered_countries = {}

    for row_dict in data:
        for k, v in row_dict.items():
            if k == 'country':
                if v != '24.9408':
                    filtered_countries[v] = [row_dict['iso2'],row_dict['iso3']]


    return filtered_countries"""




"""def filter_data_by_city(filename, my_session):
    csv_data=read_csv(filename)

    n=0

    for row_dict in csv_data:
        for k, v in row_dict.items():
            if k == row_dict['country']:
                country_name = v
                print(country_name)        
                country = Country.query(Country).filter(Country.country == country_name).first()
                if country:
                    if k == 'city':
                        city_name = v
                        print(city_name)
                        city = City.query(City).filter(City.city == city_name).first()
                        if not city:
                            new_city=City( admin_name = row_dict['admin_name'],
                                           city = row_dict['city'],
                                           lat = row_dict['lat'],
                                           lng = row_dict['lng'],
                                           city_ascii = row_dict['city_ascii'] ,
                                           capital = row_dict['capital'],
                                           population = row_dict['capital'], 
                                           fk_count_id =country.id)
                            try:
                                my_session.add(new_city)
                                my_session.commit()
                                return f"Successfully added City: {new_city.city} to the database"
                            except SQLAlchemyError as err:
                                my_session.rollback()
                                print(err)
                                return f"Error adding city: {city_name}"

                        else:
                            print(f'City {city_name} is already in the database')    

                else:
                    print(f'Country{country_name} is not in the database')        
        n+=1
    return n"""

"""def filter_data_by_city(filename, my_session):
    csv_data = read_csv(filename)
    n = 0

    for row_dict in csv_data:
        country_name = row_dict.get('country')

        if not country_name:
            continue  

        country = my_session.query(Country).filter(Country.country == country_name).first()

        if not country:
            print(f'Country {country_name} is not in the database')
            continue

        city_name = row_dict.get('city')

        if not city_name:
            continue  


        city = my_session.query(City).filter(City.city == city_name).first()

        if city:
            print(f'City {city_name} is already in the database')
            continue

        new_city = City(
            capital=row_dict.get('capital', ''),
            city=row_dict.get('city', ''),
            lat=row_dict.get('lat', ''),
            lng=row_dict.get('lng', ''),
            city_ascii=row_dict.get('city_ascii', ''),
            admin_name=row_dict.get('admin_name', ''),
            population=row_dict.get('population', 0),  # Assuming population should be an integer
            fk_count_id=country.id
        )

        try:
            my_session.add(new_city)
            my_session.commit()
            print(f"Successfully added City: {new_city.city} to the database")
        except SQLAlchemyError as err:
            my_session.rollback()
            print(f"Error adding city {city_name}: {err}")

        n += 1

    return n"""

FILENAME = "/home/lollo/Cities/worldcities.csv"



def read_csv(filename):

    csv_data = [] 

    with open(filename, 'r') as file:
        lines = file.readlines()
        
        headers = lines[0].strip().replace('"', '').split(',')

        for row in lines[1:]:
            row_values = row.strip().replace('"', '').split(',')

            if len(row_values) != len(headers):
                continue

            if not row_values:
                continue

            row_dict = {}
            for i, value in enumerate(row_values):
                row_dict[headers[i]] = value
            

            csv_data.append(row_dict)
            

    return csv_data

from db import (Country, City, Session)
from sqlalchemy.exc import SQLAlchemyError

def filter_data_by_country(filename, my_session):
    csv_data = read_csv(filename)
    n = 0

    for row_dict in csv_data:
        # Controlla la presenza delle chiavi richieste
        if 'country' not in row_dict or 'iso2' not in row_dict or 'iso3' not in row_dict:
            continue  # Salta la riga se manca una chiave

        country_name = row_dict['country']
        iso2 = row_dict['iso2']
        iso3 = row_dict['iso3']

        # Verifica se il paese è già nel database
        country = my_session.query(Country).filter(Country.country == country_name).first()

        if not country:
            # Crea un nuovo oggetto Country e aggiungilo al database
            new_country = Country(country=country_name, iso2=iso2, iso3=iso3)
            try:
                my_session.add(new_country)
                my_session.commit()
                print(f"Successfully added Country: {country_name} to the database")
            except SQLAlchemyError as err:
                my_session.rollback()
                print(f"Error adding country {country_name}: {err}")

        else:
            print(f"Country {country_name} already exists in the database")

        n += 1

        # Stampare un messaggio di fine e uscire dal ciclo
        print("Finished adding countries to the database.")
        break

    return n


def filter_data_by_city(filename, my_session):
    csv_data = read_csv(filename)
    n = 0

    for row_dict in csv_data:
        # Controlla la presenza delle chiavi richieste
        if 'country' not in row_dict or 'city' not in row_dict:
            continue  # Salta la riga se manca una chiave

        country_name = row_dict['country']
        city_name = row_dict['city']

        # Ottieni il paese dal database
        country = my_session.query(Country).filter(Country.country == country_name).first()

        if not country:
            print(f'Country {country_name} is not in the database')
            continue

        # Controlla se la città esiste già nel database
        city = my_session.query(City).filter(City.city == city_name).first()

        if city:
            print(f'City {city_name} is already in the database')
            continue

        # Crea un nuovo oggetto City
        new_city = City(
            admin_name=row_dict['admin_name'],
            city=row_dict['city'],
            lat=row_dict['lat'],
            lng=row_dict['lng'],
            city_ascii=row_dict['city_ascii'],
            capital=row_dict['capital'],
            population=(row_dict['population']),  # Converti la popolazione in intero
            fk_count_id=country.id
        )

        try:
            my_session.add(new_city)
            my_session.commit()
            print(f"Successfully added City: {new_city.city} to the database")
        except SQLAlchemyError as err:
            my_session.rollback()
            print(f"Error adding city {city_name}: {err}")

        n += 1

    return n


def main():
    FILE = "/home/lollo/Cities/worldcities.csv"

    print("Choose an option:")
    print("1. Filter data by city")
    print("2. Filter data by country")
    choice = input("Enter your choice: ")

    with Session() as my_session:
        if choice == "1":
            filtered_cities = filter_data_by_city(filename=FILE, my_session=my_session)
            print(filtered_cities)
        elif choice == "2":
            filtered_countries = filter_data_by_country(filename=FILE, my_session=my_session)
            print(filtered_countries)
        else:
            print("Invalid choice. Exiting...")



if __name__ == "__main__":
    main()
