# REST API для сайта ФСТР pereval.online

## Федерация спортивного туризма России ведет базу данных горных перевалов, на которые поступают туристические взносы. Модератор Федерации проверит информацию и сохранит ее в базе данных.

## Это API-решение для мобильного приложения для Andriod и IOS, которое упростит задачу туристам по отправке данных о пропуске при наличии подключения к Интернету.

Требования:

Когда турист достигает горного перевала, он может сделать фотографию и использовать мобильное приложение для отправки информации. Когда этот турист нажимает кнопку «Отправить», мобильное приложение вызывает метод submitData, который принимает данные в формате JSON.
```
{
  "user": {
    "email": "user@example.com",
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "surname": "Ivanovich",
    "phone": "+79277777777"
  },
  "coords": {
    "latitude": 100,
    "longitude": 90,
    "height": 2147483647
  },
  "level": {
    "winter": "string",
    "summer": "string",
    "autumn": "string",
    "spring": "string"
  },
  "images": [
    {
      "data": "string",
      "title": "string"
    }
  ],
  "status": "new",
  "beauty_title": "string",
  "title": "string",
  "other_titles": "string",
  "connect": "string"
}
```
После отправки объекту присваивается статус «новый». Эксперты FSTR меняют его статус на «ожидает», что означает, что эксперт работает над ним, проверяет новый объект, а затем меняет статус на «принято» или «отклонено».

Методы API
GET /api/pereval/
Возвращает список всех горных перевалов.

POST /api/pereval/
Позволяет подать заявку на один горный перевал.

GET /api/pereval/{id}/ 
Получает данные для определенного горного перевала.

PATCH /api/pereval/{id}/

Позволяет изменить значения атрибутов перевала. Возвращает ответ JSON с
+ состояние: 1 для успешного обновления и 0 для неудачного обновления.
+ сообщение: объясняет, почему обновление не удалось

GET /api/pereval/?user__email={email}

Возвращает список всех объектов, которые были отправлены в систему пользователем с указанным адресом электронной почты.