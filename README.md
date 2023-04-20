# API for Social network Yatube
### Описание
API предоставляет функционал по выполнению CRUD действий над публикациями, комментариями, подписками.  
Авторизация по токену. Неавторизованным пользователям предоставляется ограниченный функционал.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
### Примеры запросов
**GET** Получение списка публикаций  
URL: http://127.0.0.1:8000/api/v1/posts/  

Response (JSON):
```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2021-10-14T20:41:29.648Z",
    "image": "string",
    "group": 0
  }
]
}
```

**POST** Добавление комментария к публикации с {post_id}  
URL: http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/  
Body:
```
{
  "text": "string"
}
```

Response (JSON):
```
{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}
```

**POST** Создание подписки авторизованного пользователя на автора following  
URL: http://127.0.0.1:8000/api/v1/follow/  
Body:
```
{
  "following": "string"
}
```

Response (JSON):
```
{
"user": "string",
"following": "string"
}
```
