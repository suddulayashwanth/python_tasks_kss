import pandas as pd

logs = []

while True:
    action = input("Enter action or type exit: ")

    if action.lower() == "exit":
        break

    logs.append(action)

try:
    log_data = pd.DataFrame({"User Action": logs})

    log_data.to_csv("user_logs.txt", index=False)

    print("Logs saved successfully")

except OSError:
    print("Unable to save the logs")