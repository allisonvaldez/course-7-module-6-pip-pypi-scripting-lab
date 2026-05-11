# Import datetime
from datetime import datetime

# Import request to fetach data from API
import requests

# Create log entries to write to the file
log_data = ["User logged in", "User updated profile", "Report exported"]

# Create a file name using correct date
filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"

# Open the file in write mode and place each entry log on its own line
with open(filename, "w") as file:
    for entry in log_data:
        file.write(f"{entry}\n")

# Print confirmation
print(f"Log written to {filename}")

# Create a funciton to fetch data from API
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
    # Call fetch_data and store the result
    post = fetch_data()
    # Print the title from the fetched post
    print("Fetched Post Title:", post.get("title", "No title found"))