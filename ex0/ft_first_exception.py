def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===", end="\n\n")

    test_values = ["25", "abc"]

    for index in test_values:
        print(f"Input data is '{index}'")

        try:
            temperature = input_temperature(index)
            print(f"Temperature is now {temperature}°C", end="\n\n")
        except Exception as error:
            print(f"Caught input_temperature error: {error}", end="\n\n")

    print("All tests completed - program didn't crash!")


test_temperature()
