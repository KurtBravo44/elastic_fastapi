# Search Service

## Установка

1. Склонируйте репозиторий.
2. Перейдите в директорию проекта.
3. Соберите Docker-контейнер:
   bash
   docker build -t search_service .
4. Запустите контейнер:
   bash
   docker run -d -p 8000:8000 search_service

## Использование

- Поиск документов: GET /search?query=ваш_поиск
- Удаление документа: DELETE /documents/{id}

