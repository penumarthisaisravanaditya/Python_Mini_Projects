# pip install requests python-dotenv

import os
import requests
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()

key = os.getenv("OPENWEATHER_API_KEY")

if not key:
    print("Error: OPENWEATHER_API_KEY is not set in the .env file.")
    exit()

while True:
    city = input("\nEnter city name: ").strip()

    if not city:
        print("Please enter a city name.")
        continue

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={key}&units=metric"
    )

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        # Check API response
        if response.status_code == 200:
            print("\n<------------------------------------------>")
            print("Weather Information")
            print("<------------------------------------------>")

            print("City:", data["name"])
            print("Country:", data["sys"]["country"])
            print("Temperature:", data["main"]["temp"], "°C")
            print("Feels Like:", data["main"]["feels_like"], "°C")
            print("Weather:", data["weather"][0]["description"])
            print("Humidity:", data["main"]["humidity"], "%")
            print("Wind Speed:", data["wind"]["speed"], "m/s")

            print("<------------------------------------------>")

        elif response.status_code == 404:
            print("Error: City not found. Please check the city name.")

        elif response.status_code == 401:
            print("Error: Invalid API key.")

        elif response.status_code == 429:
            print("Error: API request limit exceeded.")

        else:
            print("Error:", data.get("message", "Something went wrong."))

    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the internet.")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    # Ask whether to continue
    while True:
        choice = input(
            "\nDo you want to check the weather for another city? (yes/no): "
        ).lower().strip()

        if choice == "yes":
            break

        elif choice == "no":
            print("Thank you for using the Weather App!")
            exit()

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
