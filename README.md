# GilanJan Backend

This is the backend of the **GilanJan** project, built with Django and Django REST Framework. It powers a real estate platform for listing and booking properties across Gilan province. The backend handles user authentication, real-time messaging, property management, and API endpoints consumed by the Next.js frontend.

---

## 🚀 Features

- JWT authentication with `dj-rest-auth` & `django-allauth`
- Real-time updates via `channels` and `daphne`
- PostgreSQL database support using `psycopg2`
- Media and image handling using `Pillow`
- Secure CORS handling for cross-origin requests
- Rich text editing with `django-ckeditor-5`
- Auto-generated API documentation using `drf-yasg`
- Environment variable support via `.env`
- Production-ready deployment setup using `gunicorn`

---

## 🛠️ Tech Stack

- **Framework**: Django 5.0.2
- **API**: Django REST Framework
- **Auth**: dj-rest-auth + SimpleJWT + allauth
- **Database**: PostgreSQL
- **Docs**: drf-yasg
- **WebSocket**: Django Channels & Daphne
- **Rich Editor**: django-ckeditor-5

---

## 📦 Installed Packages

```txt
Django==5.0.2
dj-rest-auth==4.0.0
django-allauth==0.52.0
django-cors-headers==4.3.1
djangorestframework==3.14.0
djangorestframework-simplejwt==5.3.1
psycopg2-binary==2.9.9
pillow==10.2.0
channels==4.0.0
daphne==4.0.0
gunicorn==21.2.0
python-dotenv==1.0.1
drf-yasg==1.21.7
asgiref==3.8.1
PyJWT==2.10.0
sqlparse==0.5.2
typing_extensions==4.12.2
tzdata==2024.2
django-ckeditor-5==0.2.15
```

---

## 📁 Project Structure (simplified)

```
gilanjan-backend/
├── core/
│   ├── models/
│   ├── views/
│   ├── serializers/
│   └── urls.py
├── media/
├── static/
├── .env
├── manage.py
└── requirements.txt
```

---

## ⚙️ Setup Instructions

1. Clone the repo:
```bash
git clone https://github.com/your-username/gilanjan-backend.git
cd gilanjan-backend
```

2. Create virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Add a `.env` file:
```env
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_postgres_url
```

4. Run the project:
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🧪 API Docs
Visit: `http://localhost:8000/swagger/`

---

## 📬 Contact
Built by **Maryam** | [maryyam.dev](https://maryyam.dev)

---

> Make sure to check out the frontend repo built with Next.js and React for the full experience.
