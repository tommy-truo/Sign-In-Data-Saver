from os import system, name
from sys import exit
from time import sleep
import json
from cryptography.fernet import Fernet


#Clears console
def clear_console():
  sleep(0.7)
  if name == 'nt':
    system('cls')
  else:
    system('clear')


#Prints all main menu options to console
def display_choices():
  print("1. Print All Saved Data To Console")
  print("2. Add/Save New Data")
  print("3. Delete Certain Saved Data")
  print("4. Edit Existing Data")
  print("5. Change Program Password")
  print("6. Exit Program\n\n")


#Collects user input for main menu
def get_input():
  menu_options = ('1', '2', '3', '4', '5', '6')

  display_choices()

  menu_choice = input("What would you like to do?\n>>>> ")
  
  while menu_choice not in menu_options:
    sleep(0.7)
    print("\nPlease enter a valid option.\n")
    
    clear_console()
    
    display_choices()
    menu_choice = input("What would you like to do?\n>>>> ")

  return menu_choice


#Gets encryption/decryption key from key file, and generates new key if file doesn't exist
def get_encr_key():
  try:
    with open('sisKey.key', 'rb') as key_file:
      key = key_file.read()
    
  except:
    new_key = Fernet.generate_key()

    with open('sisKey.key', 'wb') as key_file:
      key_file.write(new_key)

    with open('sisKey.key', 'rb') as key_file:
      key = key_file.read()

  finally:
    return key


#Encrypts all data in JSON file and writes encrypted data to file
def encrypt():
  encr_key = get_encr_key()
  
  with open('sisData.json', 'rb') as json_file:
    file_data = json_file.read()
  
  fernet = Fernet(encr_key)

  encr_data = fernet.encrypt(file_data)

  with open('sisData.json', 'wb') as json_file:
    json_file.write(encr_data)


#Decrypts all encrypted data in JSON file and returns decrypted data, then re-encrypts data
def decrypt():
  decr_key = get_encr_key()

  with open('sisData.json', 'rb') as json_file:
    file_data = json_file.read()

  fernet = Fernet(decr_key)

  decr_data = fernet.decrypt(file_data)

  with open('sisData.json', 'wb') as json_file:
    json_file.write(decr_data)

  with open('sisData.json') as json_file:
    file_data = json.load(json_file)

  encrypt()

  return file_data


#Creates new JSON file and password if file is invalid
def invalid_file():
  print("Data file either doesn't exist or isn't accessible. Creating new data file (may result in data loss if file already existed)...\n\n")
    
  example_data = {"used_keys" : ["0"],
    "user_data" : {"0" : {
    "website" : "examplewebsite.com",
    "email" : "example@email.com",
    "password" : "ExamplePassword",
    "username" : "ExampleUsername",
    "phone_num" : "(123)456-7890"
        }
      }
    }
    
  sleep(0.7)

  clear_console()
  
  new_password = input("Please enter a new password (Remember this password, as it is neccessary to access and edit the file contents through this program).\n\n>>>> ")

  user_password = {"sis_password" : new_password}

  example_data.update(user_password)

  sleep(0.7)

  clear_console()

  with open('sisData.json', 'w') as json_file:
    json.dump(example_data, json_file, indent = 2)

  encrypt()
    
  print("New data file was created and is accessible.\n\n")


#Checks for JSON file, and creates new file if one doesn't exist/isn't accessible
def check_for_file():
  clear_console()
  
  print("Searching for data file...\n\n")
  
  sleep(0.7)

  try:
    file_data = decrypt()

    if len(file_data) < 3:
      invalid_file()
    
    elif len(file_data) == 3:
      print("Data file was found and is accessible.\n\n")
  
  except:
    invalid_file()
    
  finally:
    sleep(0.7)
    
    print("Do not delete/edit the files 'sisData.json' and 'sisDataKey.key' or data will be lost/corrupted.")

  clear_console()


