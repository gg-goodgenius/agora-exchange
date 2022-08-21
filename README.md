[![deploy](https://github.com/gg-goodgenius/agora-exchange/actions/workflows/deploy.yml/badge.svg)](https://github.com/gg-goodgenius/agora-exchange/actions/workflows/deploy.yml)
# AGORA Exchange Service

## Установка 
```
git clone https://github.com/gg-goodgenius/agora-exchange
cd agora-exchange
docker-compose up 
```
## Доступ
localhost:8000 - маркетплейс
localhost:8001 - микросервис
localhost:5555 - flower

## endpoints
- [POST] localhost:8001/login/ - авторизация для получения токена
- [GET] localhost:8001/exchange/ - получить обновления для маркетплейса
- [POST] localhost:8001/exchange/ - отправить обновления для маркетплейса (in_body: type - тип данных (поумолчанию 'xml'), file - файл с данными)

## Дополнительно
Для устновки паролей на django admin используются скрипты:
initadmin_exchange - для микросервиса
initadmin_marketplace - для маркетплейса

### Наша команда 
- Руслан Хайруллин - разработчик ([@ruha02](https://t.me/ruha02))
- Тимофей - разработчик ([@Timofey1566](https://t.me/Timofey1566))
- Оля Баскакова - дизайнер презентции ([@OlyaBaskakowa](https://t.me/OlyaBaskakowa))
