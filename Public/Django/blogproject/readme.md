##**Teck Stack**
    Django
    Django REST Framework
    SQLite (default database)
    Django-filter

---
git clone https://github.com/niranjanl08/Django_Blog_API.git
cd blogproject
---
**INSTALL Requirements**
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
---
**RUN MIGRATIONS**
python manage.py makemigrations
python manage.py migrate
---
**RUN SERVER**
python manage.py runserver

SERVER RUNS at : http://127.0.0.1:8000/

ON POSTs:  PERFORM CRUD(POST,GET,DELETE,PUT) on http://127.0.0.1:8000/api/posts (mention id for delete,put operations)
DO the same for comments
---
**FILTER**
BY AUTHOR : /api/posts/?author="NAME"
search : /api/posts/?search=keyword
ordering : /api/posts/?ordering=-created_at --to do desc :/api/posts/?ordering=-created_at


**Sample JSON POST:**
{
    "title_blog": "My Blog",
    "content_of_blog": "This is the json template",
    "author_of_blog": "team"
}

**Sample JSON Comment:**
{
    "name_of_person": "VishnuNerengen",
    "email_id": "vishnunerengen@gmail.com",
    "comment": "Great blog!",
    "post_name": 1
}
