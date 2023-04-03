import requests

# GitLab API endpoint and personal access token
GITLAB_API_ENDPOINT = 'https://gitlab.com/api/v4'
PERSONAL_ACCESS_TOKEN = 'your_personal_access_token_here'

# Headers required for authentication
headers = {'PRIVATE-TOKEN': PERSONAL_ACCESS_TOKEN}

# User ID of the user whose information we want to retrieve
user_id = 123456

# Endpoint to retrieve information for a single user
user_endpoint = f'{GITLAB_API_ENDPOINT}/users/{user_id}'

# Retrieve user information
response = requests.get(user_endpoint, headers=headers)

# Print user information
if response.status_code == 200:
    user_info = response.json()
    print(f"User name: {user_info['name']}")
    print(f"User email: {user_info['email']}")
    print(f"User created at: {user_info['created_at']}")
    print(f"User last activity at: {user_info['last_activity_at']}")
else:
    print(f"Error retrieving user information. Status code: {response.status_code}")

