
Создание ресурса
```bash
curl -X POST http://127.0.0.1:8000/tasks/ -H "Content-Type: application/json" -d '{"title": "Test Task"}
>>>{"id":1,"title":"Test Task","is_completed":false}
```


Получение ресурсов
```bash
curl -X GET http://127.0.0.1:8000/tasks/
>>>[{"id":1,"title":"Test Task","is_completed":false}]
```
