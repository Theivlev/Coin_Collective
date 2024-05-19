
# "Веб-сервис для групповых денежных сборов" (Coin_collective)

## 1. [Описание](#1)
## 2. [Установка Docker (на платформе Ubuntu)](#2)
## 3. [База данных и переменные окружения](#3)
## 4. [Команды для запуска](#4)
## 5. [Техническая информация](#5)
## 6. [Об авторе](#7)

## 1. Описание

Проект Coin_collective предоставляетследующие возможности:
  - Данные хранятся в реляционной БД, взаимодействие с ней
осуществляется посредством Django ORM.
  - API реализовано на базе Django REST Framework
  - Реализовано кэширование данных, возвращаемых GET-эндпоинтом, с
обеспечением достоверности ответов
  - Проект докеризирован и запускается через docker-compose up -d --build
  - Присутствует Management command для наполнения БД
моковыми данными (несколько тысяч).
  - При создании Группового сбора или Платежа реализована отправка письма на почту автора
  - Эндпоинты соответствуют REST и покрыты документацией Swagger.

## 2. Установка Docker (на платформе Ubuntu)
 
Для запуска необходимо установить Docker и Docker Compose.  
Подробнее об установке на других можно узнать на [официальном сайте](https://docs.docker.com/engine/install/).

## 3. База данных и переменные окружения

Проект использует базу данных PostgreSQL.  
Для подключения и выполненя запросов к базе данных необходимо создать и заполнить файл ".env" с переменными окружения

Шаблон для заполнения файла ".env":
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

## 4. Команды для запуска

# Запустить контейнер

docker-compose up -d --build

# Выполнить миграции:

docker-compose exec web python manage.py migrate

# Создать суперюзера

docker-compose exec web python manage.py createsuperuser 

# Получить токен:

Получить токен через POST запрос на http://localhost/api/token/login/

## Документация:
*Полная документация и примеры запросов доступны по эндпоинту*

http://localhost/swagger/

## 5. Техническая информация

Стек технологий: Python, Docker, PostgreSQL, nginx, Django Rest,   gunicorn, 

Веб-сервер: nginx (контейнер nginx)  
Backend фреймворк: Django (контейнер coin_collective-web )  
API фреймворк: Django REST (контейнер coin_collective-web )  
База данных: PostgreSQL (контейнер db)

## 7. Об авторе

Ивлев Алексей Константинович 
Python-разработчик (Backend)   
E-mail: theivlev@yandex.ru  