from faker import Faker
from db import User, Address, Country, Session
from sqlalchemy.exc import SQLAlchemyError

fake = Faker()

def generate_fake_addresses(num_addresses):
    addresses = []
    for _ in range(num_addresses):
        street = fake.street_address()
        city = fake.city()
        postal_code = fake.postcode()
        country_name = fake.country()
        addresses.append({'street': street, 'city': city, 'postal_code': postal_code, 'country_name': country_name})
    return addresses

def add_address(username, street, city, postal_code, country_name, my_session):
    user = my_session.query(User).filter(User.username == username).first()
    if user:
        country = my_session.query(Country).filter(Country.country == country_name).first()
        if country:
            new_address = Address(
                street=street,
                city=city,
                postal_code=postal_code,
                country_id=country.id,
                user_id=user.id
            )
            my_session.add(new_address)
            try:
                my_session.commit()
                return f"Successfully added Address: {new_address.street} to the database"
            except SQLAlchemyError as err:
                my_session.rollback()
                print(err)
                return f"Error adding address: {err}"
        else:
            return f"Country '{country_name}' does not exist in the database"
    else:
        return f"User '{username}' does not exist in the database"

def update_address(username, street, city, postal_code, country_name, my_session):
    user = my_session.query(User).filter(User.username == username).first()
    if user:
        country = my_session.query(Country).filter(Country.country == country_name).first()
        if country:
            address = my_session.query(Address).filter(Address.user_id == user.id, Address.street == street).first()
            if address:
                address.street = street
                address.city = city
                address.postal_code = postal_code
                address.country_id = country.id
                try:
                    my_session.commit()
                    return f"Successfully modified Address: {address.street} in the database"
                except SQLAlchemyError as err:
                    my_session.rollback()
                    print(err)
                    return f"Error updating address: {err}"
            else:
                return "Address does not exist in the database"
        else:
            return f"Country '{country_name}' does not exist in the database"
    else:
        return f"User '{username}' does not exist in the database"

def delete_address(street, my_session):
    address = my_session.query(Address).filter(Address.street == street).first()
    if address:
        try:
            my_session.delete(address)
            my_session.commit()
            return f"Successfully deleted Address: {address.street} from the database"
        except SQLAlchemyError as err:
            my_session.rollback()
            print(err)
            return f"Error deleting address: {err}"
    else:
        return "Address does not exist in the database"

def main():
    NUM_ADDRESSES = 100

    fake_addresses = generate_fake_addresses(NUM_ADDRESSES)

    with Session() as my_session:
        while True:
            choice = input("----------------------\nChoose a letter: \n'a' to add a new address \n'u' to update an existing address\n'd' to delete an address \n'q' to quit\n----------------------\n ")
            if choice.lower() == 'a':
                print("Available addresses:")
                for i, address in enumerate(fake_addresses, start=1):
                    print(f"{i}. {address['street']}, {address['city']}, {address['postal_code']}, {address['country_name']}")

                choice = int(input("Enter the number of the address you want to add (1-100): "))
                address_data = fake_addresses[choice - 1]

                username = input("Enter the username to associate the new address: ")

                added_address = add_address(username=username, **address_data, my_session=my_session)
                print(added_address)
            elif choice.lower() == 'u':
                street = input("Enter the street of the address you want to update: ")

                username = input("Enter the username of the address you want to update: ")

                address_data = fake_addresses[choice - 1]

                updated_address = update_address(username=username, street=street, **address_data, my_session=my_session)
                print(updated_address)
            elif choice.lower() == 'd':
                street = input("Enter the street of the address you want to delete: ")
                result = delete_address(street, my_session)
                print(result)
            elif choice.lower() == 'q':
                print("Exiting...")
                break

if __name__ == "__main__":
    main()



