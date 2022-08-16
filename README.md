# [Бот-шутка](https://t.me/silly_naming_bot) для создания названий компаний

### О чём проект
Это прежде всего учебный проект, который помог мне разобраться с некоторыми инструментами, о них в самом конце.

### Что делает бот
Присылает насколько названий на выбор.

### Описание бота
Мы все иногда потешаемся над канцеляритом в переписках, казёными выражениям и ... названиями компаний в стиле РостАгро... 😊
Иногда создаётся впечатление, что львиная доля компаний названа при помощи генератора рандомных слов.  
За примерами можно заглянуть по [ссылке к боту](https://t.me/silly_naming_bot) или в [Спарк](https://spark-interfax.ru/) — посмотреть типичного контрагента для промышенного предприятия.  
Когда будете создавать свою компанию, назовите хорошо. Или воспользуйтесь ботом.  
Have fun!

### Что получилось

При работе над ботом освоил слудующее:
- создание виртуальной машины со статическим IP;
- подключение к ВМ по SSH;
- получения POST запросов и работа с ними на ВМ;
- получение self-signed SSL сертификата для настройки Telegram webhook;
- отработка работы с webhook;
- запаковка ключей и другой важной информации в отдельный файл, чтобы не "светить" её в коде.

Всё это на чистом API без использования библиотек, написанных третьими лицами.  

В итоге, теперь можно создавать ботов для решения прикладных задач: рассылка алертов, обновление данных, запуск скриптов и проч.
