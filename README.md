# Project "QRCode Aqua"
## Navigation / Навігація:
> [!TIP]
> - [Main information](#main-information-of-project--основна-інформація-про-проект)
> - [Command structure](#command-structure--склад-команди)
> - [Figma & FigJam](#figma--figjam)
> - [Project structure](#project-structure--структура-проєкту)
> - [Applications and for what they needed](#applications-and-for-what-they-needed-they-main-functions--додатки-та-навіщо-вони-потрібні-їх-основні-функції)
> - [How run this project on your own PC](#how-correctly-run-the-project-on-your-own-pc--як-правильно-запустити-проект-на-вашому-власному-компютері)
> - [Conclusion / Висновок](#how-correctly-run-the-project-on-your-own-pc--як-правильно-запустити-проект-на-вашому-власному-компютері)
## Main Information of project / Основна Інформація про проект:
### QRCode Aqua project can do / QRCode Aqua project може робити:
- Generate and save customizated QR-codes / Генерує а також зберігає кастомізовані QR-коди 
- Can changing type of subcribes with payment methods / Може змінюваати типи підписок с оплачуваними методами
- Saves every qr-code who was created by user / Зберігає кожжний QR-код який був створений користувачем
- Control and limit the action of the QR-code / Контролює й обмежує дії с QR-кодом
____
### Why this project is useful / Чому цей проект корисний:
- Цей проєкт буде корисний якщо вам потрібно згенерувати просто та швидко кастомний QR-код за вашим URL-посиланням або інформацією
- This project will be useful if you need to generate a custom QR code based on your URL link or information simply and quickly
## Command structure / склад команди:
- Illya Shramko / Ілля Шрамко (Team Lead) [github.com/IllyaShramko](https://github.com/IllyaShramko/QRcode-Aqua)
- Timur Koshel' / Тимур Кошель [github.com/kosheltimur](https://github.com/kosheltimur/QRcode)
- Egor Galkin / Єгор Галкін [github.com/EgorGalkinORG](https://github.com/EgorGalkinORG/QRcode-Aqua)
- David Petrenko / Давид Петренко [github.com/Davidptn](https://github.com/Davidptn/Qr_Aqua)
____
> [!NOTE]
> ## [Figma](https://www.figma.com/design/MmrkuvX06fTykUtPIY5vig/Untitled?node-id=0-1&t=zx68S8o0qcLjLxW1-1) & [FigJam](https://www.figma.com/board/IK5GgL0IesWTOP4s8QbsvZ/FigJam-QRAqua?node-id=0-1&t=K6yqz4vuzxA6GEBs-1)
 
____
# Project structure / Структура проєкту:
![Structure_project](/blog/static/images/structure_project.jpg)
____
## Applications and for what they needed, they main functions / Додатки та навіщо вони потрібні, їх основні функції:
> [!NOTE]
> ### On English language:
> - Application `user` created for use functions __login__, __registration__ and __logout__. Also there created model __Profile__.
> - Application `subscribes` created for control and switch type of subscribe user, e.g. how much user can generate QRcodes, when the term of > work ends of QRcode. Also there created model __Subscribe__.
> - Application `payment` created for switch subscribe who was selected by user on page `subscribes`.
> - Application `my_qrs` created for keep user's QRcodes and delete they if it want user. Also `my_qrs` needed for redirect users on their > web-sites and it is implemented in this way:
>     ```python
>     # Create a function for redirect the user if all conditions are met.
>     def redirect_qrcode(request: HttpRequest, pk):
>     # Get QRcode by him id
>     QRcode = QRcodes.objects.get(pk=pk)
>     # Get info about him url
>     url = QRcode.url
>     # Get info about him term work
>     date_delete = QRcode.date_delete
>     # Create condition: if user's type sub "base"
>     if QRcode.user.subscribe == "base":
>         # Create condition: if term work of QRcode end (6 months), show error.
>         if date_delete < timezone.now():
>             # Show error: QRcode has end his term work (6 months).
>             return render(request, 'my_qrs/error_qrcode.html', context={
>                 "error_qrcode": 'time'
>             })
>     # Create second condition: if QRcode's owner has type sub < type sub now. 
>     elif QRcode.user.subscribe.id < QRcode.subscribe_created.id:
>         # Show error.
>         return render(request, 'my_qrs/error_qrcode.html', context={
>             "error_qrcode": 'sub', "is_auth": True, "username": request.user,
>             'sub': {
>                 "current": Profile.objects.get(user= request.user).subscribe,
>                 "created": QRcode.subscribe_created
>             }
>         })
>     # Redirect user on his web-site by url who we get before.
>     return redirect(url)
>     ```
> - Application `home_app` it's main page for navigation on all other pages (`/create_qrc`,`/my_qrc`,`/subscribes`,`/logout`)
> - Application `create_qrc` created for generate customizated QRcodes by user url and save they on `my_qrc` page.
> ### На Українській мові:
> - Додаток `user` створений для використання функцій __login__, __registration__ і __logout__. Також тут створенна модель __Profile__.
> - Додаток `subscribes`, створений для керування та перемикання типу підписок користувача, наприклад скільки користувач може згенерувати > QR-кодів, коли закінчується термін роботи QR-коду. Також тут створенна модель __Subscribe__.
> - Додаток `payment`, створений для перемикання підписок, який вибрав обрав на сторінці `subscribes`.
> - Додаток `my_qrs`, створений для збереження QR-кодів користувача та видалення їх, якщо це потрібно користувачу. Також потрібен для > перенаправлення користувача на його сайт, який він вказав при створенні QR-кода, це реалізовано ось таким способом:
>     ```python
>     # Створюємо функцію для перенаправлення користувача якщо всі умови задоволняють це зробити
>     def redirect_qrcode(request: HttpRequest, pk):
>     # Отримуємо QRcode за його id
>     QRcode = QRcodes.objects.get(pk=pk)
>     # Отримуємо інформацію про його посилання
>     url = QRcode.url
>     # Отримуємо інформацію про його термін роботи
>     date_delete = QRcode.date_delete
>     # Створюємо умову: Якщо тип підписки користувача "base"
>     if QRcode.user.subscribe == "base":
>         # Створюємо умову: Якщо термін роботи QRкода вичерпано (6 місяців), то виводило помилку.
>         if date_delete < timezone.now():
>             # Виводимо помилку в якій говорится про те що термін праці QRкода вичерпано (6 місяців)
>             return render(request, 'my_qrs/error_qrcode.html', context={
>                 "error_qrcode": 'time'
>             })
>     # Створюємо другу умову: Якщо у власника QRкода тип підписки менше ніж його зараз.
>     elif QRcode.user.subscribe.id < QRcode.subscribe_created.id:
>         # Виводиму помилку відповідну помилку.
>         return render(request, 'my_qrs/error_qrcode.html', context={
>             "error_qrcode": 'sub', "is_auth": True, "username": request.user,
>             'sub': {
>                 "current": Profile.objects.get(user= request.user).subscribe,
>                 "created": QRcode.subscribe_created
>             }
>         })
>     # Перенаправляємо користувача на його сайт, якщо всі умови задовільні.
>     return redirect(url)
>     ```
> - Додаток `home_app` це головна сторінка для навігації на всі інші сторінках (`/create_qrc`,`/my_qrc`,`/subscribes`,`/logout`)
> - Додаток `create_qrc`, створений для створення кастомізованих QR-кодів за посиланням користувача та збереження їх на сторінці `my_qrc`.
____
# How correctly run the project on your own PC / Як правильно запустити проект на вашому власному комп'ютері:
### For first, you need to clone this repository with command / Для початку вам потрібно скопіювати проект с командою:
```
git clone https://github.com/IllyaShramko/QRcode-Aqua.git
```
### Second, you need to create venv and install all requirements who typed bottom for correctly work project / По-друг, вам потрібно створити venv і встановити всі біблеотеки з файлу requirements, які перечислені внизу для коректної роботи проекту:
#### You can create and activate venv for 3 commands / Ви можете створити та активувати віртуальне оточення з допомоги 3 команд:
```
cd QRcode-aqua
```
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
____
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