# Flask API with Docker Hub + GitHub Actions

## Run locally with Python

```bash
pip install -r requirements.txt
python app.py
```

Open:
- http://localhost:5000/health
- http://localhost:5000/api/data

## Run from Docker Hub on Docker Desktop

Pull the image:

```bash
docker pull YOUR_DOCKER_USERNAME/flask-api:latest
```

Run the container:

```bash
docker run -d -p 5000:5000 --name flask-api YOUR_DOCKER_USERNAME/flask-api:latest
```

Test it:

```bash
curl http://localhost:5000/health
curl http://localhost:5000/api/data
```

## Run tests

```bash
pytest -q
```

## GitHub Actions setup

Add these repository secrets:
- DOCKER_USERNAME
- DOCKER_PASSWORD

Use a Docker Hub access token as the password value.
