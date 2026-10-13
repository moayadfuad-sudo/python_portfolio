#fix_the_session.py
#this program reports a user's session time.

username = input("Username: ")
#Runtime error: changed the input to int to convert the string input to an integer
total_seconds = int(input("Session length in seconds: "))

#semantic error: chang the / opperator to // to convert the seconds to minutes
minutes = total_seconds // 60
seconds = total_seconds % 60

print("=" * 30)
#symantic error: added f prefex the variable {username} insted of printing it as a string
print(f"User: {username}")
#Runtime error: converted minutes to string to concatenate it with other strings
print( "Session: " + str(minutes) + " min " + str(seconds) + " s")
print("=" * 30)