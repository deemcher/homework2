"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        print('Длинна строки: ' + str(len(text)))
        print('Количество слов: ' + str(len(text.split())))
        with open('referat2.txt', 'w', encoding='utf-8') as new_file:
            text = text.replace('.', '!')
            new_file.write(text)

if __name__ == "__main__":
    main()
