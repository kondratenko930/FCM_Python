import firebase_admin
import datetime
from firebase_admin import credentials
from firebase_admin import messaging

#1.инициализация SDK с указанием ключевого файла учетной записи сгенерированного в настройках консоли приложения
cred = credentials.Certificate("D:/1/python/FCM/drink-it-ec277-firebase-adminsdk-pnwbr-0ad6545fdf.json")
firebase_admin.initialize_app(cred)


#2.токен устройства
deviceToken = 'c8-GsZAqTyS6z0whf85cZU:APA91bE5aBln0zGr-5N1aVRUh0yGhzuCioGTAoqd6x2j2vSJmdumE5R74N6RQZHuSkSAV7_IZ6Dnmqzajr-4nUHaA6CGyge-_fxqQwZVqia5YWH-4mlfXQ8Nyh5yIbTudB6eNZ2qgl3o'

#firebase_admin.messaging.send()


#3.сообщение

message = messaging.Message(
        android=messaging.AndroidConfig(
            ttl=datetime.timedelta(seconds=3600),
            priority='normal',
            notification=messaging.AndroidNotification(
                title='10 $GOOG up 1.43% on the day_999999999999999999999999999999999999999',
                body='$GOOG gained 11.80 points to close at 835.67, up 1.43% on the day.99999999999999999999999999',
                icon='stock_ticker_update',
                color='#f45342'
            ),
        ),
        token=deviceToken,
    )


# message = messaging.Message(
#         priority='normal',
#         notification=messaging.Notification(
#             title='Заголовок',
#             body='Тело нашего тестового сообщения...',
#         ),
#         token=deviceToken,
# )




# message = messaging.Message(messaging.Notification(title="Portugal vs. Denmark",body="great match!"),
#     # data={
#     #     'score': '850',
#     #     'time': '2:45',
#     # },
#     token=deviceToken,
# )

#validate_only
#4. отправить сообщение

response = messaging.send(message)

#5.обработать ответ
print('Successfully sent message:', response)

#
print("fcm!")