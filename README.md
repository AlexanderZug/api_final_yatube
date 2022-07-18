# Учебный проект по DRF, написанный в рамках Яндекс.Практикума 

API дает возможность - в зависимости от прав доступа - добавлять новых пользователей, создавать, редактировать, удалять посты, писать к ним комментарии и подписываться на авторов.


![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

## Запуск проекта

> Установите Python (если он не установлен), предпочтительно начиная с версии 3.8 <br>
> [Download Python3](https://www.python.org/downloads/release/python-3910/)

Клонируйте репозиторий:
```
git clone https://github.com/AlexanderZug/api_final_yatube.git
```
Перейдите в папку с проектом:
```
cd api_final_yatube
```
Создайте и активируйте вирутальное окружение:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Установите зависимости:
```
pip3 install -r requirements.txt
```
Выполните миграции:
```
python3 manage.py migrate
```
Запуситете проект:
```
python3 manage.py runserver
```

## Документацию по API с эндпоинтами и правами доступа Вы сможете найти перейдя по адресу:
```
http://127.0.0.1:8000/redoc/
```

> документация будет доступна после запуска проекта
