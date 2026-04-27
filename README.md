# hello-python-app

A minimal Python API built with **Flask** that serves `Hello Python App` on `http://localhost:3000`.

## Project structure

```text
.
├── app.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
└── README.md
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
pip install -r requirements.txt
python app.py
```

Open:

```bash
http://localhost:3000
```

## Run with Docker

Build the image:

```bash
docker build -t hello-python-app .
```

Run the container:

```bash
docker run -p 3000:3000 hello-python-app
```

Open:

```bash
http://localhost:3000
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
