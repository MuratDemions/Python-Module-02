def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")

    elif operation_number == 1:
        result = 10 / 0

    elif operation_number == 2:
        open("/home/musipit/There_is_not_file")

    elif operation_number == 3:
        result = "hello" + 5
        print(result)


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===", end="\n\n")

    for index in range(5):
        print(f"Testing operation {index}...")

        try:
            garden_operations(index)
            print("Operation completed successfully", end="\n\n")

        except ValueError as error:
            print(f"Caught ValueError: {error}", end="\n\n")

        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}", end="\n\n")

        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}", end="\n\n")

        except TypeError as error:
            print(f"Caught TypeError: {error}", end="\n\n")

    print("All error types tested successfully!")


test_error_types()
