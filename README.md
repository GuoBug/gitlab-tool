# GitLab API Tool

This project aims to help manage personal GitLab instances. By using the GitLab API, we can access many different resources within a GitLab instance, such as projects, branches, tags, merge requests, users, etc. This project includes some scripts that can automatically perform common management tasks using the GitLab API, such as:

- Creating new projects
- Cloning existing projects
- Listing projects
- Getting project details
- Listing branches
- Listing tags
- Listing merge requests
- Listing users

This project is written in Python and uses the official GitLab Python client library `python-gitlab` to call the GitLab API.

## Usage

### 1. Install dependencies

Before using this project, make sure that Python 3 and the `python-gitlab` library are installed on your computer. You can install the `python-gitlab` library using the following command:

```sh
pip install python-gitlab
```

2. Configure GitLab API access token

To use the GitLab API, you need to generate a personal access token for GitLab. Follow the steps below to generate an access token:

1. Log in to your GitLab account.
2. Click on your avatar in the top right corner and select "Settings".
3. In the left menu, click "Access Tokens".
4. Enter a name for the access token and select the desired permissions.
5. Click "Create Personal Access Token".

Once you have generated the access token, you need to save it in an environment variable so that this project can use it to call the GitLab API. You can set the environment variable using the following command:

```sh
export GITLAB_PRIVATE_TOKEN=your_private_token_here
```
