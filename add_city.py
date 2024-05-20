from db import (City, Session)
from test import (read_file, filter_data_by_city, FILENAME)
from sqlalchemy.exc import SQLAlchemyError

def add_cities(filename, my_session):
    """
    Reads city data from a file, filters it, and adds cities to the database.

    Args:
        filename (str): Path to the CSV file containing city data.
        my_session (sqlalchemy.orm.session.Session): A SQLAlchemy session object.
    """

    my_dict_list = read_file(filename)
    n = 0

    for city_name, city_data in filter_data_by_city(my_dict_list).items():
        new_city = City(
            city=city_name,
            country_id=None, 
            lat=city_data[0] if city_data[0] else None,  
            lng=city_data[1] if city_data[1] else None,
            population=city_data[2] if city_data[2] else None,
        )

        try:
            my_session.add(new_city)
            print(f"Successfully added city {city_name} ({n+1} total)")
            n += 1
        except SQLAlchemyError as err:
            print(f"Error adding city {city_name}: {err}")

    my_session.commit()

def main():
    with Session() as my_session:
        add_cities(filename=FILENAME, my_session=my_session)

if __name__ == "__main__":
    main()
