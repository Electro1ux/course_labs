<div align="center">
<h1><a id="intro">Лабораторная работа №2</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a></div>

***
## Задание

- [x] 1. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ who | wc -I # Команда who выводит список пользователей вошедших в систему, затем pipe (|) передает этот вывод на вход команды wc, которая с флагом l подсчитывает количество строк, то есть вошедших пользователей
$ id # Выводит информацию о текущем пользователе и его группах
$ whoami # Выводит имя текущего пользователя
$ hostnamectl # Выводит текущее имя хоста и информацию о системе.
```
```
┌──(kali㉿kali)-[~]
└─$ who | wc -l
1
                                                                                                        
┌──(kali㉿kali)-[~]
└─$ id
uid=1000(kali) gid=1000(kali) groups=1000(kali),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),100(users),101(netdev),103(scanner),107(bluetooth),125(lpadmin),133(wireshark),135(kaboxer),137(docker)
                                                                                                        
┌──(kali㉿kali)-[~]
└─$ whoami     
kali
                                                                                                                        
┌──(kali㉿kali)-[~]
└─$ hostnamectl
 Static hostname: kali
       Icon name: computer-vm
         Chassis: vm 🖴
      Machine ID: aa8b2369c8374f788c337132b3a3fa02
         Boot ID: 8223242a88ca458c822a43b6dcea10fc
    AF_VSOCK CID: 503436368
  Virtualization: vmware
Operating System: Kali GNU/Linux Rolling          
          Kernel: Linux 6.12.25-amd64
    Architecture: x86-64
 Hardware Vendor: VMware, Inc.
  Hardware Model: VMware Virtual Platform
Firmware Version: 6.00
   Firmware Date: Thu 2020-11-12
    Firmware Age: 5y 1month 2d
```
- [x] 2. Выведите утилитой `tree` список вложенности дерева диреторий для каталога своего пользователя. Далее используйте `ls -a` и укажите отличие от `ls -l`.
```
tree -d # Флаг -d позволяет вывести только дерво директорий
ls -l # Выводит содержимое текущей директории, флаг -l позволяет вывести подробную информацию
ls -a # Выводит содержимое текущей директории, включая скрытые файлы с помощью флага -a
```
```
┌──(kali㉿kali)-[~/course_labs]
└─$ tree -d
.
├── artifacts
│   ├── art_cheatsheet
│   ├── cheatsheet
│   ├── exmpls
│   ├── owasp
│   └── ppt
├── assets
│   ├── logotype
│   └── style
└── labs
    ├── lab01
    ├── lab02
    ├── lab03
    ├── lab04
    ├── lab05
    │   ├── client
    │   ├── server
    │   └── source
    └── lab06

20 directories
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
```
┌──(root㉿kali)-[/home/kali/course_labs]
└─# locate screen | wc -l 
1385
                                                                                                                        
┌──(root㉿kali)-[/home/kali/course_labs]
└─# updatedb             
                                                                                                                        
┌──(root㉿kali)-[/home/kali/course_labs]
└─# locate screen | wc -l
1386
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
![Logo](screens/app.jpg)
<details><summary><strong>Код программы</strong></summary><p>

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
```
┌──(root㉿kali)-[/home/kali/course_labs]
└─# useradd smallman                                                     
                                                                                                                        
┌──(root㉿kali)-[/home/kali/course_labs]
└─# passwd smallman
New password: 
Retype new password: 
passwd: password updated successfully
                                                                                                                        
┌──(root㉿kali)-[/home/kali/course_labs]
└─# usermod smallman -c 'Hach Hachov Hacherovich,239,45-67,499-239-45-33'
                                                                                                         
┌──(root㉿kali)-[/home/kali/course_labs]
└─# grep smallman /etc/passwd
smallman:x:1002:1002:Hach Hachov Hacherovich,239,45-67,499-239-45-33:/home/smallman:/bin/sh
                                                                                                                        
┌──(root㉿kali)-[/home/kali/course_labs]
└─# id smallman
uid=1002(smallman) gid=1002(smallman) groups=1002(smallman),1500(readgroup)
                                                                                                                        
┌──(root㉿kali)-[/home/kali/course_labs]
└─# grep readgroup /etc/group
readgroup:x:1500:smallman

