# pytksqliteproj
A Simple Login application using tkinter and sqlite3 with two buttons Login and Register:

It accepts username and password from the user.and the application is connected to database through sqlite and checks if the user is already registered in the db. If user is already registered,it will show ‘Access Granted’ on c lick of Login
Else it will show ‘Access Denied .Please register’.
On clicking Register,it again checks if user is already registered and if registered displays the message ‘the user is already registered. Please Login’
Otherwise, the new username and password is inserted into the db and shows the success message and the user can login once registered.