#Generates key for new value in JSON dict, then stores used keys in array/list
def get_new_key():
  file_data = decrypt()

  new_key = 1

  while str(new_key) in file_data["used_keys"]:
    new_key += 1

  with open('sisData.json', 'w') as used_key_file:
    file_data["used_keys"].append(str(new_key))
    
    json.dump(file_data, used_key_file)

  encrypt()

  return new_key


#Collects and returns new inputted sign-in data
def collect_new_data():
  clear_console()
  
  check_for_file()
  
  website = input("Enter the WEBSITE/APPLICATION that will use this data (Enter 'cancel' to exit data creation screen):\n\n>>>> ")

  if website.lower() == 'cancel':
    clear_console()
    
    check_user_input()
  
  email = input("\n\nEnter the EMAIL that is used by the website (Enter 'cancel' to exit data creation screen):\n\n>>>> ")

  if email.lower() == 'cancel':
    clear_console()
    
    check_user_input()
  
  password = input("\n\nEnter the PASSWORD that is used by the website (Enter 'cancel' to exit data creation screen):\n\n>>>> ")

  if password.lower() == 'cancel':
    clear_console()
    
    check_user_input()
  
  username = input("\n\nEnter the USERNAME that is used by the website (Enter 'cancel' to exit data creation screen; if there's NO username, enter 'n/a'):\n\n>>>> ")
  if username.lower() == 'n/a':
    username = 'N/A'

  if username.lower() == 'cancel':
    clear_console()
    
    check_user_input()

  phone_num = input("\n\nEnter the PHONE NUMBER that is used by the website (Enter 'cancel' to exit data creation screen; if there's NO phone number, enter 'n/a'):\n\n>>>> ")
  
  if phone_num.lower() == 'n/a':
    phone_num = 'N/A'

  if phone_num.lower() == 'cancel':
    clear_console()
    
    check_user_input()

  return website, email, password, username, phone_num


#Allows user to select the data they want to modify
def select_data(modify):
  print_saved_data()

  selected_data = input("\nSelect the data you want to " + modify + " (Enter 'cancel' to exit this screen):\n\n>>>> ")

  if selected_data.lower() == 'cancel':
    sleep(0.7)
    
    clear_console()

    check_user_input()

  file_data = decrypt()

  if selected_data in file_data["used_keys"]:
    confirm = input("\n\nAre you sure you want to " + modify + ":\n\n" + selected_data + ". Website : " + file_data["user_data"][selected_data]["website"] + "\nEmail : " + file_data["user_data"][selected_data]["email"] +"\nPassword : " + file_data["user_data"][selected_data]["password"] +"\nUsername : " + file_data["user_data"][selected_data]["username"] + "\nPhone Number : " + file_data["user_data"][selected_data]["phone_num"] + "\n\n(Yes or No)\n\n>>>> ")

    while confirm.lower() not in ['yes', 'no']:
      print("\nThat is not an option.")

      sleep(0.7)

      clear_console()

      confirm = input("\n\nAre you sure you want to " + modify + ":\n\n" + selected_data + ". Website : " + file_data["user_data"][selected_data]["website"] + "\nEmail : " + file_data["user_data"][selected_data]["email"] +"\nPassword : " + file_data["user_data"][selected_data]["password"] +"\nUsername : " + file_data["user_data"][selected_data]["username"] + "\nPhone Number : " + file_data["user_data"][selected_data]["phone_num"] + "\n\n(Yes or No)\n\n>>>> ")

    if confirm.lower() == 'yes':
      return selected_data

    elif confirm.lower() == 'no':
      select_data(modify)

  else:
    print("\nThat is not an option.")

    select_data(modify)


