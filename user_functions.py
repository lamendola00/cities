from faker import Faker
from db import User, Session
from sqlalchemy.exc import SQLAlchemyError

fake = Faker()

def generate_fake_users(num_users):
    users = []
    for _ in range(num_users):
        name = fake.first_name()
        surname = fake.last_name()
        username = fake.user_name()
        email = fake.email()
        phone = fake.phone_number()
        password = fake.password()
        users.append({'name': name, 'surname': surname, 'username': username, 'email': email, 'phone': phone, 'password': password})
    return users

def add_user(fake_user, my_session):
    new_user = User(
        name=fake_user['name'],
        surname=fake_user['surname'],
        username=fake_user['username'],
        email=fake_user['email'],
        phone=fake_user['phone'],
        password=fake_user['password']
    )
    my_session.add(new_user)
    try:
        my_session.commit()
        return f"Successfully added user: {new_user.username}"
    except SQLAlchemyError as err:
        my_session.rollback()
        print(err)
        return f"Error adding user: {err}"

def update_user(username, fake_user, my_session):
    existing_user = my_session.query(User).filter(User.username == username).first()
    if existing_user:
        existing_user.name = fake_user['name']
        existing_user.surname = fake_user['surname']
        existing_user.email = fake_user['email']
        existing_user.phone = fake_user['phone']
        existing_user.password = fake_user['password']
        try:
            my_session.commit()
            return f"Successfully updated user: {existing_user.username}"
        except SQLAlchemyError as err:
            my_session.rollback()
            print(err)
            return f"Error updating user: {err}"
    else:
        return f"User '{username}' does not exist"
    
def delete_user(username, my_session):
    user = my_session.query(User).filter(User.username == username).first()
    if user:
        try:
            my_session.delete(user)
            my_session.commit()
            return f"User {username} successfully deleted from the database"
        except SQLAlchemyError as err:
            my_session.rollback()
            print(err)
            return f"Error deleting user: {err}"
    else:
        return f"User with username {username} does not exist in the database"


def main():
    with Session() as my_session:
        while True:
            choice = input("----------------------\nChoose a letter: \n'a' to add/update a user \n'd' to delete a user \n'q' to quit\n----------------------\n ")
            if choice.lower() == 'a':
                add_update_choice = input("Enter 'a' to add a new user or 'u' to update an existing user: ")
                if add_update_choice.lower() == 'a':
                    num_users = int(input("Enter the number of fake users to generate: "))
                    fake_users = generate_fake_users(num_users)
                    for fake_user in fake_users:
                        add_result = add_user(fake_user, my_session)
                        print(add_result)
                elif add_update_choice.lower() == 'u':
                    username = input("Enter the username of the user you want to update: ")
                    fake_user = generate_fake_users(1)[0]
                    update_result = update_user(username, fake_user, my_session)
                    print(update_result)
                else:
                    print("Invalid choice. Please enter 'a' or 'u'.")

            elif choice.lower() == 'd':
                print("Current users:")
                users = my_session.query(User).all()
                for user in users:
                    print(f"Username: {user.username}, Name: {user.name}, Surname: {user.surname}")

                username_to_delete = input("----------------------\nEnter the username to delete: \n----------------------\n")

                result = delete_user(username_to_delete, my_session)
                my_session.commit()
                print(result)

            elif choice.lower() == 'q':
                print("Exiting...")
                break

if __name__ == "__main__":
    main()



""""""

