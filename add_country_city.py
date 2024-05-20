from db import (Country, City, Session)
from test import (read_csv,filter_data_by_country,filter_data_by_city, FILENAME)
from sqlalchemy.exc import SQLAlchemyError

def add_countries(filename, my_session):
    my_dict_list = read_csv(filename)
    n=0
    
    for key, value in filter_data_by_country(my_dict_list).items():
        
        new_country = Country(country    = key,
                            iso2         = value[0],
                            iso3         = value[1])
                        
        try:
            my_session.add(new_country)
            print(f"Successfully {n} added to the database")
                                
        except SQLAlchemyError as err:
            print(err)
        
        n+=1
    my_session.commit()

def add_cities(filename, my_session):
    my_dict_list = read_csv(filename)

    # Creare una mappa nome_paese -> id_paese
    country_name_id_map = {country.country: country.id for country in my_session.query(Country)}

    n = 0
    for key, value in filter_data_by_city(my_dict_list).items():
        # Ottenere l'id del paese corrispondente al nome del paese dalla mappa
        country_id = country_name_id_map.get(value[6])  # Assumendo che il country_name sia alla posizione 6 nella lista value

        new_city = City(
            city=key,
            admin_name=value[0],
            lat=value[1],
            lng=value[2],
            capital=value[3],
            city_ascii=value[4],
            population=value[5],
            fk_count_id=country_id
        )

        try:
            my_session.add(new_city)
            print(f"Successfully added {key} to the database")
        except SQLAlchemyError as err:
            print(err)

        n += 1

    my_session.commit()


def add_cities2(cities, my_session):

    for city in cities:
        city = my_session.query(City).filter(City.city == city.get('id')).first()
        if not city:
            new_city = City(
                city=city.get('city'),
                city_ascii=city.get('city_ascii'),
                lat=city.get('lat'),
                lng=city.get('lng'),
                country=city.get('country'),
                iso2=city.get('iso2'),
                iso3=city.get('iso3'),
                admin_name=city.get('admin_name'),
                capital=city.get('capital'),
                population=city.get('population'),
                city_id=city.get('id')
            )

        try:
                my_session.commit(new_city)
                return f"Successfully modified Address: {city} in the database"
        except SQLAlchemyError as err:
                my_session.rollback()
                print(err)
                return f"Error updating address: {err}"


def main():
    with Session() as my_session:
        add_cities(filename = FILENAME, my_session = my_session)
        

if __name__ == "__main__":
    main()
