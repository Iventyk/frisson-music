# Frisson Music

**Frisson Music** is a community-driven OST hub where users can discover, rate, and comment on soundtracks from movies, series, anime, and games. The platform is designed to provide structured and accurate information about OST albums, allowing the community to collaboratively maintain and improve the database.

---

## Project Overview

- **Purpose:**  
  Frisson Music aims to provide a clean and structured mapping of OST albums to their respective media (movies, series, anime, games), including season/part information, release dates, artists, and tracklists.  

- **Community-driven:**  
  Users can add new albums or edit existing ones, but all submissions must be verified for accuracy. Incorrect or misleading data can result in account suspension.

- **Key Features:**  
  - Browse albums by media type or media title.  
  - Filter and search albums by title.  
  - Rate albums with a 1-5 star system.  
  - Leave comments on albums.  
  - Display average ratings and personal ratings.  
  - Pagination for large album lists.  
  - Dark theme with consistent UI styling.  
  - Fully responsive design using Bootstrap.  

---

## Technical Details

- **Framework:** Django 6.0  
- **Database:** SQLite (development) / Postgres or MySQL (production)  
- **Frontend:** Bootstrap 5, custom CSS, JavaScript for interactive rating stars  
- **API Integration:** Spotify API (optional) for populating albums  
- **Templates:** Jinja2/Django templates, consistent dark theme  
- **Static Files:** Stored in `static/`, including CSS, JS, and images  
- **Templates:** Stored in `templates/frisson_music/`

---

## Populating the Database

- Edit `populate_db.py` file to use your own search parameters
- Use `python populate_db.py` command to run script 

---

## UI Template

- https://demos.creative-tim.com/black-dashboard/examples/dashboard.html

---

## Data Base Diagram

![Data_Base_Diagram](DB_Diagram.drawio.png)

---

## Test Users

- superuser `mine@gmail.com` `qqq333qqq`
- other `test@gmail.com` `poiuy098`