from os import system, name
from sys import exit
from time import sleep
import json


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
  print("5. Exit Program\n\n")


#Collects user input for main menu
def get_input():
  menu_options = ('1', '2', '3', '4', '5')

  display_choices()

  menu_choice = input("What would you like to do?\n>>>> ")
  
  while menu_choice not in menu_options:
    sleep(0.7)
    print("\nPlease enter a valid option.\n")
    
    clear_console()
    
    display_choices()
    menu_choice = input("What would you like to do?\n>>>> ")

  return menu_choice


#Creates new JSON file if file is invalid
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
    
  with open('sidsData.json', 'w') as json_file:
    json.dump(example_data, json_file, indent = 2)
    
  sleep(0.7)
    
  print("New data file was created and is accessible.\n\n")


#Checks for JSON file, and creates new file if one doesn't exist/isn't accessible
def check_for_file():
  clear_console()
  
  print("Searching for data file...\n\n")
  sleep(0.7)

  try:
    with open('sidsData.json') as json_file:
      file_data = json.load(json_file)

      if len(file_data) < 2:
        invalid_file()
    
      elif len(file_data) == 2:
        print("Data file was found and is accessible.\n\n")
  
  except:
    invalid_file()
    
  finally:
    sleep(0.7)
    
    print("Do not delete/edit the file 'sidsData.json' or data will be lost/corrupted.")

  clear_console()


#Generates new key for new value in JSON dict, then stores used keys in array/list
def get_new_key():
  with open("sidsData.json") as used_key_file:
    file_data = json.load(used_key_file)

  new_key = 1

  while str(new_key) in file_data["used_keys"]:
    new_key += 1

  with open('sidsData.json', 'w') as used_key_file:
    file_data["used_keys"].append(str(new_key))
    
    json.dump(file_data, used_key_file, indent = 2)

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

  selected_data = input("\nSelect the data you want to " + modify + " (Enter 'cancel' to exit this screen):\n>>>> ")

  if selected_data.lower() == 'cancel':
    sleep(0.7)
    
    clear_console()

    check_user_input()

  with open("sidsData.json") as json_file:
    file_data = json.load(json_file)

  if selected_data in file_data["used_keys"]:
    confirm = input("\n\nAre you sure you want to " + modify + ":\n\n" + selected_data + ". Website : " + file_data["user_data"][selected_data]["website"] + "\nEmail : " + file_data["user_data"][selected_data]["email"] +"\nPassword : " + file_data["user_data"][selected_data]["password"] +"\nUsername : " + file_data["user_data"][selected_data]["username"] + "\nPhone Number : " + file_data["user_data"][selected_data]["phone_num"] + "\n\n(Yes or No)\n>>>> ")

    while confirm.lower() not in ['yes', 'no']:
      print("\nThat is not an option.")

      sleep(0.7)

      clear_console()

      confirm = input("\n\nAre you sure you want to " + modify + ":\n\n" + selected_data + ". Website : " + file_data["user_data"][selected_data]["website"] + "\nEmail : " + file_data["user_data"][selected_data]["email"] +"\nPassword : " + file_data["user_data"][selected_data]["password"] +"\nUsername : " + file_data["user_data"][selected_data]["username"] + "\nPhone Number : " + file_data["user_data"][selected_data]["phone_num"] + "\n\n(Yes or No)\n>>>> ")

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
  
  with open("sidsData.json") as json_file:
    file_data = json.load(json_file)

  if len(file_data["user_data"]) == 0:
    print("Your data file has no saved user data.")

    sleep(0.7)

    print("\n\nIn order to print/change user data in JSON file, you must add user data first.")

    sleep(0.7)

    _ = input("\n\nEnter any key to continue:\n>>>> ")

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

  with open('sidsData.json', 'r+') as json_file:
    file_data = json.load(json_file)

    file_data["user_data"].update(new_dict)
  
    json_file.seek(0)

    json.dump(file_data, json_file, indent = 2)

  sleep(0.7)
  
  print("\n\nNew saved data added.")



# 3. Deletes selected user data from JSON file
def delete_data():
  selected_data = select_data('delete')

  with open("sidsData.json") as json_file:
    file_data = json.load(json_file)
  
  file_data["used_keys"].remove(selected_data)

  del file_data["user_data"][selected_data]
      
  with open("sidsData.json", "w") as json_file:
    json.dump(file_data, json_file, indent = 2)

  sleep(0.7)
  
  print("\n\nSelected data was successfully deleted.")