# 1. Prints saved user data in JSON file to console
def print_saved_data():
  check_for_file()

  clear_console()
  
  file_data = decrypt()

  if len(file_data["user_data"]) == 0:
    print("Your data file has no saved user data.")

    sleep(0.7)

    print("\n\nIn order to print/change user data in JSON file, you must add user data first.")

    sleep(0.7)

    _ = input("\n\nEnter any key to continue:\n\n>>>> ")

    clear_console()
    
    check_user_input()
  
  else:
    for i in file_data["user_data"]:
      print(i + ". Website : " + file_data["user_data"][i]["website"])
      print("Email : " + file_data["user_data"][i]["email"])
      print("Password : " + file_data["user_data"][i]["password"])
      print("Username : " + file_data["user_data"][i]["username"])
      print("Phone Number : " + file_data["user_data"][i]["phone_num"] + "\n")

  sleep(0.7)


# 2. Adds new user data to JSON file
def add_new_data():
  website, email, password, username, phone_num = collect_new_data()
  
  dict_key = get_new_key()

  new_dict = {dict_key : {
    'website' : website.title(),
    'email' : email,
    'password' : password,
    'username' : username,
    'phone_num' : phone_num
    }
  }
  
  file_data = decrypt()

  file_data["user_data"].update(new_dict)

  with open('sisData.json', 'w') as json_file:
    json.dump(file_data, json_file)

  encrypt()

  sleep(0.7)
  
  print("\n\nNew saved data added.")



# 3. Deletes selected user data from JSON file
def delete_data():
  selected_data = select_data('delete')

  file_data = decrypt()
  
  file_data["used_keys"].remove(selected_data)

  del file_data["user_data"][selected_data]
      
  with open("sisData.json", "w") as json_file:
    json.dump(file_data, json_file)

  encrypt()

  sleep(0.7)
  
  print("\n\nSelected data was successfully deleted.")


# 4. Edits selected data in JSON file
def edit_data():
  selected_website = select_data('edit')
  
  clear_console()
  
  sleep(0.7)
  
  file_data = decrypt()
  
  print("1. Website : " + file_data["user_data"][selected_website]["website"] + "\n2. Email : " + file_data["user_data"][selected_website]["email"] +"\n3. Password : " + file_data["user_data"][selected_website]["password"] +"\n4. Username : " + file_data["user_data"][selected_website]["username"] + "\n5. Phone Number : " + file_data["user_data"][selected_website]["phone_num"])
  
  edited_info = input("\n\nWhat do you want to edit? (Enter '6' to Edit All Data or 'cancel' to exit the edit screen)\n\n>>>> ")
  
  while edited_info not in ['1', '2', '3', '4', '5', '6', 'cancel']:
    print("\nThat is not an option.")

    sleep(0.7)

    clear_console()

    print("1. Website : " + file_data["user_data"][selected_website]["website"] + "\n2. Email : " + file_data["user_data"][selected_website]["email"] +"\n3. Password : " + file_data["user_data"][selected_website]["password"] +"\n4. Username : " + file_data["user_data"][selected_website]["username"] + "\n5. Phone Number : " + file_data["user_data"][selected_website]["phone_num"])

    edited_info = input("\n\nWhat do you want to edit? (Enter '6' to Edit All Data or 'cancel' to exit the edit screen)\n\n>>>> ")
  
  if edited_info == '1':
    new_website = input("\n\nWhat would you like to change the website to? (Enter 'cancel' to exit the edit screen)\n\n>>>> ")

    if new_website.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["website"] = new_website

      with open("sisData.json", "w") as json_file:
        json.dump(file_data, json_file)

      encrypt()

  elif edited_info == '2':
    new_email = input("\n\nWhat would you like to change the email to? (Enter 'cancel' to exit the edit screen)\n\n>>>> ")

    if new_email.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["email"] = new_email

      with open("sisData.json", "w") as json_file:
        json.dump(file_data, json_file)

      encrypt()

  elif edited_info == '3':
    new_password = input("\n\nWhat would you like to change the password to? (Enter 'cancel' to exit the edit screen)\n\n>>>> ")

    if new_password.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["password"] = new_password

      with open("sisData.json", "w") as json_file:
        json.dump(file_data, json_file)

      encrypt()

  elif edited_info == '4':
    new_username = input("\n\nWhat would you like to change the username to? (Enter 'cancel' to exit the edit screen)\n\n>>>> ")

    if new_username.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["username"] = new_username

      with open("sisData.json", "w") as json_file:
        json.dump(file_data, json_file)

      encrypt()

  elif edited_info == '5':
    new_phone_num = input("\n\nWhat would you like to change the phone number to? (Enter 'cancel' to exit the edit screen)\n\n>>>> ")

    if new_phone_num.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["phone_num"] = new_phone_num

      with open("sisData.json", "w") as json_file:
        json.dump(file_data, json_file)

      encrypt()
  
  elif edited_info == '6':
    website, email, password, username, phone_num = collect_new_data()

    file_data["user_data"][selected_website]["website"] = website
    file_data["user_data"][selected_website]["email"] = email
    file_data["user_data"][selected_website]["password"] = password
    file_data["user_data"][selected_website]["username"] =username
    file_data["user_data"][selected_website]["phone_num"] = phone_num

    with open("sisData.json", "w") as json_file:
      json.dump(file_data, json_file)

    encrypt()

  elif edited_info.lower() == 'cancel':
    clear_console()

    check_user_input()

  print("\n\nSelected data was successfully edited.")


