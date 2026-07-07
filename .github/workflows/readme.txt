Sign in to Docker Hub.
Go to Account Settings → Security.
Click New Access Token.
Give it a name such as GitHub Actions.
Copy the generated token immediately.
Then in GitHub:

Open your repository on GitHub.
Go to Settings → Secrets and variables → Actions.
Create these secrets:
DOCKER_USERNAME = your Docker Hub username
DOCKER_PASSWORD = the access token you just created