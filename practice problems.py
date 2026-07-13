
correct_password = "python123"
max_attempts=3

for attempt in range(max_attempts):
    password=input("enter password:")

if password == correct_password:
    print("access granted")
    "break"
else:
    remaining = max_attempts - attempt -1
    if remaining>0:
        print("incorrect password" , remaining)
    else:
        print("too many incorrect attempts")