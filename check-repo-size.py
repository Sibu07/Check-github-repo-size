import requests
import re

def get_repository_size(repo_link, access_token):
    # Extract owner and repository name from the link
    match = re.search(r"github.com/([^/]+)/([^/]+)", repo_link)
    if match:
        owner = match.group(1)
        repo = match.group(2)
    else:
        print("Invalid repository link.")
        return None

    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        size = data['size']
        return size
    else:
        print(f"Failed to retrieve the repository size for {repo_link}.")
        return None

# Helper function to convert size to human-readable format
def convert_size(size):
    # Convert to kilobytes (KB)
    if size < 1024:
        return f"{size} KB"
    # Convert to megabytes (MB)
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} MB"
    # Convert to gigabytes (GB)
    else:
        return f"{size / (1024 * 1024):.2f} GB"

# Usage example
repository_link = input("Enter the GitHub repository link: ")
access_token = "[put Your Api Token Here]"

repository_size = get_repository_size(repository_link, access_token)
if repository_size:
    formatted_size = convert_size(repository_size)
    print(f"The size of the repository is {formatted_size}.")
