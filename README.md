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
1. Клонируйте репозиторий 
```bash
git clone git@github.com:1ce1ceice/TaskManager.git
cd TaskManager 
```

2. Создайте виртуальное окружение
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Установите зависимости
```bash
pip install -r requirements.txt
``` 

4. Настройка базы данных
```sql
CREATE DATABASE taskmanager;
postgresql://postgres@localhost:5433/taskmanager
```

5. Запуск сервера
```bash
python server.py
```
6. Запуск клиента (GUI)
В ДРУГОМ ТЕРМИНАЛЕ
```bash
source venv/bin/activate
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

---

## Видео демонстрация работы

https://github.com/user-attachments/assets/a4669dfe-cf90-4d75-8b91-25c060497542

---

## Видео демонстрация работы тестов

https://github.com/user-attachments/assets/37e60b86-39a0-40ad-b2a5-901457e9e51d



