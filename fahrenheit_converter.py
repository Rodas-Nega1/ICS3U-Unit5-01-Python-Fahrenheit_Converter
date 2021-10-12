# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user for the temperature in celsius
# then converts it into fahrenheit


def fahrenheit_conversion():
    # convert user celsius to fahrenheit

    # input
    user_temperature = input("Enter a temperature (°C): ")
    print("")

    # process
    try:
        user_temperature_int = int(user_temperature)

        convert_fahrenheit = (9 / 5) * user_temperature_int + 32

        print(
            "{0}°C is equal to {1}°F".format(user_temperature_int, convert_fahrenheit)
        )

    except Exception:
        print("That is an invalid integer.")

    finally:
        print("\nDone.")


def main():
    # this function calls the precedent function

    # call function
    fahrenheit_conversion()


if __name__ == "__main__":
    main()
