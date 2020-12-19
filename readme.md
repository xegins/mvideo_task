# Запуск сервера
1. Перед запуском сервера в файле **config.cfg** указываются параметры *host*, *port* и 
путь к файлу с данными по рекомендациям *recommends_path*, если они не заданы, 
то будут использованы значения по умолчанию:    
host=localhost,    
port=80,    
recommends_path=recommends.csv.
2. При запуске программы данные из файла записываются в словарь, ключами которого
являются sku, а значениями являются списки с рекоммендованными товарами.     
(данный словарь занимает **~10Гб** оперативной памяти)
3. Для получения рекомендованных товаров отправляется запрос вида: **host:port/sku**    
например: http://localhost:80/Air5Z6EmFO    
запрос с указанием "близости" рекомендованного товара: http://localhost:80/Air5Z6EmFO?limit=0.7
# Масштабирование сервиса
1. Для масштабирования системы можно использовать шардирование, распределяя 
товары со всеми рекоммендуемыми для него между серверами.    
2. Добавление одной записи в файл с рекомендациями будет обходится примерно в 150 
байт, при добавлении ее в словарь с рекомндациями. 