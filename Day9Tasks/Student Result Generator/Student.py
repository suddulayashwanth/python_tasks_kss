class Result:
    def calculate_result(self, subject1, subject2, subject3=None):
        if subject3 is None:
            total = subject1 + subject2
            average = total / 2
        else:
            total = subject1 + subject2 + subject3
            average = total / 3

        print("Total Marks:", total)
        print("Average Marks:", average)


result = Result()

print("Result using two subjects:")
result.calculate_result(80, 90)

print("\nResult using three subjects:")
result.calculate_result(80, 90, 85)