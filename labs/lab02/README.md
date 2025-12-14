<div align="center">
<h1><a id="intro">Лабораторная работа №2</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a>

***
## Задание

- [x] 1. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ who | wc -I # Команда who выводит список пользователей вошедших в систему, затем pipe (|) передает этот вывод на вход команды wc, которая с флагом l подсчитывает количество строк, то есть вошедших пользователей
$ id # Выводит информацию о текущем пользователе и его группах
$ whoami # Выводит имя текущего пользователя
$ hostnamectl # Выводит текущее имя хоста и информацию о системе.
```


- [x] 2. Выведите утилитой `tree` список вложенности дерева диреторий для каталога своего пользователя. Далее используйте `ls -a` и укажите отличие от `ls -l`.
```
tree -d # Флаг -d позволяет вывести только дерво директорий
ls -l # Выводит содержимое текущей директории, флаг -l позволяет вывести подробную информацию
ls -a # Выводит содержимое текущей директории, включая скрытые файлы с помощью флага -a
```


- [x] 3. Используйте утилиту `file` и `df` для определения какая файловая система на разделе `/dev/sda1`.
df -T /dev/sda1 # Позволяет вывести информацию о примонитрованной файловой системе, флаг -T добавляет к выводу тип ФС
file -s /dev/sda1 # Позволяет вывести информацию о типе файла, а флаг -s позволяет читать блочные устройства
- [x] 4. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ which vi # Расположение исполняемого файла редактора vi (Команда находит исполняемый файл, сканируя директории из $PATH)
$ locate hello.py # Выводит расположение файла по имени
$ sudo updatedb # Вручную обновляет базу данных locate
$ locate hello # Выводит расположение пути до файла или директории, содержащего строку hello
$ touch screen # Создание файла screen
$ find ~ -name screen # Поиск файла в домашней директории с именем screen
$ locate screen # Поиск пути до файла или директории, содержащего строку screen
$ sudo updated # Вручную обновляет базу данных locate, чтобы появился путь до screen
$ locate screen # Теперь команда находит screen
```


- [x]  5. Используйте конструкцию и вставьте ее в созданный файл ранее. Подключите `pygame` - используем исключительно для стилизации окна.

```py
import pygame
pygame.init()

# Устанавливаем размеры окна
screen_width = 800
screen_height = 600
window_size = (screen_width, screen_height)
pygame.display.set_mode(window_size) # Создаем окно

# Задаем цвет фона
bg_color = (255, 255, 255)
pygame.draw.rect(screen, bg_color, [0, 0, screen_width, screen_height], 1)

# Выводим текст на экран
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect()
text_rect.center = (400, 300)
screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
pygame.display.flip() # Обновляем экран
```


```

import pygame
import typer
import time
import sys

app = typer.Typer()

def colorful_render(screen, font, text, position):
    colors = [(255, 0, 0), (0, 255, 0), (255, 255, 0), (0, 0, 255), (255, 0, 255)]
    x, y = position

    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        char_surface = font.render(char, True, color)
        screen.blit(char_surface, (x, y))
        x += char_surface.get_width()
        pygame.display.flip()
        time.sleep(0.2)  # пауза для эффекта "печатающейся строки"

@app.command()
def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
):
    greeting = f"Добрый день, {name} {lastname}!" if formal else f"Привет, {name}!"

    # Инициализация Pygame
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Greeting App")
    screen.fill((0, 0, 0))  # черный фон

    font = pygame.font.SysFont(None, 75)
    text_rect = font.render(greeting, True, (255, 255, 255)).get_rect()
    text_rect.center = (screen_width // 2, screen_height // 2)

    colorful_render(screen, font, greeting, (text_rect.x, text_rect.y))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    app()

```
</p></details>
- [x] 6. Сделайте `commit` и `push` в свой репозиторий с изменениями в `master branch`. На следующих лабораторных работах мы вернемся к этому файлу.
- [x] 7. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ groups # Выводит список групп текущего пользователя
$ useradd smallman # Создает нового пользователя
$ userdel smallman -rf # Удаляет пользователя, -r удаляет также директории home и mail, -f позволяет сделать это принудительно без подтверждения
$ useradd smallman # Второе создание
$ passwd smallman # Установка пароля пользователя
$ usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33' # Команда usermod позволяет изменять учетную запись, а флаг -c записывает комментарий к этой УЗ
$ passwd smallman # снова смена пароля
$ id smallman # Информация о пользователе uid, gid, группы пользователя
$ groupadd -g 1500 readgroup # Создание группы с gid 1500 и названием readgroup
$ usermod -aG readgroup smallman # Команда добавляет пользователя smallman в группу readgroup без удаления из других групп
$ chmod 666 screen # Изменение прав на файл screen. Права 666 Чтение и запись всеми пользователями
```



- [x] 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному пользователю и выведите права этого польователя для измененного файла только используя `readgroup`.


- [x] 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ touch nmapres.txt # Создание файла 
$ setfacl -m u:smallman:rw nmapres.txt # Установление с помощью ACL прав на чтение и запись пользователю smallman файла nmapres.txt
$ setfacl -m g:readgroup:r nmapres.txt # Установление с помощью ACL прав на чтение группе readgroup файла nmapres.txt
$ getfacl nmapres.txt # Вывод прав на файл
```

- [x] 10. Сохраните файл внутри локального репозитория, так как следующая работа будет подразумевать запись в нее данных о nmap.
- [x] 11. Для закрепления выведите все списки групп пользователей на вашей ОС и права на верхнеуровневые каталоги.
```
cat /etc/group # Вывод содержимого файла в котором находится список всех групп
ls -l / # Права на верхнеуровневые каталоги можно вывести с помощью относительного пути ../ или абсолютного /
```

- [x] 12. Выведите все права для файлов и директорий локального репозитория которые имеют различные пользователи  (без использования длинных путей)
```
getfacl -R course_labs 
```

- [x] 13. Выведите процессы которые у вас запущены в терминале и вне его.
```
ps -a # список процессов привязанных к терминалу
ps aux # Список процессов флаг а - процессы всех пользователей, x - процессы не привязанные к tty, u - более подробный вывод 
```

- [x] 14. Оформить `README.md` по аналогии и использовать `shield`, etc.
- [x] 15. Составить `gist` отчет и отправить ссылку личным сообщением

***

## Links

- [Gist](https://gist.github.com)
- [GitHub CLI](https://cli.github.com)
- [cat](https://en.wikipedia.org/wiki/Cat_(Unix))
- [cd](https://en.wikipedia.org/wiki/Cd_(command))
- [cp](https://en.wikipedia.org/wiki/Cp_(Unix))
- [echo](https://en.wikipedia.org/wiki/Echo_(command))
- [env](https://en.wikipedia.org/wiki/Env_(shell))
- [file](https://en.wikipedia.org/wiki/File_(command))
- [ls](https://en.wikipedia.org/wiki/Ls)
- [mkdir](https://en.wikipedia.org/wiki/Mkdir)
- [mv](https://en.wikipedia.org/wiki/Mv)
- [ps](https://en.wikipedia.org/wiki/Ps_(Unix))
- [pwd](https://en.wikipedia.org/wiki/Pwd)
- [rm](https://en.wikipedia.org/wiki/Rm_(Unix))
- [touch](https://en.wikipedia.org/wiki/Touch_(Unix))
- [apt](http://help.ubuntu.ru/wiki/apt)
- [brew](https://brew.sh)
- [npm](https://docs.npmjs.com)
