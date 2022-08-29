# Wiki starter in Django

## How To Setup

```
git clone https://github.com/minotaurdsp/miki.git
```

### Make new env

```
python3 -m venv venv
```

### Activate env

```
source venv/bin/activate
```

### Install requirements

```
pip install -r miki/requirements.txt
```

### Change directory

```
cd miki/miki
```

### Init new db shema 

```
python manage.py makemigrations
python manage.py migrate
```

### Import demo data

```
python manage.py loaddata fixtures/pages-demo-data.json
```

### Start app

```
python manage.py runserver

```

### Demo accounts

```
http://127.0.0.1:8000/admin

Demo Admin account
u:admin
p:admin123456

User Account with reduced permissions
Demo user account
u:base_user
p:test123456

```
