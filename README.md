[![wakatime](https://wakatime.com/badge/user/ddd893b9-21da-4cb4-9172-465025e48d6b/project/93c4c1be-2695-4d26-a35d-13d5c789bf9f.svg)](https://wakatime.com/projects/frisson_music)

## 🎵 Frisson Music

**Frisson Music** is a community-driven OST hub for discovering, rating, and discussing soundtracks from movies, series, anime, and games.

The main goal of the project is to solve a common problem: **lack of structured and accurate OST-to-media mapping**.  
Here, albums are clearly linked to media, seasons, parts, and release context — and maintained collaboratively by the community.

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![python-dotenv](https://img.shields.io/badge/python--dotenv-000000?style=for-the-badge)
![spotipy](https://img.shields.io/badge/Spotipy-1DB954?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)

![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Jinja2](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge)


![pytest](https://img.shields.io/badge/pytest-15416C?style=for-the-badge&logo=pytest&logoColor=white)
![black](https://img.shields.io/badge/Black-000000?style=for-the-badge)
![flake8](https://img.shields.io/badge/Flake8-4B8BBE?style=for-the-badge)


---
## 🌍 Deployed Application

Live version of the project available here:  

-  https://frisson-music.onrender.com

---

## 🚀 Features

- Browse OST albums by:
  - Media type (Movie / Series / Anime / Game)
  - Specific media title
- Search albums by title
- Rate albums using a 1–5 star system
- View:
  - Average album rating
  - Your personal rating
- Leave comments on albums
- Pagination for large album lists
- Dark-themed UI based on **Black Dashboard**
- Fully responsive layout (desktop & mobile)
- Community-driven moderation:
  - Users can suggest edits
  - Incorrect or misleading data may result in account suspension

---

## 🧠 Project Philosophy

Frisson Music is built around **community trust and data accuracy**.

Instead of chaotic OST dumps, the platform enforces a structured hierarchy:

Media → Seasons / Parts → OST Albums → Tracks

This allows users to:
- Clearly understand where an OST belongs
- Avoid duplicated or incorrectly labeled albums
- Maintain high-quality metadata over time

---

## 🛠 Tech Stack

- **Backend:** Django
- **Database:**  
  - SQLite (development)  
  - PostgreSQL (production)
- **Frontend:**  
  - Bootstrap  
  - Custom CSS  
  - JavaScript (interactive rating stars)
- **UI Template:**  
  - Black Dashboard (Creative Tim)
- **Static files:**  
  - CSS, JS, icons, images stored in `static/`
- **Templates:**  
  - Django templates

---

## 🔌 Spotify API Integration

The project supports optional database population via **Spotify API**.

### Populate Database

- Edit `populate_db.py` file to use your own search parameters
1. Configure Spotify credentials
2. Edit search parameters inside:

- Use `python populate_db.py` command to run script (bash)

---

## Test Users

- superuser `mine@gmail.com` `qqq333qqq`
- other `test@gmail.com` `poiuy098`

---

## 📦 Installation (Development)

- `git clone https://github.com/your-username/frisson_music.git`
- `cd frisson_music`
- `python -m venv venv`
- `source venv/bin/activate`  # Windows: `venv\Scripts\activate`
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

---

## Data Base Diagram

![Data_Base_Diagram](DB_Diagram.drawio.png)

---

## UI Template

- https://demos.creative-tim.com/black-dashboard/examples/dashboard.html
- https://github.com/creativetimofficial/black-dashboard
