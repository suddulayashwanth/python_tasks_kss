import pandas as pd

sample_logs = ["INFO Login successful", "ERROR Invalid password", "ERROR File not found", "ERROR Invalid password"]

log_data = pd.DataFrame({"Log": sample_logs})

log_data.to_csv("logs.txt", index=False, header=False)


def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()


errors = []

try:
    for log in read_logs("logs.txt"):
        if "ERROR" in log:
            error_message = log.replace("ERROR ", "")

            errors.append(error_message)

            print(log)

except OSError:
    print("Unable to read the log file")

error_series = pd.Series(errors)

error_counts = error_series.value_counts().to_dict()

print("Error occurrences:", error_counts)