# 5. Changes Program Password in JSON file
def change_password():
  check_for_file()

  clear_console()

  file_data = decrypt()

  new_password = input("What would you like to change your program password to? (Enter 'cancel' to exit to main menu)\n\n>>>> ")

  if new_password.lower() == 'cancel':
    clear_console()
    
    check_user_input()

  else:
    confirm = input("\n\nAre you sure you want to change your program password to " + new_password + "? (Yes or No)\n\n>>>> ")

    while confirm.lower() not in ['yes', 'no']:
      print("\n\nThat is not an option.")

      clear_console()

      confirm = input("\n\nAre you sure you want to change your program password to " + new_password + "? (Yes or No)\n\n>>>> ")

    if confirm.lower() == 'yes':
      file_data["sis_password"] = new_password
    
      with open("sisData.json", "w") as json_file:
        json.dump(file_data, json_file)

      encrypt()

      sleep(0.7)
    
      print("\n\nSuccessfully changed program password.")

    elif confirm.lower() == 'no':
      change_password()


#Checks user input, then calls corresponding functions
def check_user_input():
  choice = get_input()
  
  if choice == '1':
    print_saved_data()

    _ = input("\nEnter any key to continue:\n\n>>>> ")

    clear_console()

    check_user_input()
  
  elif choice == '2':
    add_new_data()

    clear_console()

    check_user_input()
  
  elif choice == '3':
    delete_data()

    clear_console()

    check_user_input()

  elif choice == '4':
    edit_data()

    clear_console()

    check_user_input()
  
  elif choice == '5':
    change_password()

    clear_console()

    check_user_input()
  
  elif choice == '6':
    sleep(0.7)
    
    clear_console()
    
    print("\nGoodbye, and thank you for using this program.\n")
    
    sleep(0.7)
    
    exit('Program Exited')


#Creates/checks for user password before allowing user to see or edit JSON file
def password():
  clear_console()
  
  try:
    file_data = decrypt()

    if "sis_password" in file_data:
      inputted_password = input("Please enter your password to access this program:\n>>>> ")
      
      while inputted_password != file_data["sis_password"]:
        print("\n\nThat is not the correct password.")

        clear_console()

        inputted_password = input("Please enter your password to access this program:\n\n>>>> ")

    else:
      invalid_file()
  
  except:
    invalid_file()
  
  finally:
    clear_console()

    print("Accessing main menu...")

    clear_console()

    check_user_input()


def main():
  password()


if __name__== "__main__":
  main()