"# news" 
clone this project:https://github.com/SDeVPro/news
after:
create virtualenv: =>
pip install virtualenv
virtualenv env 
cd env
Scripts\activate
cd ..
after:
pip install -r req.txt
after:
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

#http://127.0.0.1:8000/admin/
admin: voy
password: admin123