┌──(root㉿kali)-[~]
└─# ls -l
total 0
-rw-r--r--  1 root root    0 Nov 28 05:31 screen
                                                                                                                        
┌──(root㉿kali)-[~]
└─# chmod 666 screen
                                                                                                                        
┌──(root㉿kali)-[~]
└─# ls -l
total 0
-rw-rw-rw-  1 root root    0 Nov 28 05:31 screen
```

- [x] 8. Выведите группу прав для `screen` и измените, что бы файл был доступен только для чтения созданному пользователю и выведите права этого польователя для измененного файла только используя `readgroup`.
```
┌──(root㉿kali)-[~]
└─# ls -l screen
-rw-rw-rw- 1 root root 0 Nov 28 05:31 screen
                                                                                                                        
┌──(root㉿kali)-[~]
└─# chown smallman:readgroup screen
                                                                                                                        
┌──(root㉿kali)-[~]
└─# chmod 400 screen               
                                                                                                                        
┌──(root㉿kali)-[~]
└─# ls -l screen
-r-------- 1 smallman readgroup 0 Nov 28 05:31 screen
                                                                                                                        
┌──(root㉿kali)-[~]
└─# getfacl screen           
# file: screen
# owner: smallman
# group: readgroup
user::r--
group::---
other::---
```
- [x] 9. Используйте `POSIX ACL`. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ touch nmapres.txt # Создание файла 
$ setfacl -m u:smallman:rw nmapres.txt # Установление с помощью ACL прав на чтение и запись пользователю smallman файла nmapres.txt
$ setfacl -m g:readgroup:r nmapres.txt # Установление с помощью ACL прав на чтение группе readgroup файла nmapres.txt
$ getfacl nmapres.txt # Вывод прав на файл
```
```
┌──(root㉿kali)-[~]
└─# getfacl nmapres.txt 
# file: nmapres.txt
# owner: root
# group: root
user::rw-
user:smallman:rw-
group::r--
group:readgroup:r--
mask::rw-
other::r--
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
<details><summary><strong>Вывод всех прав</strong></summary><p>

```

getfacl -R course_labs
# file: course_labs
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/description
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/info
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/info/exclude
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/logs
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/logs/HEAD
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/logs/refs
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/logs/refs/heads
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/logs/refs/heads/master
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/logs/refs/remotes
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/logs/refs/remotes/origin
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/logs/refs/remotes/origin/HEAD
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/index
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/packed-refs
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/HEAD
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/refs
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/refs/tags
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/refs/heads
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/refs/heads/master
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/refs/remotes
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/refs/remotes/origin
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/refs/remotes/origin/HEAD
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/objects
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/objects/info
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/objects/pack
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/.git/objects/pack/pack-ef08859f66140af9a23911558894b7ca11da7322.pack
# owner: root
# group: root
user::r--
group::r--
other::r--

# file: course_labs/.git/objects/pack/pack-ef08859f66140af9a23911558894b7ca11da7322.rev
# owner: root
# group: root
user::r--
group::r--
other::r--

# file: course_labs/.git/objects/pack/pack-ef08859f66140af9a23911558894b7ca11da7322.idx
# owner: root
# group: root
user::r--
group::r--
other::r--

# file: course_labs/.git/config
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/.git/hooks
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/labs
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/labs/lab04
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/labs/lab04/README.md
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab06
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/labs/lab06/README.md
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/labs/lab05/source
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/labs/lab05/source/Dockerfile
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/source/hello.py
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/source/requirements.txt
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/README.md
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/docker-compose.yml
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/client
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/labs/lab05/client/Dockerfile
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/client/client.py
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/client/requirements.txt
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/server
# owner: root
# group: root
user::rwx
group::r-x
other::r-x

# file: course_labs/labs/lab05/server/app.py
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/labs/lab05/server/Dockerfile
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/assets/logotype/logo.jpg
# owner: root
# group: root
user::rw-
group::r--
other::r--

# file: course_labs/CONTRIBUTING.md
# owner: root
# group: root
user::rw-
group::r--
other::r--

