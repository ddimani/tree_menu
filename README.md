# tree_menu

## Приложение для отрисовки древовидного меню на Django с помощью templatetag

### Описание 
Простое Django приложение для отрисовки древовидного меню, реализованное через templatetag.
Меню и его элементы создаются и редактируются в админ панели Django.
С помощью тега {% draw_menu 'menu_name' %} меню можно расположить на любой странице приложения.

## Техно-стек проекта.
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

### Как запустить проект:

1. Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/ddimani/tree_menu.git
```

```
cd tree_menu
```

2. Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
source env/bin/activate
```

3. Создать файл .env:

```
touch .env
```

4. Указать переменные окружения в файле .env по примеру файла .env.example:

```
SECRET_KEY='django-insecure-0-4h$#ck)3icf6re%myv+3jly88@m&vt%g$!6(n-je&r60-%yn'

DEBUG=False
```

5. Перейти в папку backend и установить зависимости из файла requirements.txt:

```
cd backend
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

6. Выполнить миграции:

```
python3 manage.py makemigrations

python3 manage.py migrate
```

7. Собрать статику:

```
python3 manage.py collectstatic
```

8. Создать Суперпользователя:

```
python3 manage.py createsuperuser
```

9. Запустить проект:

```
python3 manage.py runserver
```

10. Откройте приложение в браузере и зайдите в админку:

```
Перейдите по адресу `http://localhost:8000/admin/`
```

11. Добавьте несколько пунктов и подпунктов ваших меню 

12. Откройте ваше меню:

```
Перейдите по адресу `http://localhost:8000
```
