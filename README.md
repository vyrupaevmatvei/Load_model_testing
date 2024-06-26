# onlineModel with load

---
# 

Проект предназначен для эффективной продуктивизации онлайн модели с нагрузочным тестированием

### Структура проекта

---

    ├── README.md               <- Общее описание проекта.
    |
    ├── app.py                  <- Точка входа.
    |
    ├── Dockerfile              <- Файл для создания образа.
    |
    ├── requirements.txt   	    <- Файл с описанием окружения модели, в нем указываются необходимые для работы модели библиотеки.
    |
    ├── config.sh               <- Файл для отправки в DockerHub во время CI/CD процесса
    |
    ├── data                    <- Данные. Сырые выборки и датасеты, появляющиеся в процессе разработки
    |                        
    ├── models                  <- Обученные и сериализованные файлы моделей
    |             
    ├── notebooks               <- Jupyter Notebooks
    |
    ├── tests                   <- Данные и скрипты для тестирования
    |   |
    |   └── __init__.py 
    |
    ├── src                     <- Папка, в которой находятся необходимые конфигурационные файлы для нагрузки
        |
        ├── load.yaml                <- Конфигурация для нагрузки модели
        |
        ├── ammo.txt                 <- То какими запросами модель нагружается

---
