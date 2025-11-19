<div align="center">
<h1><a id="intro"> Лабораторные работы <sup><kbd>intro</kbd></sup></a><br></h1>

***

### Этапы реализации
    
1.  Порядок выполнения работ:

-  [ ] lab01 - <a href="https://github.com/geminishkv/course_labs/blob/develop/labs/lab01/README.md"> Лабораторная работа посвящена изучению систем обмена данными и подготовительными материалами для последующих работ</a>
-  [ ] **Обновление будет предоставлено позднее**

***

### Формализованные требования 

- ✔️ Единый стиль кода
- ✔️ Все функции по работе с деревом должны находиться в пространстве имен
- ✔️ Оформление `README.md` в соответствии с содержанием проекта
- ✔️ Оформление `.gitignore` в соответствии с содержанием проекта
- ✔️ Использовать подходящий тип `LICENSE` для проекта
- ✔️ Создать и использовать скрипты для автоматизации сборки проекта, примеров, тестов, пакетирования
- ✔️ Обеспечить непрерывный процесс сборки проекта с использованием сервиса **Travis CI/ AppVeyor** (**community edition**)
- ✔️ Обеспечить 100% покрытие кода с использованием фреймворков
- ✔️ Написать документацию к проекту с использованием инструмента **doxygen** и разместить ее на сервисе GitHub Pages
- ✔️ Обеспечить размещение пакета проекта на сервисе GitHub Release при успешном слияние ветки develop и master
- ✔️ Проконтролировать корректную эксплуатацию проекта
- ✔️ Рефакторинг и поддержка лабораторных работ в процессной деятельности
- ✔️ Все команды выполняться строго их терминала/ консоли без использования WebUI за исключениям работы с токенами, ключами и специфичными настройками.

***

### Сопроводительыне материалы

- gitscm

```sh
$ git init # Инициализация пустого локального репозитория
$ git remote add origin URL_link # Связывание удалённого репозитория с именем "origin" по ссылке "URL_link" с локальным
$ git pull origin name_branch # Ветка из которой мы берем изменения для тестирования
$ git remote show # Показать подключенные удалённые репозитории
$ git status 	# Показывает состояние локального репозитория (отслеживаемые, изменённые, новые файлы и пр.)
$ git add . # Добавить в индекс все новые, изменённые, удалённые файлы из текущей директории и её поддиректорий
$ git commit -S -m"added sources" # Зафиксировать в коммите проиндексированные изменения (закоммитить), добавить сообщение
$ git push origin name_branch # Отправляем изменения из локально репозитория в удалённый в ветку "name_branch"
$ git show HEAD # Информация о последнем комите (git log -1)
$ git clean -fdn # Удаляет неотслеживаемые файлы и каталоги с предворительным просмотром
$ git push --set-upstream origin new-name # Установка upstream (связывает локальную ветку с удаленной)
$ git remote show # Вывод связанных веток
$ git push origin :old-name # Удаление старой ветки в удаленном репо
$ git push origin new-name # Публикация новой ветки
```

- gitscm index

```bash
$ git add text.txt # Добавить в индекс указанный файл (был изменён, был удалён или это новый файл)
$ git add -i # Запустить интерактивную оболочку для добавления в индекс только выбранных файлов
$ git add -p # Показать новые/изменённые файлы по очереди с указанием их изменений и вопросом об отслеживании/индексировании
$ git reset # Убрать из индекса все добавленные в него изменения (в рабочей директории все изменения сохранятся), антипод git add
$ git reset readme.txt # Убрать из индекса изменения указанного файла (в рабочей директории изменения сохранятся)
$ git checkout text.txt # ОПАСНО: отменить изменения в файле, вернуть состояние файла, имеющееся в индексе
$ git reset --hard # ОПАСНО: отменить изменения; вернуть то, что в коммите, на который указывает HEAD (незакомиченные изменения удалены из индекса и из рабочей директории, неотслеживаемые файлы останутся на месте)
$ git clean -df # Удалить неотслеживаемые файлы и директории
```

- gitscm конфликты

