# Django Blog API

## Tech Stack
- Django
- Django REST Framework
- SQLite (default database)
- Django-filter

## Installation

### Clone the Repository
```bash
git clone https://github.com/niranjanl08/Django_Blog_API.git
cd Django_Blog_API
```

### Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Requirements
```bash
pip install -r requirements.txt
```

## Database Setup

### Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Server
```bash
python manage.py runserver
```

The server will run at: **http://127.0.0.1:8000/**

## API Endpoints

### Posts
- **CRUD Operations**: `http://127.0.0.1:8000/api/posts/`
  - POST: Create a new post
  - GET: Retrieve all posts
  - PUT: Update a post (mention id)
  - DELETE: Delete a post (mention id)

### Comments
- **CRUD Operations**: `http://127.0.0.1:8000/api/comments/`
  - POST: Create a new comment
  - GET: Retrieve all comments
  - PUT: Update a comment (mention id)
  - DELETE: Delete a comment (mention id)

## Filtering & Searching

### Filter by Author
```
GET /api/posts/?author=NAME
```

### Search
```
GET /api/posts/?search=keyword
```

### Ordering
```
GET /api/posts/?ordering=-created_at  # Descending order
GET /api/posts/?ordering=created_at   # Ascending order
```

## Sample JSON Payloads

### Create/Update Post
```json
{
  "title_blog": "My Blog",
  "content_of_blog": "This is the json template",
  "author_of_blog": "team"
}
```

### Create/Update Comment
```json
{
  "name_of_person": "VishnuNerengen",
  "email_id": "vishnunerengen@gmail.com",
  "comment": "Great blog!",
  "post_name": 1
}
```