import requests

while True:
    city = input("Enter city name: ")

    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url)

    weather = response.text
    print(weather)

    while True:
        choice = input("Do you want to check the weather for another city? (yes/no): ").lower()

        if choice == "yes":
            break
        elif choice == "no":
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            print("<------------------------------------------>")