```bash

$ git remote set-url origin ssh://git@github.com_gitlab.com/username/newRepoName.git # Замена URL
$ git pull --rebase origin name_branch # Переинициализация
$ git remote -v # Проверка правильности указанного link
$ git reset HEAD~ # Отмена последнего commit $ git reset --hard HEAD~ # Удаление commit с изменениями
$ git push origin --delete name_branch / git branch -rD origin/name_branch
$ git branch -d name_branch # Удаление локального репо
$ git reset HEAD file # Убирает файл из индекса
$ git checkout -- file # Отменяет изменение
$ git clean -fdn # Удаляет неотслеживаемые файлы и каталоги с предварительным просмотром
```

- gh actions

```bash
$ gh auth login
$ gh repo create repo_name # Cоздание удаленного репозитория (без URL)
$ gh pr create # pull reguest
	 —assignee «nickname» 
	 --base main 
	 --head feature-branch # Индивидуальный pull request (можно -a)
$ gh pr create --title "Bug" --body "work" $ gh pr create --base base_name # head changed_branch $ gh repo create repo_name --source=. --public
$ gh repo clone user/repo
$ gh issue list # Список открытых issue
$ gh pr create --title "Название" --body "Описание" --base main --head feature-branch
	 --title # Заголовок PR
	 --body # Описание
	 --base # Целевая ветка
	 --head # Ваша ветка
$ gh pr merge --squash
$ gh repo view --web # Открыть репозитория в web
```

- gistup

```bash
$ npm install -g gistup
$ gh <command> <subcommand> --help
$ gh gist create -d "my test gist" -f some_local_file.txt  test_gist
```

- .gitignore

```
*build*/
*install*/
*.swp
.idea/
```

***

### Приложение:

<details><summary><strong>Указатели</strong></summary><p>

- `HEAD` — указатель на текущий коммит или на текущую ветку (то есть, в любом случае, на коммит). Указывает на родителя коммита, который будет создан следующим.
- `ORIG_HEAD` — указатель на коммит, с которого вы только что переместили `HEAD` (командой `git reset` ..., например).
- Ветка (`master`, `develop` etc.) — указатель на коммит. При добавлении коммита, указатель ветки перемещается с родительского коммита на новый.
- Теги — простые указатели на коммиты. Не перемещаются.

 </p></details></div>
 
<details><summary><strong>ENV</strong></summary><p>

Команда git config позволяет управлять конфигурацией (примеры для --global)

- Локальный (--local) - только для текущего репозитория, файл .git/config
- Глобальный (--global) - для пользователя, файл ~/.gitconfig
- Системный (--system) - для всех пользователей /etc/gitconfig

 </p></details></div>

<details><summary><strong>Unix commands</summary><p>

- [ar](https://en.wikipedia.org/wiki/Ar_(Unix))
- [cat](https://en.wikipedia.org/wiki/Cat_(Unix))
- [cd](https://en.wikipedia.org/wiki/Cd_(command))
- [cp](https://en.wikipedia.org/wiki/Cp_(Unix))
- [cut](https://en.wikipedia.org/wiki/Cut_(Unix))
- [echo](https://en.wikipedia.org/wiki/Echo_(command))
- [env](https://en.wikipedia.org/wiki/Env_(shell))
- [ex](https://en.wikipedia.org/wiki/Ex_(editor))
- [file](https://en.wikipedia.org/wiki/File_(command))
- [find](https://en.wikipedia.org/wiki/Find)
- [ls](https://en.wikipedia.org/wiki/Ls)
- [man](https://en.wikipedia.org/wiki/Man_page)
- [mkdir](https://en.wikipedia.org/wiki/Mkdir)
- [mv](https://en.wikipedia.org/wiki/Mv)
- [nm](https://en.wikipedia.org/wiki/Nm_(Unix))
- [ps](https://en.wikipedia.org/wiki/Ps_(Unix))
- [pwd](https://en.wikipedia.org/wiki/Pwd)
- [rm](https://en.wikipedia.org/wiki/Rm_(Unix))
- [sed](https://en.wikipedia.org/wiki/Sed)
- [touch](https://en.wikipedia.org/wiki/Touch_(Unix))

</p></details></div>
