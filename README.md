# hello-python-app

A minimal Python web app that serves **Hello Python App** on **http://localhost:8080**.

## Run locally

```bash
python app.py
```

Open:

```bash
http://localhost:8080
```

## Run with Docker

Build the image:

```bash
docker build -t hello-python-app .
```

Run the container:

```bash
docker run -p 8080:8080 hello-python-app
```

Open:

```bash
http://localhost:8080
```

## Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-user>/<your-repo>.git
git push -u origin main
```
