# Django Blog - Learning Project

This repository contains the code I am writing while following the excellent [Python Django Tutorial Series by Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p). 

The purpose of this project is to learn and practice building a full-featured web application from scratch using Django.

## 📚 Concepts Covered
Throughout this tutorial, I am learning and implementing the following concepts:
- Django Project & App Structure
- URL Routing and Views
- Django Templates and Static Files (HTML, CSS, Bootstrap)
- Models, Database Migrations, and Django ORM
- The Django Admin Interface
- User Registration, Login, and Authentication
- User Profiles and Image Uploads (Signals)
- Class-Based Views (CRUD operations: Create, Read, Update, Delete)
- Pagination
- Password Reset functionality

## 🛠️ Tech Stack
- **Language:** Python 3
- **Framework:** Django 
- **Database:** SQLite (Default for development)
- **Environment:** macOS, VS Code

## 🚀 How to Run Locally

If you want to run this project on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Abitesh/django-blog.git
   cd django-blog
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv django_env
   source django_env/bin/activate
   ```

3. **Install Django (and other dependencies):**
   ```bash
   pip install django
   # (Will add a requirements.txt later if needed)
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.

## 📝 Acknowledgements
All credit for the tutorial content and project design goes to [Corey Schafer](https://www.youtube.com/c/CoreyMSchafer). This repository is strictly for my personal learning, practice, and reference.
