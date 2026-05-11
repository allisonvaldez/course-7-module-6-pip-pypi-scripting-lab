# Import datetime
from datetime import datetime

# Import request to fetch data from API
import requests

# generate_log function — creates a log file from a list of entries
def generate_log(log_data):
    # Validate input — raise ValueError if log_data is not a list
    if not isinstance(log_data, list):
        raise ValueError("log_data must be a list")

    # Create a file name using correct date
    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

    # Open the file in write mode and place each entry log on its own line
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    # Print confirmation
    print(f"Log written to {filename}")

    # Return filename so tests can verify it
    return filename

# Create a function to fetch data from API
def fetch_data():
    # Get request
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    # Check status of request
    if response.status_code == 200:
        # Return data in JSON
        return response.json()
    # Return empty if otherwise
    return {}

if __name__ == "__main__":
    # Create log entries to write to the file
    log_data = ["User logged in", "User updated profile", "Report exported"]
    # Call generate_log with the list
    generate_log(log_data)
    # Call fetch_data and store the result
    post = fetch_data()
    # Print the title from the fetched post
    print("Fetched Post Title:", post.get("title", "No title found"))