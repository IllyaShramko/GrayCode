# Project "QRCode Auqa"
### command structure / склад команди:
- Illya Shramko / Ілля Шрамко [github.com/IllyaShramko](https://github.com/IllyaShramko)
- Timur Koshel' / Тимур Кошель [github.com/kosheltimur](https://github.com/kosheltimur)
- Egor Galkin / Єгор Галкін [github.com/EgorGalkinORG](https://github.com/EgorGalkinORG)
- David Petrenko / Давид Петренко [github.com/Davidptn](https://github.com/Davidptn)
____
## Main Information of project / Основна Інформація про проект:
### QRCode Auqa project can do / QRCode Auqa project може робити:
- Start up / Запускатися
- Generate and save customizated QR-codes / Генерує а також зберігає кастомізовані QR-коди 
- Can changing type of subcribes with payment methods / Може змінюваати типи підписок с оплачуваними методами
- Saves every qr-code who was created by user / Зберігає кожжний QR-код який був створений користувачем
- Control and limit the action of the QR-code / Контролює й обмежує дії с QR-кодом
____

### Why this project is useful / Чому цей проект корисний:
- The project has many functions such as / У проекта є багато функцій такі як:
    - Registration / Реєстрація
    - Authorizations / Авторизація
    - Generating QRcodes / Генерація QRcode
    - Changing type of subscribes / Змінювати типи підписок
    - Choosing self customization / Вибір самостійного налаштування
    - Deleting QR-codes by user / Видаляти QRcode-и користувачем
    - Redirect user from our site to his website what he indicated when he generate QR-code / Перенаправлення користувача з нашого сайту на його веб-сайт який він вказав коли генерував QR-код

# How correctly run the project on your own PC / Як правильно запустити проект на вашому власному комп'ютері:
### For first, you need to clone this repository with command / Для початку вам потрібно скопіювати проект с командою:
```
git clone https://github.com/IllyaShramko/QRcode-Aqua.git
```
### Second, you need to create venv and install all requirements who typed bottom for correctly work project / По-друг, вам потрібно створити venv і встановити всі біблеотеки з файлу requirements, які перечислені внизу для коректної роботи проекту:
#### You can create venv for 1 command / Ви можете створити віртуальне оточення з допомоги 1 команди:
On Windows console:
```
python -m venv venv
```
On MacOS terminal:
```
python3 -m venv venv
```
### Third, libraries which you need to install for run the project / По-третє, модулі, які вам знадобиться установити для роботи проекту:
#### 1. django, it's main module for work all project, without he project won't be started! / django це головний модуль для роботи всього проекту, без нього проект не запуститься!
#### 2. os need for manupilate files, save qrcodes etc. / OS потрібен для маніпулювання файлами та збереження qr-кодів, тощо.
#### 3. qrcode, it's main module for generate qrcodes, without he project can started, but doesn't generate qrcodes / qrcode, це основний модуль для створення qr-кодів, без нього можна запустити проект, але не буде генерувати qr-коди
#### 4. pillow, it's needed for work module qrcode / pillow, потрібен для роботи модуля qrcode
#### 5. time, it's needed for control and limit the action on QR-codes / time, потрібен для контролю та обмеження дій над QR-кодами
### You can install all of this module for 1 command / Ви можете встановити усі ці модулі з допомоги 1 команди:
```
pip install -r requirements.txt
```