from faker import Faker
from db import Country, City, Session
from sqlalchemy.exc import SQLAlchemyError

fake = Faker()

def generate_fake_countries(num_countries):
    countries = []
    for _ in range(num_countries):
        country_name = fake.country()
        iso2 = fake.country_code(representation="alpha-2")
        iso3 = fake.country_code(representation="alpha-3")
        countries.append({'country': country_name, 'iso2': iso2, 'iso3': iso3})
    return countries

def generate_fake_cities(num_cities):
    cities = []
    for _ in range(num_cities):
        city_name = fake.city()
        admin_name = fake.state()
        lat = fake.latitude()
        lng = fake.longitude()
        city_ascii = city_name.lower().replace(' ', '_')
        capital = fake.random_element(elements=('primary', 'admin', 'minor'))
        population = fake.random_int(min=10000, max=10000000)
        country_id = fake.random_int(min=1, max=num_cities)  # Simula una foreign key per il campo fk_count_id
        cities.append({'city': city_name, 'admin_name': admin_name, 'lat': lat, 'lng': lng, 'city_ascii': city_ascii,
                       'capital': capital, 'population': population, 'fk_count_id': country_id})
    return cities

def filter_data_by_country(fake_countries, my_session):
    n = 0
    for country_data in fake_countries:
        country_name = country_data['country']
        iso2 = country_data['iso2']
        iso3 = country_data['iso3']

        country = my_session.query(Country).filter(Country.country == country_name).first()

        if not country:
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

    print("Finished adding countries to the database.")
    return n

def filter_data_by_city(fake_cities, my_session):
    n = 0
    for city_data in fake_cities:
        city_name = city_data['city']

        country_id = city_data['fk_count_id']
        country = my_session.query(Country).filter(Country.id == country_id).first()

        if not country:
            print(f'Country for city {city_name} not found in the database')
            continue

        city = my_session.query(City).filter(City.city == city_name).first()

        if city:
            print(f'City {city_name} is already in the database')
            continue

        new_city = City(
            admin_name=city_data['admin_name'],
            city=city_data['city'],
            lat=city_data['lat'],
            lng=city_data['lng'],
            city_ascii=city_data['city_ascii'],
            capital=city_data['capital'],
            population=city_data['population'],
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

    print("Finished adding cities to the database.")
    return n

def main():
    NUM_COUNTRIES = 100
    NUM_CITIES = 100

    fake_countries = generate_fake_countries(NUM_COUNTRIES)
    fake_cities = generate_fake_cities(NUM_CITIES)

    with Session() as my_session:
        print("Choose an option:")
        print("1. Filter data by city")
        print("2. Filter data by country")
        choice = input("Enter your choice: ")

        if choice == "1":
            filtered_cities = filter_data_by_city(fake_cities, my_session)
            print(filtered_cities)
        elif choice == "2":
            filtered_countries = filter_data_by_country(fake_countries, my_session)
            print(filtered_countries)
        else:
            print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
