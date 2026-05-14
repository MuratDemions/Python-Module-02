def input_temperature(temp_str: str) -> int:
    temperature = int(temp_str)
    if temperature > 40:
        raise ValueError(f"{temperature}°C is too hot for plants (max 40°C)")
    if temperature < 0:
        raise ValueError(f"{temperature}°C is too cold for plants (min 0°C)")
    return temperature


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===", end="\n\n")
    test_values = ["25", "abc", "100", "-50"]
    for index in test_values:
        print(f"Input data is '{index}'")
        try:
            temperature = input_temperature(index)
            print(f"Temperature is now {temperature}°C", end="\n\n")
        except Exception as error:
            print(f"Caught input_temperature error: {error}", end="\n\n")
    print("All tests completed - program didn't crash!")


test_temperature()