```
</p></details>
- [x] 13. Выведите процессы которые у вас запущены в терминале и вне его.
```
ps -a # список процессов привязанных к терминалу
ps aux # Список процессов флаг а - процессы всех пользователей, x - процессы не привязанные к tty, u - более подробный вывод 
```

<details><summary><strong>Вывод всех прав</strong></summary><p>

```

┌──(kali㉿kali)-[~/course_labs]
└─$ ps -a
    PID TTY          TIME CMD
  15255 pts/0    00:00:00 ps
                                                                                                                        
┌──(kali㉿kali)-[~/course_labs]
└─$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.1  23668 13976 ?        Ss   04:27   0:01 /sbin/init splash
root           2  0.0  0.0      0     0 ?        S    04:27   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    04:27   0:00 [pool_workqueue_release]
root           4  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-kvfree_rcu_reclaim]
root           5  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-rcu_gp]
root           6  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-sync_wq]
root           7  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-slub_flushwq]
root           8  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-netns]
root          10  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/0:0H-events_highpri]
root          11  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/0:1-mm_percpu_wq]
root          12  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/u128:0-ipv6_addrconf]
root          13  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-mm_percpu_wq]
root          14  0.0  0.0      0     0 ?        I    04:27   0:00 [rcu_tasks_kthread]
root          15  0.0  0.0      0     0 ?        I    04:27   0:00 [rcu_tasks_rude_kthread]
root          16  0.0  0.0      0     0 ?        I    04:27   0:00 [rcu_tasks_trace_kthread]
root          17  0.0  0.0      0     0 ?        S    04:27   0:00 [ksoftirqd/0]
root          18  0.0  0.0      0     0 ?        I    04:27   0:00 [rcu_preempt]
root          19  0.0  0.0      0     0 ?        S    04:27   0:00 [rcu_exp_par_gp_kthread_worker/1]
root          20  0.0  0.0      0     0 ?        S    04:27   0:00 [rcu_exp_gp_kthread_worker]
root          21  0.0  0.0      0     0 ?        S    04:27   0:00 [migration/0]
root          22  0.0  0.0      0     0 ?        S    04:27   0:00 [idle_inject/0]
root          23  0.0  0.0      0     0 ?        S    04:27   0:00 [cpuhp/0]
root          24  0.0  0.0      0     0 ?        S    04:27   0:00 [cpuhp/1]
root          25  0.0  0.0      0     0 ?        S    04:27   0:00 [idle_inject/1]
root          26  0.0  0.0      0     0 ?        S    04:27   0:00 [migration/1]
root          27  0.0  0.0      0     0 ?        S    04:27   0:00 [ksoftirqd/1]
root          28  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/1:0-events]
root          29  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/1:0H-events_highpri]
root          30  0.0  0.0      0     0 ?        S    04:27   0:00 [cpuhp/2]
root          31  0.0  0.0      0     0 ?        S    04:27   0:00 [idle_inject/2]
root          32  0.0  0.0      0     0 ?        S    04:27   0:00 [migration/2]
root          33  0.0  0.0      0     0 ?        S    04:27   0:00 [ksoftirqd/2]
root          35  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/2:0H-events_highpri]
root          36  0.0  0.0      0     0 ?        S    04:27   0:00 [cpuhp/3]
root          37  0.0  0.0      0     0 ?        S    04:27   0:00 [idle_inject/3]
root          38  0.0  0.0      0     0 ?        S    04:27   0:00 [migration/3]
root          39  0.0  0.0      0     0 ?        S    04:27   0:00 [ksoftirqd/3]
root          41  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/3:0H-events_highpri]
root          42  0.0  0.0      0     0 ?        S    04:27   0:00 [cpuhp/4]
root          43  0.0  0.0      0     0 ?        S    04:27   0:00 [idle_inject/4]
root          44  0.0  0.0      0     0 ?        S    04:27   0:00 [migration/4]
root          45  0.0  0.0      0     0 ?        S    04:27   0:00 [ksoftirqd/4]
root          47  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/4:0H-events_highpri]
root          48  0.0  0.0      0     0 ?        S    04:27   0:00 [cpuhp/5]
root          49  0.0  0.0      0     0 ?        S    04:27   0:00 [idle_inject/5]
root          50  0.0  0.0      0     0 ?        S    04:27   0:00 [migration/5]
root          51  0.0  0.0      0     0 ?        S    04:27   0:00 [ksoftirqd/5]
root          53  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/5:0H-events_highpri]
root          54  0.0  0.0      0     0 ?        S    04:27   0:00 [cpuhp/6]
root          55  0.0  0.0      0     0 ?        S    04:27   0:00 [idle_inject/6]
root          56  0.0  0.0      0     0 ?        S    04:27   0:00 [migration/6]
root          57  0.0  0.0      0     0 ?        S    04:27   0:00 [ksoftirqd/6]
root          59  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/6:0H-events_highpri]
root          60  0.0  0.0      0     0 ?        S    04:27   0:00 [cpuhp/7]
root          61  0.0  0.0      0     0 ?        S    04:27   0:00 [idle_inject/7]
root          62  0.0  0.0      0     0 ?        S    04:27   0:00 [migration/7]
root          63  0.0  0.0      0     0 ?        S    04:27   0:00 [ksoftirqd/7]
root          65  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/7:0H-events_highpri]
root          66  0.0  0.0      0     0 ?        I    04:27   0:01 [kworker/u129:0-kvfree_rcu_reclaim]
root          75  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/u131:5-kvfree_rcu_reclaim]
root          76  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/u131:6-events_unbound]
root          80  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/u130:3-flush-8:0]
root          81  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/u130:4-events_unbound]
root          85  0.0  0.0      0     0 ?        S    04:27   0:00 [kdevtmpfs]
root          86  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-inet_frag_wq]
root          87  0.0  0.0      0     0 ?        S    04:27   0:00 [kauditd]
root          88  0.0  0.0      0     0 ?        S    04:27   0:00 [khungtaskd]
root          89  0.0  0.0      0     0 ?        S    04:27   0:00 [oom_reaper]
root          91  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-writeback]
root          92  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/u129:2-events_unbound]
root          93  0.0  0.0      0     0 ?        S    04:27   0:00 [kcompactd0]
root          94  0.0  0.0      0     0 ?        SN   04:27   0:00 [ksmd]
root          95  0.0  0.0      0     0 ?        SN   04:27   0:00 [khugepaged]
root          96  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-kintegrityd]
root          97  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-kblockd]
root          98  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-blkcg_punt_bio]
root          99  0.0  0.0      0     0 ?        S    04:27   0:00 [irq/9-acpi]
root         102  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/6:1-mm_percpu_wq]
root         103  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/7:1-events]
root         104  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-tpm_dev_wq]
root         105  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-edac-poller]
root         106  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-devfreq_wq]
root         108  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/1:1H-kblockd]
root         109  0.0  0.0      0     0 ?        S    04:27   0:00 [kswapd0]
root         113  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/2:1-cgroup_destroy]
root         114  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/5:1-cgroup_destroy]
root         119  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-kthrotld]
root         720  0.0  0.0   8380  7604 ?        Ss   04:27   0:00 /usr/sbin/haveged --Foreground --verbose=1
root         725  0.0  0.1 113972  9808 ?        Ssl  04:27   0:01 /usr/bin/vmtoolsd
root         730  0.0  0.0 309020  7008 ?        Ssl  04:27   0:00 /usr/libexec/accounts-daemon
message+     733  0.0  0.0  10240  6052 ?        Ss   04:27   0:00 /usr/bin/dbus-daemon --system --address=systemd: --no
polkitd      741  0.0  0.1 382572  9800 ?        Ssl  04:27   0:00 /usr/lib/polkit-1/polkitd --no-debug --log-level=noti
root         742  0.0  0.1  18996  9108 ?        Ss   04:27   0:00 /usr/lib/systemd/systemd-logind
root         837  0.0  0.2 336888 19628 ?        Ssl  04:27   0:00 /usr/sbin/NetworkManager --no-daemon
root         861  0.0  0.1 390916 12264 ?        Ssl  04:27   0:00 /usr/sbin/ModemManager
root        1120  0.1  0.6 2097104 50700 ?       Ssl  04:27   0:02 /usr/bin/containerd
root        1135  0.2  1.2 3024548 101304 ?      Ssl  04:27   0:03 /usr/sbin/dockerd -H fd:// --containerd=/run/containe
root        1145  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-rpciod]
root        1146  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/R-xprtiod]
root        1148  0.0  0.0   6864  2736 ?        Ss   04:27   0:00 /usr/sbin/cron -f
root        1151  0.0  0.0 380976  7020 ?        SLsl 04:27   0:00 /usr/sbin/lightdm
root        1163  1.0  2.3 538916 190508 tty7    Ssl+ 04:27   0:15 /usr/lib/xorg/Xorg :0 -seat seat0 -auth /var/run/ligh
root        1165  0.0  0.0   8160  2388 tty1     Ss+  04:27   0:00 /sbin/agetty -o -- \u --noreset --noclear - linux
root        1195  0.0  0.0      0     0 ?        I    04:27   0:00 [kworker/u129:4-kvfree_rcu_reclaim]
rtkit       1482  0.0  0.0  21472  3016 ?        SNsl 04:27   0:00 /usr/libexec/rtkit-daemon
root        1552  0.0  0.0 1671424 5828 ?        Sl   04:27   0:00 /usr/sbin/docker-proxy -proto tcp -host-ip 127.0.0.1 
root        1562  0.0  0.0 1671168 5792 ?        Sl   04:27   0:00 /usr/sbin/docker-proxy -proto tcp -host-ip 0.0.0.0 -h
root        1569  0.0  0.0 1818888 7840 ?        Sl   04:27   0:00 /usr/sbin/docker-proxy -proto tcp -host-ip :: -host-p
root        1623  0.0  0.3 2059508 24452 ?       Sl   04:27   0:00 /usr/bin/containerd-shim-runc-v2 -namespace moby -id 
root        1625  0.0  0.2 1985776 21140 ?       Sl   04:27   0:00 /usr/bin/containerd-shim-runc-v2 -namespace moby -id 
root        1627  0.0  0.2 2059508 21416 ?       Sl   04:27   0:00 /usr/bin/containerd-shim-runc-v2 -namespace moby -id 
root        1707  0.0  0.0   1040   580 ?        Ss   04:27   0:00 /sbin/docker-init -- /entrypoint.sh /run.sh
dnsmasq     1709  0.0  1.6 1135484 131760 ?      Ssl  04:27   0:00 mariadbd
root        1711  0.0  0.3 193064 31064 ?        Ss   04:27   0:00 apache2 -DFOREGROUND
root        1834  0.0  0.0   4324  3308 ?        S    04:27   0:00 /bin/bash /run.sh
root        2240  0.5  3.9 3824072 317156 ?      Sl   04:27   0:07 /usr/lib/jvm/java-8-openjdk-amd64//bin/java -Dproc_da
www-data    2248  0.0  0.1 193104 11568 ?        S    04:27   0:00 apache2 -DFOREGROUND
www-data    2249  0.0  0.1 193104 11568 ?        S    04:27   0:00 apache2 -DFOREGROUND
www-data    2250  0.0  0.1 193104 11568 ?        S    04:27   0:00 apache2 -DFOREGROUND
www-data    2251  0.0  0.1 193104 11568 ?        S    04:27   0:00 apache2 -DFOREGROUND
www-data    2252  0.0  0.1 193104 11568 ?        S    04:27   0:00 apache2 -DFOREGROUND
root        2361  0.0  0.1 172908 10240 ?        Sl   04:27   0:00 lightdm --session-child 13 24
kali        2375  0.0  0.1  23072 12896 ?        Ss   04:27   0:00 /usr/lib/systemd/systemd --user
kali        2377  0.0  0.0  25048  3780 ?        S    04:27   0:00 (sd-pam)
kali        2397  0.0  0.0   9148  5000 ?        Ss   04:27   0:00 /usr/bin/dbus-daemon --session --address=systemd: --n
kali        2398  0.0  0.1 110788 14008 ?        S<sl 04:27   0:00 /usr/bin/pipewire
kali        2400  0.0  0.0  84744  5220 ?        Ssl  04:27   0:00 /usr/bin/pipewire -c filter-chain.conf
kali        2401  0.0  0.4 613040 33528 ?        S<sl 04:27   0:00 /usr/bin/wireplumber
kali        2402  0.0  0.1  99304  8540 ?        S<sl 04:27   0:00 /usr/bin/pipewire-pulse
kali        2403  0.0  0.1 183148  9812 ?        SLsl 04:27   0:00 /usr/bin/gnome-keyring-daemon --foreground --componen
kali        2404  0.0  0.0   7228  3408 ?        Ss   04:27   0:00 /usr/bin/mpris-proxy
kali        2426  0.0  0.4 347972 34672 ?        Ssl  04:27   0:00 xfce4-session
kali        2493  0.0  0.0 381168  7372 ?        Ssl  04:27   0:00 /usr/libexec/at-spi-bus-launcher
kali        2500  0.0  0.0   8724  4764 ?        S    04:27   0:00 /usr/bin/dbus-daemon --config-file=/usr/share/default
kali        2510  0.0  0.0 168748  7464 ?        Sl   04:27   0:00 /usr/libexec/at-spi2-registryd --use-gnome-session
kali        2518  0.0  0.0  10676  1640 ?        Ss   04:27   0:00 /usr/bin/ssh-agent -s
kali        2527  0.0  0.0 155452  3540 ?        SLsl 04:27   0:00 /usr/bin/gpg-agent --supervised
kali        2530  0.3  1.5 1774312 125496 ?      Sl   04:27   0:05 xfwm4
kali        2534  0.0  0.0 312640  7572 ?        Ssl  04:27   0:00 /usr/libexec/gvfsd
kali        2541  0.0  0.0 398372  6712 ?        Sl   04:27   0:00 /usr/libexec/gvfsd-fuse /run/user/1000/gvfs -f
kali        2570  0.0  0.3 275388 26272 ?        Sl   04:27   0:00 xfsettingsd
kali        2575  0.0  0.0 165232  5676 ?        Ssl  04:27   0:00 /usr/libexec/dconf-service
root        2579  0.0  0.0      0     0 ?        I<   04:27   0:00 [kworker/u137:1]
kali        2580  0.0  0.5 506336 43720 ?        Sl   04:27   0:00 xfce4-panel
kali        2585  0.0  0.2 411548 23908 ?        Sl   04:27   0:00 Thunar --daemon
kali        2591  0.1  1.1 671400 95024 ?        Sl   04:27   0:01 xfdesktop
kali        2595  0.0  0.5 428672 42340 ?        Sl   04:27   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /us
kali        2599  0.2  1.0 265316 89412 ?        Sl   04:27   0:03 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /us
kali        2600  0.0  0.3 411516 24960 ?        Sl   04:27   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /us
kali        2601  0.1  0.3 274020 28356 ?        Sl   04:27   0:02 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /us
kali        2602  0.0  0.4 359424 39204 ?        Sl   04:27   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /us
kali        2603  0.0  0.4 425628 37224 ?        Sl   04:27   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /us
kali        2604  0.0  0.4 286496 38108 ?        Sl   04:27   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /us
kali        2606  0.0  0.4 425856 38008 ?        Sl   04:27   0:00 /usr/lib/x86_64-linux-gnu/xfce4/panel/wrapper-2.0 /us
kali        2642  0.0  0.2 341848 19512 ?        Ssl  04:27   0:00 /usr/lib/x86_64-linux-gnu/xfce4/notifyd/xfce4-notifyd
root        2647  0.0  0.1 319064 10480 ?        Ssl  04:27   0:00 /usr/libexec/upowerd
kali        2655  0.0  0.5 587092 43376 ?        Sl   04:27   0:00 nm-applet
kali        2657  0.0  0.4  64708 39588 ?        S    04:27   0:00 /usr/bin/python3 /usr/share/system-config-printer/app
kali        2670  0.0  0.0  12424  1656 ?        Ssl  04:27   0:00 xcape -e Super_L Control_L Escape
kali        2672  0.0  0.4 209472 35320 ?        Sl   04:27   0:00 xfce4-screensaver
kali        2673  0.0  0.1 191040 16216 ?        Sl   04:27   0:00 /usr/libexec/polkit-mate-authentication-agent-1
kali        2675  0.0  0.0 316716  6140 ?        Sl   04:27   0:00 /usr/libexec/geoclue-2.0/demos/agent
kali        2685  0.0  0.7 529184 58532 ?        Sl   04:27   0:00 /usr/bin/python3 /usr/bin/blueman-applet
kali        2687  0.0  0.1 922612  8236 ?        Sl   04:27   0:00 xiccd
kali        2690  0.1  0.4 148728 38556 ?        Sl   04:27   0:01 /usr/bin/vmtoolsd -n vmusr --blockFd 3
kali        2691  0.0  0.2 336560 23792 ?        Sl   04:27   0:00 xfce4-power-manager
colord      2758  0.0  0.1 315952 14392 ?        Ssl  04:27   0:00 /usr/libexec/colord
kali        2837  0.0  0.1 391008 10640 ?        Ssl  04:27   0:00 /usr/libexec/gvfs-udisks2-volume-monitor
root        2841  0.0  0.1 404296 13536 ?        Ssl  04:27   0:00 /usr/libexec/udisks2/udisksd
kali        2846  0.0  0.2 378764 18000 ?        Ssl  04:27   0:00 /usr/libexec/bluetooth/obexd
kali        2851  0.0  0.0 307932  6744 ?        Ssl  04:27   0:00 /usr/libexec/gvfs-mtp-volume-monitor
kali        2856  0.0  0.0 308884  6956 ?        Ssl  04:27   0:00 /usr/libexec/gvfs-gphoto2-volume-monitor
kali        2867  0.0  0.1 390032  8592 ?        Ssl  04:27   0:00 /usr/libexec/gvfs-afc-volume-monitor
kali        2873  0.0  0.0 307828  6400 ?        Ssl  04:27   0:00 /usr/libexec/gvfs-goa-volume-monitor
kali        2894  0.0  0.0 168880  6496 ?        Ssl  04:27   0:00 /usr/libexec/gvfsd-metadata
kali        2906  0.0  0.1 534080  8544 ?        Sl   04:27   0:00 /usr/libexec/gvfsd-trash --spawner :1.24 /org/gtk/gvf
kali        2930  0.2  0.8 732188 68676 ?        Sl   04:27   0:03 /usr/bin/qterminal
kali        2932  0.0  0.2 556916 19316 ?        Ssl  04:27   0:00 /usr/libexec/xdg-desktop-portal
kali        2938  0.0  0.0 308740  6424 ?        Ssl  04:27   0:00 /usr/libexec/xdg-permission-store
kali        2946  0.0  0.0 614480  6864 ?        Ssl  04:27   0:00 /usr/libexec/xdg-document-portal
root        2952  0.0  0.0   2584  1800 ?        Ss   04:27   0:00 fusermount3 -o rw,nosuid,nodev,fsname=portal,auto_unm
kali        2959  0.0  0.2 406556 18908 ?        Ssl  04:27   0:00 /usr/libexec/xdg-desktop-portal-gtk
kali        2969  0.0  0.0  13628  7376 pts/0    Ss   04:27   0:00 /usr/bin/zsh
root        5565  0.0  0.0      0     0 ?        I    04:32   0:00 [kworker/u132:0-kvfree_rcu_reclaim]
root        5659  0.0  0.0      0     0 ?        I    04:32   0:00 [kworker/u130:0-kvfree_rcu_reclaim]
root        8366  0.0  0.0      0     0 ?        I    04:37   0:00 [kworker/u132:3-events_unbound]
root        8861  0.0  0.0      0     0 ?        I    04:38   0:00 [kworker/u131:0-flush-8:0]
root        9552  0.2  0.0      0     0 ?        I    04:39   0:01 [kworker/3:0-mm_percpu_wq]
root       10884  0.0  0.0      0     0 ?        I    04:42   0:00 [kworker/0:0-mm_percpu_wq]
root       11000  0.0  0.0      0     0 ?        I    04:42   0:00 [kworker/4:0]
root       13335  0.0  0.0      0     0 ?        I    04:46   0:00 [kworker/5:0-events]
root       13748  0.0  0.0      0     0 ?        I    04:47   0:00 [kworker/7:0-events_power_efficient]
kali       15286  0.0  0.0   9532  4068 pts/0    R+   04:50   0:00 ps aux

```
</p></details>
- [x] 14. Оформить `README.md` по аналогии и использовать `shield`, etc.
- [x] 15. Составить `gist` отчет и отправить ссылку личным сообщением
[gist отчет](https://gist.github.com/Electro1ux/2ce7c6623c6c64229a64115359900cd7)
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
