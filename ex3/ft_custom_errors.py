class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unknown plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unknown water error") -> None:
        super().__init__(message)


def test_plant() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water() -> None:
    raise WaterError("Not enough water in the tank!")


def main() -> None:
    print("=== Custom Garden Errors Demo ===", end="\n\n")

    print("Testing PlantError...")
    try:
        test_plant()
    except PlantError as error:
        print(f"Caught PlantError: {error}", end="\n\n")

    print("Testing WaterError...")
    try:
        test_water()
    except WaterError as error:
        print(f"Caught WaterError: {error}", end="\n\n")

    print("Testing catching all garden errors...")

    try:
        test_plant()
    except GardenError as error:
        print(f"Caught GardenError: {error}", end="\n\n")

    try:
        test_water()
    except GardenError as error:
        print(f"Caught GardenError: {error}", end="\n\n")

    print("All custom error types work correctly!")


main()