"""from db import (User, Address,Country, Session)
from sqlalchemy.exc import SQLAlchemyError

def get_user_by_username(username, my_session):
    user = my_session.query(User).filter(User.username == username).first()
    return user.id

def get_country_id(country_name, my_session):
    country = my_session.query(Country).filter(Country.country == country_name).first()
    return country.id

def get_all_usernames(my_session):
    usernames = my_session.query(User.username).all()
    return [username[0] for username in usernames]

predefined_addresses = [
    {'street': 'Via Cavour 18', 'city': 'Ravenna', 'postal_code': '48100', 'country_name': 'Italy', 'country_id': 49},
    {'street': 'Piazza Duomo 5', 'city': 'Milano', 'postal_code': '20121', 'country_name': 'Italy', 'country_id': 49},
    {'street': 'Champs-Élysées 36', 'city': 'Paris', 'postal_code': '75008', 'country_name': 'France', 'country_id': 20},
    {'street': 'Calle Alcalá 19', 'city': 'Madrid', 'postal_code': '28014', 'country_name': 'Spain', 'country_id': 31},
    {'street': 'Hauptstr. 12', 'city': 'Berlin', 'postal_code': '10317', 'country_name': 'Germany', 'country_id': 42},
    {'street': 'Tverskaya St. 6', 'city': 'Moscow', 'postal_code': '125009', 'country_name': 'Russia', 'country_id': 11},
    {'street': 'Hollywood Blvd 1234', 'city': 'Los Angeles', 'postal_code': '90028', 'country_name': 'United States', 'country_id': 10},
    {'street': 'Roppongi Hills 6-10-1', 'city': 'Tokyo', 'postal_code': '106-6108', 'country_name': 'Japan', 'country_id': 1},
    {'street': 'Pitt St 42', 'city': 'Sydney', 'postal_code': 'NSW 2000', 'country_name': 'Australia', 'country_id': 37}
]

def add_address2(inusername, choice, my_session):
    user_id = get_user_by_username(inusername, my_session)
    if user_id:
        if 1 <= choice <= len(predefined_addresses):
            address_data = predefined_addresses[choice - 1]
            new_address = Address(
                street=address_data['street'],
                city=address_data['city'],
                postal_code=address_data['postal_code'],
                country_id=address_data['country_id'],
                user_id=user_id
            )
            my_session.add(new_address)
            try:
                my_session.commit()
                return f"Successfully added Address: {new_address.street} to the database"
            except SQLAlchemyError as err:
                my_session.rollback()
                print(err)
                return f"Error adding address: {err}"
        else:
            return "Invalid choice"
    else:
        return f"User '{inusername}' does not exist"

def update_address2(inusername, choice, my_session):
    user_id = get_user_by_username(inusername, my_session)
    if user_id:
        if 1 <= choice <= len(predefined_addresses):
            address_data = predefined_addresses[choice - 1]
            address = my_session.query(Address).filter(Address.user_id == user_id).first()
            if address:
                address.street = address_data['street']
                address.city = address_data['city']
                address.postal_code = address_data['postal_code']
                address.country_id = address_data['country_id']
                try:
                    my_session.commit()
                    return f"Successfully modified Address: {address.street} in the database"
                except SQLAlchemyError as err:
                    my_session.rollback()
                    print(err)
                    return f"Error updating address: {err}"
            else:
                return "Address does not exist in the database"
        else:
            return "Invalid choice"
    else:
        return f"User '{inusername}' does not exist"

def add_address(inusername, instreet, incity, inpostal_code,country_name, my_session):
    user_id = get_user_by_username(inusername, my_session)
    incountry_id=get_country_id(country_name=country_name,my_session=my_session)

    if user_id:
        
        address = my_session.query(Address).filter(Address.user_id == user_id, Address.street == instreet).first()

        if not address:
            new_address = Address(
                street=instreet,
                city=incity,
                postal_code=inpostal_code,
                country_id=incountry_id,
                user_id=user_id
            )

            try:
                my_session.add(new_address)
                return f"Successfully added Address: {new_address.street} to the database"
            except SQLAlchemyError as err:
                my_session.rollback()
                print(err)
                return f"Error adding address: {err}"
        else:
            return f"This address is already created for user:{inusername}"
        
    else:
        return f"This user: {inusername} does not exist!"

def update_address(inusername, instreet, incity, inpostal_code, incountry_id, my_session):
    user_id = get_user_by_username(inusername, my_session)

    if user_id:

        address = my_session.query(Address).filter(Address.user_id == user_id).first()

        if address:
            address.street = instreet
            address.city = incity
            address.postal_code = inpostal_code
            address.country_id = incountry_id
            address.user_id =user_id

            try:
                my_session.commit()
                return f"Successfully modified Address: {address.street} in the database"
            except SQLAlchemyError as err:
                my_session.rollback()
                print(err)
                return f"Error updating address: {err}"
        else:
            return "Address does not exist in the database"
    else:
        return f"User '{inusername}' does not exist"



def delete_address(instreet, my_session):
    address = my_session.query(Address).filter(Address.street == instreet).first()
    
    if address:
        try:
            my_session.delete(address)
            my_session.commit()
            return f"Successfully deleted Address: {address.street} from the database"
        except SQLAlchemyError as err:
            my_session.rollback()
            print(err)
            return f"Error deleting address: {err}"
    else:
        return "Address does not exist in the database"
    


def main():
    with Session() as my_session:
        while True:
            choice = input("----------------------\nChoose a letter: \n'a' to add a new address \n'u' to update an existing address\n'd' to delete an address \n'q' to quit\n----------------------\n ")
            if choice.lower() == 'a':
                print("Available addresses:")
                for i, address in enumerate(predefined_addresses, start=1):
                    print(f"{i}. {address['street']}, {address['city']}, {address['postal_code']}, {address['country_name']}")

                choice = int(input("Enter the number of the address you want to add (1-10): "))
                
                usernames = get_all_usernames(my_session)
                print("Available usernames:")
                for i, username in enumerate(usernames, start=1):
                    print(f"{i}. {username}")

                user_choice = int(input("Enter the number of the username to associate the new address: "))
                username = usernames[user_choice - 1]

                added_address2 = add_address2(inusername=username, choice=choice, my_session=my_session)
                print(added_address2)
                
            elif choice.lower() == 'u':
                print("Available addresses:")
                for i, address in enumerate(predefined_addresses, start=1):
                    print(f"{i}. {address['street']}, {address['city']}, {address['postal_code']}, {address['country_name']}")

                choice = int(input("Enter the number of the address you want to update (1-10): "))
                
                usernames = get_all_usernames(my_session)
                print("Available usernames:")
                for i, username in enumerate(usernames, start=1):
                    print(f"{i}. {username}")

                user_choice = int(input("Enter the number of the username to update the address: "))
                username = usernames[user_choice - 1]

                up_address2 = update_address2(inusername=username, choice=choice, my_session=my_session)
                print(up_address2)
                
            elif choice.lower() == 'd':
                instreet = input("Enter the street to delete: ")
                result = delete_address(instreet, my_session)
                print(result)
                
            elif choice.lower() == 'q':
                print("Exiting...")
                break

if __name__ == "__main__":
    main()"""




"""def main():
    parser = argparse.ArgumentParser(description="Manage addresses in the database")
    parser.add_argument('-a', '--add', action='store_true', help='Add a new address')
    parser.add_argument('-u', '--update', action='store_true', help='Update an existing address')
    parser.add_argument('-d', '--delete', action='store_true', help='Delete an address')
    
    args = parser.parse_args()
    
    with Session() as my_session:
        if args.add:
            added_address = add_address(instreet="instreet", 
                                        incity="incity", 
                                        inpostal_code="inpostal_code",
                                        incountry_id="incountry_id",
                                        inuser_id="inuser_id",
                                        my_session="my_session")
            my_session.commit() 
            print(added_address)
            
        elif args.update:
            up_address = update_address(instreet="instreet", 
                                        incity="incity", 
                                        inpostal_code="inpostal_code",
                                        incountry_id="incountry_id",
                                        inuser_id="inuser_id",
                                        my_session="my_session")
            my_session.commit() 
            print(up_address)
            
        elif args.delete:
            instreet = input("Enter the street to delete: ")
            result = delete_address(instreet, my_session)
            my_session.commit() 
            print(result)

"""