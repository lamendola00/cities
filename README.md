SQLAlchemy Database Management


This repository contains scripts and modules for managing a MySQL database using SQLAlchemy in Python. It includes functionality for creating database schemas, establishing connections, adding, updating, and deleting data from the database.

Requirements:

- Python 3

- SQLAlchemy

- PyMySQL
  
- Faker (for generating fake data, optional)

Usage:

1. db_set.py:

- Responsible for creating the database schema and establishing the connection using SQLAlchemy.
- Imports necessary modules from SQLAlchemy to create the database schema, including necessary data types, relationships, and session management.
- Establishes a connection to the MySQL database server.

2. db.py:

- Defines classes for database tables: Country, City, Address, and User.
- Establishes a connection to the MySQL database server.
- Utilizes SQLAlchemy for database management and ORM (Object-Relational Mapping).

3. user_functions.py:

- Implements functions for managing user data in the database.
- Utilizes Faker library to generate fake user data for testing purposes.
- Functions include:
  - generate_fake_users(num_users): Generates fake user data
  - add_user(fake_user, my_session): Adds a new user to the database.
  - update_user(username, fake_user, my_session): Updates an existing user in the database.
  - delete_user(username, my_session): Deletes a user from the database.
    
- Provides a command-line interface for adding, updating, and deleting users interactively.

4. address_functions.py:

- Implements functions for managing address data in the database.
- Utilizes Faker library to generate fake address data for testing purposes.
- Functions include:
  - generate_fake_addresses(num_addresses): Generates fake address data.
  - add_address(username, street, city, postal_code, country_name, my_session): Adds a new address to the database.
  - update_address(username, street, city, postal_code, country_name, my_session): Updates an existing address in the database.
  - delete_address(street, my_session): Deletes an address from the database.

- Provides a command-line interface for adding, updating, and deleting addresses interactively.

5. country_and_city_functions.py:

- Implements functions for generating and filtering country and city data in the database.
- Utilizes Faker library to generate fake country and city data for testing purposes.
- Functions include:
  - generate_fake_countries(num_countries): Generates fake country data.
  - generate_fake_cities(num_cities): Generates fake city data.
  - filter_data_by_country(fake_countries, my_session): Filters and adds countries to the database.
  - filter_data_by_city(fake_cities, my_session): Filters and adds cities to the database.

-Provides a command-line interface for filtering and adding country/city data interactively.

