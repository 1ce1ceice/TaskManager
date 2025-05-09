# Клиент-серверное приложение "Task Manager"

Простое приложение для управления задачами с сервером на Flask и клиентом на Tkinter.

---

## Архитектура

- Клиент: Десктоп-приложение на Tkinter
- Сервер: Flask + SQLAlchemy
- База данных: PostgreSQL

---

## Структура

- `model.py` `server.py` - Бизнес-логика и работа с базой данных и API
- `view.py` - Пользовательский интерфейс (Tkinter GUI)
- `controller.py` - Управление событиями
- `tests/` - Юнит-тесты

---

## Установка
```bash
pip install -r requirements.txt
``` 
---

## Запуск

Сервер
```bash
python server.py
```

Клиент
```bash
python client/main.py
```
---

## Тестирование
```bash
pytest
```
---

## Автор
Заикин Тимофей 

