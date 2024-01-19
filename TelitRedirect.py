import webbrowser
from datetime import datetime

def open_url_with_id():
    while True:
        # Get user input for the ID
        user_id = input("Enter the ID (or type 'exit' to end): ")

        # Check if the user wants to exit
        if user_id.lower() == 'exit':
            break

        # Get today's date in the desired format (YYYY-MM-DD)
        today_date = datetime.now().strftime("%Y-%m-%d")

        # Construct the URL using the provided ID and today's date
        url = f"https://portal-de.telit.com/things/property/{user_id}/prop_temperature?start=2023-09-01+10%3A00%3A00&end={today_date}+23%3A59%3A59"

        
        # Open the URL in the default web browser
        webbrowser.open(url)

if __name__ == "__main__":
    open_url_with_id()
