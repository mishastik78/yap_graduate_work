# Дипломный проект 20 когорты 

https://github.com/baramba/yap_graduate_work

## Тема
### Сервис лояльности онлайн кинотеатра

## Участники
* Антон Ревуцкий, backend
* Юрий Сухобок, backend
* Михаил Индуров, backend
* Бабихин Максим, frontend
  
  
## Запуск
1. Переименовать .env_example в .env
2. Запустить контейнеры
```
docker compose up -d
```
3. Выполнить миграции в контейнере, где IMAGE=yap_graduate-adminpanel
```
docker exec -it container_id python manage.py migrate
```
4. Демонстрационная страницы будет доступна по адресу http://localhost
5. Административная панель будет доступна по адресу http://localhost/admin


## Описание проекта

Сервис позволяет создавать промокоды различных типов для привлечения новых клиентов, удержания старых и повышения продаж.


![image](./docs/c4.png)
![image](./docs/seq1.png)
![image](./docs/seq2.png)

