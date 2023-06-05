# postgres-flask
Использовались postgres, sqlalchemy, flask, docker-compose.

#### Установка
Для установки сервиса на Windows 10 убедитесь, что у вас установлен и запущен Docker Desktop (устанавливается только на Windows 10 Enterprise, Pro, or Education издания), скачайте docker-compose.yml файл и перенесите его в отдельную папку. В терминале перейдите в папку, содержащую docker-compose.yml файл и введите команду docker compose up. Docker сам скачает все необходимые образы с Docker Hub'а и запустит сервис.
Инструкции по сборке содержатся в файлах docker-compose.yml и Dockerfile. URI для подключения к postgres БД находится в файле config.py.

#### Примеры запросов:
  1. POST запрос с содержимым вида {"questions_num": integer}.
```
curl -X POST -H "Content-Type: application/json" -d "{\"questions_num\": \"1\"}" http://localhost:80
```
```
null
```
```
curl -X POST -H "Content-Type: application/json" -d "{\"questions_num\": \"1\"}" http://localhost:80
```
```
"Her four terms representing Minnesota in Congress included a presidential run"
```
