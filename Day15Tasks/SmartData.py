import time

import pandas as pd


def execution_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        result = function(*args, **kwargs)

        end_time = time.time()

        print("Execution time:", end_time - start_time)

        return result

    return wrapper


def stream_numbers(filename):
    with open(filename, "r") as file:
        for line in file:
            try:
                yield float(line.strip())

            except ValueError:
                print("Invalid data ignored:", line.strip())


@execution_time
def process_data(filename):
    try:
        numbers = list(stream_numbers(filename))

        if len(numbers) == 0:
            raise ValueError("No valid numbers found")

        number_series = pd.Series(numbers)

        mean_value = number_series.mean()

        standard_deviation = number_series.std()

        maximum_value = number_series.max()

        minimum_value = number_series.min()

        result = pd.DataFrame({
            "Mean": [mean_value],
            "Standard Deviation": [standard_deviation],
            "Maximum": [maximum_value],
            "Minimum": [minimum_value]
        })

        print(result)

    except FileNotFoundError:
        print("File not found")

    except ValueError as error:
        print(error)

    except OSError:
        print("Unable to read the file")


number_data = pd.DataFrame({"Numbers": [10, 20, "invalid", 30, 40, 50]})

number_data.to_csv("numbers.txt", index=False, header=False)

process_data("numbers.txt")