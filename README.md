# WeatherSite
Проект на django по общению с API для показывания погоды на всю неделю.     
Проект реализует получение координат введенного пользователем города при помощи [geocode.maps.co](http://geocode.maps.co "geocode.maps.co") и потом посылает результат на [api.pirateweather.net](http://api.pirateweather.net "api.pirateweather.net"), получая прогноз погоды и показывая его пользователю.     
Доступен сайт на хосте pythonanywhere: https://alexeivarweather.pythonanywhere.com/    

## Функции
Возможность вводить город на русском/английском для получения данных на русском/английском.    
Язык переключается выбором перед отправкой.    
После нажатия get weather показывает текущую погоду и прогноз на неделю.    
Для текущей погоды показывает температуру, описание погоды и иконку погоды.    
Для прогноза показывает день, минимальную и максимальную температуру, описание погоды и иконку погоды.    

## Установка
Скачать и установить требования из requirements.txt.    
Предоставить .env файл с API ключом для pirateweather и geocode.maps в формате WEATHER_API_KEY для pirateweather и GEOCODE_API_KEY для geocode.maps.    
Проект написан на python 3.12.7. Сайт использует python 3.10.    
## Онлайн версия

Доступен сайт на хосте pythonanywhere: https://alexeivarweather.pythonanywhere.com/      
Для обоих API имеются свои лимиты, 1000 в день для geocode.maps и до 10000 в месяц для pirateweather.
