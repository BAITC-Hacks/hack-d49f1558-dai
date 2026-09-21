# Фильтр алертов

Тестовое задание Hackalem. Скрипт читает events.json, оставляет из потока событий только критичные и печатает сводку одной фразой.

## Как запустить

Нужен Python 3.10 и новее, зависимостей нет, только стандартная библиотека.

```
python3 filter_alerts.py
```

Путь к файлу можно передать аргументом, по умолчанию берётся events.json из текущей папки:

```
python3 filter_alerts.py events.json
```

## Что получилось

Из 8 событий критичны 3: disk 90%, payment failed и db timeout. Четыре события info и одно событие warn не попадают в вывод. Фильтр проверяет поле severity на значение critical.

Вывод скрипта:

```
critical: disk 90%
critical: payment failed
critical: db timeout
критичных 3
```

## Файлы

- events.json: 8 входных событий (info, warn, critical)
- filter_alerts.py: загрузка JSON, фильтр, печать