"""def main():
    with Session() as my_session:
        while True:
            choice = input("----------------------\nChoose a letter: \n'a' to add a new user \n'u' to update an existing user\n'd' to delete an user \n'q' to quit\n----------------------\n ")
            if choice.lower() == 'u':
                # Punto 1: Stampa gli user presenti nel database con un numero crescente
                print("Users in the database:")
                users = my_session.query(User).all()
                for i, user in enumerate(users, start=1):
                    print(f"{i}. Username: {user.username}, Name: {user.name}, Surname: {user.surname}, Email: {user.email}, Phone: {user.phone}, Password: {user.password}")

                # Punto 2: Permette di scegliere il numero dell'user da aggiornare e lo salva in una variabile
                user_choice = int(input("Enter the number of the user you want to update: "))
                if 1 <= user_choice <= len(users):
                    selected_user = users[user_choice - 1]
                else:
                    print("Invalid choice. Please choose a number within the range.")
                    return

                # Punto 3: Stampa gli user presenti in predefined_user
                print("\nUsers in predefined_user:")
                for i, predefined_user in enumerate(predefined_users, start=1):
                    print(f"{i}. Username: {predefined_user['username']}, Name: {predefined_user['name']}, Surname: {predefined_user['surname']}, Email: {predefined_user['email']}, Phone: {predefined_user['phone']}, Password: {predefined_user['password']}")

                # Punto 4: Permette di scegliere quale user sostituire alla variabile selezionata
                predefined_user_choice = int(input("Enter the number of the user from predefined_user to replace the selected user: "))
                if 1 <= predefined_user_choice <= len(predefined_users):
                    selected_predefined_user = predefined_users[predefined_user_choice - 1]
                else:
                    print("Invalid choice. Please choose a number within the range.")
                    return

                # Punto 5: Sostituisce i dati dell'user nel database con i dati dell'user scelto da predefined_user
                selected_user.username = selected_predefined_user['username']
                selected_user.name = selected_predefined_user['name']
                selected_user.surname = selected_predefined_user['surname']
                selected_user.email = selected_predefined_user['email']
                selected_user.phone = selected_predefined_user['phone']
                selected_user.password = selected_predefined_user['password']

                # Effettua il commit delle modifiche al database
                my_session.commit()

                # Punto 6: Stampa l'user che hai inserito
                print("\nUpdated user:")
                print(f"Username: {selected_user.username}, Name: {selected_user.name}, Surname: {selected_user.surname}, Email: {selected_user.email}, Phone: {selected_user.phone}, Password: {selected_user.password}")

                lollo = update_user(inname="Lorenzo", 
                                insurname="Amendola", 
                                inusername="iamlol",
                                inemail="oll@test.com",
                                inphone="123456789",
                                inpassowrd="drowssap",
                                my_session=my_session)
                print(lollo)

            elif choice.lower() == 'a':
                print("Available addresses:")
                for i, user in enumerate(predefined_users, start=1):
                    print(f"{i}. {user['name']}, {user['surname']}, {user['username']}, {user['email']}, {user['phone']}, {user['password']}")

                choice = int(input("Enter the number of the address you want to add: "))

                add_address2 = add_user2(choice=choice, my_session=my_session)
                my_session.commit()
                print(add_address2)
                lollo = add_user(inname="Lorenzo", 
                                insurname="Amendola", 
                                inusername="lol",
                                inemail="lol@test.com",
                                inphone="987654321",
                                inpassword="password",
                                my_session=my_session)
                print(lollo)

            elif choice.lower() == 'd':
                print("Current users:")
                users = my_session.query(User).all()
                for user in users:
                    print(f"Username: {user.username}, Name: {user.name}, Surname: {user.surname}")
                
                username_to_delete = input("----------------------\nEnter the username to delete: \n----------------------\n")
                
                result = delete_user(username_to_delete, my_session)
                my_session.commit()
                print(result)

            elif choice.lower() == 'q':
                print("Exiting...")
                break

if __name__ == "__main__":
    main()"""

"""def add_user(inname, insurname, inusername, inemail, inphone, inpassword, my_session):
    user = my_session.query(User).filter(User.name==inname, User.surname==insurname, User.username==inusername).first()

    if not user:
        new_user = User(
            name=inname,
            surname=insurname,
            username=inusername,
            email=inemail,
            phone=inphone,
            password=inpassword  
        )
        try:
            my_session.add(new_user)
            return f"Successfully added user {new_user.name} {new_user.surname} to the database"
        except SQLAlchemyError as err:
            my_session.rollback()  
            print(err)
            return f"Error adding user: {err}"
    else:
        return f"User with username {inusername} already exists in the database"

def update_user(inname, insurname, inusername, inemail, inphone, inpassword, my_session):
    user = my_session.query(User).filter(User.name==inname, User.surname==insurname).first()
    if user:
        user.name = inname
        user.surname = insurname
        user.username = inusername
        user.email = inemail
        user.phone = inphone
        user.password = inpassword

        try:
            return f"Successfully {user.name} {user.surname} modified in the database"
        except SQLAlchemyError as err:
            my_session.rollback()
            print(err)
            return f"Error: {err}"
    else:
        return f"User {inname} {insurname} does not exist in the database"

"""

"""def add_user(inname, insurname, inusername, inemail, inphone, inpassword, my_session):
    user = my_session.query(User).filter(User.name == inname, User.surname == insurname, User.username == inusername).first()
    if not user:
        new_user = User(
            name=inname,
            surname=insurname,
            username=inusername,
            email=inemail,
            phone=inphone,
            password=inpassword  
        )
        try:
            my_session.add(new_user)
            return f"Successfully added user {new_user.name} {new_user.surname} to the database"
        except SQLAlchemyError as err:
            my_session.rollback()  
            print(err)
            return f"Error adding user: {err}"
    else:
        return f"User with username {inusername} already exists in the database"

def update_user(inname, insurname, inusername, inemail, inphone, inpassword, my_session):
    user = my_session.query(User).filter(User.name == inname, User.surname == insurname).first()
    if user:
        user.name = inname
        user.surname = insurname
        user.username = inusername
        user.email = inemail
        user.phone = inphone
        user.password = inpassword
        try:
            return f"Successfully {user.name} {user.surname} modified in the database"
        except SQLAlchemyError as err:
            my_session.rollback()
            print(err)
            return f"Error: {err}"
    else:
        return f"User {inname} {insurname} does not exist in the database"

def delete_user(inusername, my_session):
    user = my_session.query(User).filter(User.username == inusername).first()
    if user:
        try:
            my_session.delete(user)
            return f"User {inusername} successfully deleted from the database"
        except SQLAlchemyError as err:
            my_session.rollback()
            print(err)
            return f"Error: {err}"
    else:
        return f"User with username {inusername} does not exist in the database"""