# 4. Edits selected data in JSON file
def edit_data():
  selected_website = select_data('edit')
  
  clear_console()
  
  sleep(0.7)
  
  with open("sidsData.json") as json_file:
    file_data = json.load(json_file)
  
  print("1. Website : " + file_data["user_data"][selected_website]["website"] + "\n2. Email : " + file_data["user_data"][selected_website]["email"] +"\n3. Password : " + file_data["user_data"][selected_website]["password"] +"\n4. Username : " + file_data["user_data"][selected_website]["username"] + "\n5. Phone Number : " + file_data["user_data"][selected_website]["phone_num"])
  
  edited_info = input("\n\nWhat do you want to edit? (Enter '6' to Edit All Data or 'cancel' to exit the edit screen)\n>>>> ")
  
  while edited_info not in ['1', '2', '3', '4', '5', '6', 'cancel']:
    print("\nThat is not an option.")

    sleep(0.7)

    clear_console()

    print("1. Website : " + file_data["user_data"][selected_website]["website"] + "\n2. Email : " + file_data["user_data"][selected_website]["email"] +"\n3. Password : " + file_data["user_data"][selected_website]["password"] +"\n4. Username : " + file_data["user_data"][selected_website]["username"] + "\n5. Phone Number : " + file_data["user_data"][selected_website]["phone_num"])

    edited_info = input("\n\nWhat do you want to edit? (Enter '6' to Edit All Data or 'cancel' to exit the edit screen)\n>>>> ")
  
  if edited_info == '1':
    new_website = input("\n\nWhat would you like to change the website to? (Enter 'cancel' to exit the edit screen)\n>>>> ")

    if new_website.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["website"] = new_website

      with open("sidsData.json", "w") as json_file:
        json.dump(file_data, json_file, indent = 2)

  elif edited_info == '2':
    new_email = input("\n\nWhat would you like to change the email to? (Enter 'cancel' to exit the edit screen)\n>>>> ")

    if new_email.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["email"] = new_email

      with open("sidsData.json", "w") as json_file:
        json.dump(file_data, json_file, indent = 2)

  elif edited_info == '3':
    new_password = input("\n\nWhat would you like to change the password to? (Enter 'cancel' to exit the edit screen)\n>>>> ")

    if new_password.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["password"] = new_password

      with open("sidsData.json", "w") as json_file:
        json.dump(file_data, json_file, indent = 2)

  elif edited_info == '4':
    new_username = input("\n\nWhat would you like to change the username to? (Enter 'cancel' to exit the edit screen)\n>>>> ")

    if new_username.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["username"] = new_username

      with open("sidsData.json", "w") as json_file:
        json.dump(file_data, json_file, indent = 2)

  elif edited_info == '5':
    new_phone_num = input("\n\nWhat would you like to change the phone number to? (Enter 'cancel' to exit the edit screen)\n>>>> ")

    if new_phone_num.lower() == 'cancel':
      clear_console()

      check_user_input()

    else:
      file_data["user_data"][selected_website]["phone_num"] = new_phone_num

      with open("sidsData.json", "w") as json_file:
        json.dump(file_data, json_file, indent = 2)
  
  elif edited_info == '6':
    website, email, password, username, phone_num = collect_new_data()

    file_data["user_data"][selected_website]["website"] = website
    file_data["user_data"][selected_website]["email"] = email
    file_data["user_data"][selected_website]["password"] = password
    file_data["user_data"][selected_website]["username"] =username
    file_data["user_data"][selected_website]["phone_num"] = phone_num

    with open("sidsData.json", "w") as json_file:
      json.dump(file_data, json_file, indent = 2)

  elif edited_info.lower() == 'cancel':
    clear_console()

    check_user_input()

  print("Selected data was successfully edited.")


#Checks user input, then calls corresponding functions
def check_user_input():
  choice = get_input()
  
  if choice == '1':
    print_saved_data()

    _ = input("\nEnter any key to continue:\n>>>> ")

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
    sleep(0.7)
    
    print("\nGoodbye, and thank you for using this program.\n")
    
    sleep(0.7)
    
    exit('Program Exited')


def main():
  check_user_input()


if __name__== "__main__":
  main()