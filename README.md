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
    - Generating QRcodes / Генерація QRcode-ів
    - Changing type of subscribes / Змінювати типи підписок
    - Choosing self customization / Вибір самостійного налаштування
    - Deleting QR-codes by user / Видаляти QR-коду користувачем
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
```
venv\Scripts\activate
```
On MacOS terminal:
```
python3 -m venv venv
```
```
source venv/bin/activate
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
### Fourth, start project / По-четверте, запустити проєкт:
#### You need enter 2 commands in console/terminal / Вам потрібно ввести 2 команди у консоль/термінал:
```
cd blog
```
```
python manage.py runserver
```
# Files and for what they needed, they main functions / Файли та навіщо вони потрібні, їх основні функції:
### Main folder / Основна тека:
#### `manage.py` needed for start project in console or terminal / `manage.py` потрібен для запуску проекту у консолі, або терміналі
#### `db.sqlite3` needed for work project / `db.sqlite3` потрібен для роботи проекту
____
### `user` folder / `user` тека:
#### `views.py` needed for create render page function / `views.py` потрібен створювання фукнції відображення сторінки
#### `urls.py` needed for create sub-links for log in and sign up / `urls.py` потрібен для під-посиланнь для авторизації та реєстрації
#### `models.py` needed for create model Profile who needed for main function / `models.py` потрібен створювання моделі Profile, яка потрібна для основних функцій проєкту
#### `templates` folder needed for keeping .html files / `templates` тека потрібена зберігання .html файлів
#### `static` folder needed for keeping .css files / `static` тека потрібена зберігання .css файлів
____
### `templates` folder needed for keeping base template for all .html files / `templates` тека потрібна для зберігання базового шаблону для всіх .html файлів
____
### `subscribes` folder / `subscribes` тека:
#### `views.py` needed for create render page function / `views.py` потрібен створювання фукнції відображення сторінки
#### `models.py` needed for create model Subscribe who needed for main function / `models.py` потрібен створювання моделі Subscribe, яка потрібна для основних функцій проєкту
#### `templates` folder needed for keeping .html files / `templates` тека потрібена зберігання .html файлів
#### `static` folder needed for keeping .css files / `static` тека потрібена зберігання .css файлів
____
### `static` folder needed for keeping base .css files and imgs who to be used in all .css & .html files / `static` тека потрібна для зберігання базових .css файлів та зображень, які будуть використовуватися у всіх .css та .html файлів 
____
### `payment` folder / `payment` тека:
#### `static` folder needed for keeping .css & .js files & imgs / `static` тека потрібна для зберігання .css та .js файлів та зображень
#### `templates` folder needed for keeping .html files / `templates` тека потрібена зберігання .html файлів
#### `views.py` needed for create render page function / `views.py` потрібен створювання фукнції відображення сторінки
____
### `my_qrs` folder / my_qrs тека:
#### `static` folder needed for keeping .css files & imgs / `static` тека потрібна для зберігання .css файлів та зображень
#### `templates` folder needed for keeping .html files / `templates` тека потрібена зберігання .html файлів
#### `views.py` needed for create render page function & redirect on site from our / `views.py` потрібен створювання фукнції відображення сторінки та перенаправлення на сайт QR-кода з нашого
____
### `media` folder needed for keeping all QR-codes created by users / `media` тека потрібна для зберігання QR-кодів створених користувачами
____
### `home_app` folder / `home_app` тека:
#### `static` folder needed for keeping .css files & imgs / `static` тека потрібна для зберігання .css файлів та зображень
#### `templates` folder needed for keeping .html files / `templates` тека потрібена зберігання .html файлів
#### `views.py` needed for create render page function / `views.py` потрібен створювання фукнції відображення сторінки
____
### `create_qrc` folder / `create_qrc` тека:
#### `static` folder needed for keeping .css & .js files & imgs / `static` тека потрібна для зберігання .css та .js файлів та зображень
#### `templates` folder needed for keeping .html files / `templates` тека потрібена зберігання .html файлів
#### `views.py` needed for create render page function / `views.py` потрібен створювання фукнції відображення сторінки
#### `models.py` needed for create model QRcodes who needed for main function / `models.py` потрібен створювання моделі QRcodes, яка потрібна для основних функцій проєкту
# Conclusion / Висновок:

This project was not easy, but it taught us how to do it:
1. Create web-applications on Django Framework
2. Work with django, qrcode
3. Work with `media` files
4. Use DB in self purposes

Цей проект був не простим, але завдяки йому ми навчились робити:
1. Робити веб-додатки на Django
2. Працювати з django, qrcode
3. Працювати з `media` файлами
4. Використовувати БД у своїх цілях

### Many thanks to Egor Galkin, David Petrenko and Timur Koshel for their work. But I especially want to say a big thank you to Egor for his great contribution to the project.
### Велика подяка Галкіну Єгору, Петренко Давиду і Кошелю Тимурові за роботу. Але особливо хочеться сказати велике спасибі Єгору за великий внесок у проект.

This project on [Figma](https://www.figma.com/design/MmrkuvX06fTykUtPIY5vig/Untitled?node-id=0-1&t=sjh89WEajAAA5qFc-1)