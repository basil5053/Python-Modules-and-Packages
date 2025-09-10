import calc_utils
import weather_utils

def main():
    while True:
        try:
            num = float(input("Enter a number to calculate square and cube: "))
            break
        except ValueError:
            print("Error: please enter a valid number.")
    print(f"Square of {num} = {calc_utils.square(num)}")
    print(f"Cube of {num} = {calc_utils.cube(num)}")
    city = input("Enter a city name: ").strip()
    if city == "":
        city = "Riyadh"
    weather_utils.today_weather(city)
    weather_utils.forecast(city)
if __name__ == "__main__":
    main()
