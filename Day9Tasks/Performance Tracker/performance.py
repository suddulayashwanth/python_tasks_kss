import time


def measure_time(function):
    def wrapper():
        start_time = time.time()

        function()

        end_time = time.time()
        execution_time = end_time - start_time

        print("Execution time:", execution_time, "seconds")

    return wrapper


@measure_time
def perform_task():
    total = 0

    for number in range(1, 1000001):
        total += number

    print("Task completed.")


perform_task()