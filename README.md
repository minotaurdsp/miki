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
pip install -r requirements.txt
```

### Import demo data

```
python manage.py makemigrations
```

### Import demo data

```
python manage.py loaddata pages-demo-data.json
```

### Start app

```
python manage.py makemigrations
python manage.py migrate
```

### Demo accounts

```
http://127.0.0.1:8000/admin

Demo Admin account
admin
admin123456

User Account with reduced permissions
Demo user account
test123456

```
