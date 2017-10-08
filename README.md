# Password Strength Calculator

Сложность пароля будет оцениваться по десятибальной шкале из нескольких показателей.
Предпологается, что пароль не будет содержать whitespace символов(пробелов)
Кроме букв и цифр в пароле разрешены только следующие символы: '@', '#', '$', '!', '.', '%', '?', '/', '<', '>', '\'. 

  * Использование символов из обоих регистров(верхнего и нижнего) + 2 балла
  * Использование цифр + 2 балла
  * Использование специальных символов, таких как: @, #, $ и др + 2 балла
  * Пароль должен иметь минимально допустимую длину  
    * Если length <= 6 символов, оценка снижается до 1 балла. 
    * Если 6 < length <= 8, то к оценке прибавляется 1 балл
    * Если 8 < length <= 10, то к оценке прибавляется 2 балла
    * Если 10 < length <= 12, то к оценке прибавляется 3 балла 
    * Если length > 12, то к оценке прибавляется 4 балла
  * Запрет на использование слов из passwor blacklist, оценка снижается до 1 балла
  * Пароль не должен быть похож на дату или телефонный номер, оценка снижается до 1 балла

# Запуск

Для запуска вы должны поместить файл popular_password.txt и password_strength.py в одну папку.
Ниже приведен пример работы скрипта:
```python
python3 password_strength.py
Password: 
Your rating:  10
```


# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

