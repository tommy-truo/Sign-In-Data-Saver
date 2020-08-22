# Sign-In Data Saver
**[NOT FINISHED]**
Sign-In Data Saver is a python program that allows users to add, edit, and save sign-in information to a JSON file. Users can easily edit sign-in information for many different websites/applications and save the information to the data file.

**Note: In the event that the data file is _deleted/corrupted_, the program will _create/overwrite_ the previous file, which may result in _losing file data_ if the file was corrupted or unreadable.**

**Security Note:**

**Since the JSON file is _only_ saved on your computer and _not_ sent to any online server/database, your information _isn't_ accessible/editable by anyone else _unless_ your computer has some kind of _virus_ or your physical _hard drive/ssd_ that stored the JSON file was _stolen_ from your computer.**

**Also, the JSON file is currently _not_ encrypted by the program. So, your information _is_ readable to others if they open the JSON file on your personal computer. This will be changed in the final version of the program. The program currently doesn't have a password feature as well, which would only allow the user to see the saved information if the correct password was entered.**

## Add New User Info
Users can add new sign-in information into the JSON file using the program with ease. In the main menu, users enter the number 2, then enter the neccessary sign-in information and the website/application that uses that sign-in information. Then, the program automatically formats the new data and appends it to the JSON file to be saved for later use.

## Select and Delete User Info
Users can also easily delete information from the JSON file using the program. Users enter the number 3 in the main menu, then select and confirm the deletion of sign-in information for a specific website/application. Then, the program permanently removes the selected information from the file.

## Print User Info to Console
In order to see all of the information in the JSON file at once, users can print all of the saved sign-in information to the console. When all of the security features are implemented, the JSON file will be completely unreadable unless it is decrypted by the program. The program will also be inaccessible unless the user enters their password in order to access their information.