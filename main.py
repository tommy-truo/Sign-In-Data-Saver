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


#Checks user input, then calls corresponding functions
def check_user_input():
  choice = get_input()
  
  if choice == '1':
    print("\n\nUser chose option 1.")
  
  elif choice == '2':
    print("\n\nUser chose option 2.")
  
  elif choice == '3':
    print("\n\nUser chose option 3.")

  elif choice == '4':
    print("\n\nUser chose option 4.")
  
  elif choice == '5':
    sleep(0.7)
    
    print("\nGoodbye, and thank you for using this program.\n")
    
    sleep(0.7)
    
    exit('Program Exited')


def main():
  check_user_input()


if __name__== "__main__":
  main()