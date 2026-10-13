#session_timer.py
total_seconds =int(input("session length in seconds: "))
#calculate a whole minutes and the seconds left
minutes = total_seconds//60
seconds = total_seconds%60
print(f"sessio length: {minutes}:{seconds}")
#in first_test this is the result: session length: 15:5
#in sec_test this is the result: session length: 1:0
#in final_test this is the result: session length: 0:59