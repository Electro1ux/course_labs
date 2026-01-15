<div align="center">
<h1><a id="intro">Лабораторная работа №5</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a> 
<a href="https://symbl.cc/en/unicode-table"><img src="https://img.shields.io/static/v1?logo=unicode&logoColor=fff&label=&message=Unicode&color=36393f&style=flat" alt="Unicode"></a> 
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<a href="https://img.shields.io/badge/Risk_Analyze-2448a2"><img src="https://img.shields.io/badge/Course-Risk_Analysis-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/AppSec-2448a2" alt= "RA"></a> <img src="https://img.shields.io/badge/Contributor-Шмаков_И._С.-8b9aff" alt="Contributor Badge"></a></div>

***

Салют :wave:,<br>
Данная лабораторная работа посвещена изучению Docker и как с ним работать. Эта лабораторная работа послужит подпоркой для старта в выявлении и определении уязвимостей на уровне сканирования контейнеров при сборке приложений. 

Для сдачи данной работы также будет требоваться ответить на дополнительыне вопросы по описанным темам.

***

## Структура репозитория лабораторной работы

```bash
lab05
├── client
│   ├── client.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
├── README.md
├── server
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
└── source
    ├── Dockerfile
    ├── hello.py
    ├── image.tar
    └── requirements.txt
```

***

## Материал

- **Контейнеризация**

Сборка приложения включает создание контейнерного образа, в котором упаковано приложение с конфигурациями, что бы приложение функционировало. `Docker` основан на использовании общих функций ядра `ОС Linux` (`cgroups`, `namespace`) для изоляции и управления ресурсами.

> **Образ** — это статический, неизменяемый шаблон, на базе которого создаются контейнера с ОС, приложением, зависимостями, библиотекакм и конфигурационными файлами. Нужен для создания воспроизводимой, неизменяемой среды выполнения приложений в контейнерах.

Для сборки образов используется `Dockerfile`, где прописаны версии зависимостей и инструкции, минимизирующие разрешения и атаки. Это инструкции, где описывается, как собрать образ. Впоследствии собирается контейнер.

> **Контейнер** — это изолированная среда выполнения приложения с необходимыми зависимостями, кодом, системными утилитами, библиотеками и настройками. Исползует не собственну гостеву ОС, а ядро хостовой ОС и имеет своё собственное файловое пространство, процессы и сеть.

После сборки образа формируется контейнер, которые являются изолированными средами выполнения для достижения цели переносимости, воспроизведения.

> **Контейнеризация** — это технология, позволяющая упаковать приложение вместе со всеми его зависимостями, библиотеками, настройками и средой выполнения в единый изолированный виртуальный контейнер. 

- **Namespaces**

Необходимы для организации изолированных рабочих пространств, - контейнеров. Когда мы запускаем контейнер, `Docker` создает набор пространств имен для данного контейнера, что создает изолированный уровень в своем простанстве имен и не имеет доступа к внешней системе. Пространство имен:

> - pid: для изоляции процесса
> - net: для управления сетевыми интерфейсами
> - ipc: для управления IPC ресурсами. (ICP: InterProccess Communication)
> - mnt: для управления точками монтирования
> - utc: для изолирования ядра и контроля генерации версий(UTC: Unix timesharing system)

- **Cgroups**

Необходимы для контрольных групп в изоляции, где предоставляется приложению только те ресурсы, которые указываем. Позволяют разделять ресурсы железа и устанавливать пределы, ограничения.

```bash
$ docker container run d \
        —e NGINX_HOST xxx.xxx \
        —p 8080:80 \
        –-v "$PWD/html" usr/share/nginx/html \
        —memory=50m \
        —cpus="2.5" \
        nginx
```

-  **Основные проблемы**

    - образ может содержать устаревшие или уязвимые версии библиотек CVE (Common Vulnerabilities and Exposures)
    - поддельные и злонамеренные образы
    - отсутствие подписей и проверки целостности
    - ошибка конфигурации и избыток прав — образы с избыточными правами доступа, запуском от root или с небезопасными настройками
    - присутствие секретов и конфиденциальных данных в образах
    - отсутствие регулярного обновления из-за неподдерживаемых образов

-  **Контекст безопасности**

    - Не задавать пользователей с правами «root» для работы сервисов внутри контейнеров. 
        > Если для функционирования сервиса не требуются расширенные привилегии, то в Dockerfile необходимо явно прописать учетную запись пользователя с минимально необходимыми правами.
    - Не запускать контейнеры в привилегированном режиме. 
        > Ключ «--privileged» отключает все средства изоляции (наложенные cgroup – контроллером устройства) docker-контейнера. Запуск контейнера с таким ключом обеспечит ему доступ к файловой системе и блочным устройствам (например, жесткому диску) хоста. Контейнеры должны быть запущены в непривилегированном режиме. Если контейнеру нужны дополнительные привилегии для корректной работы, то необходимо явно прописать или удалить требуемые docker capabilities.
    - Не отключать профили безопасности Docker. 
        > По умолчанию для запуска контейнеров Docker использует профили безопасности Linux, лучше использовать профили AppArmor, SELinux, grsecurity, seccomp, - позволяют ограничить активности контейнера, обеспечивая контроль сети, использования дополнительных возможностей (docker capabilities), контроль обращений к файловой системе хоста и пр. Контейнеры должны работать с активными профилями безопасности Docker, не docker-default. Если необходимо использовать другой профиль, то это можно сделать с помощью --security-opt.
    - Не допускать запуск контейнеров, использующих тип сети «host»
        > В режиме Host контейнер использует ту же сеть, что и хост, т.е. контейнерная сеть не изолируется от сети Docker хоста и контейнер не получает собственный IP-адрес, что дает доступ к REST API daemon docker изнутри контейнера, а также к устройствам, расположенным в сети хоста. Для реализации сетевого взаимодействия между контейнерами, они должны запускаться в режиме bridge или none.
    - Не разрешать доступ к docker.socket изнутри контейнера. Не подключать docker socket в контейнер без необходимости, либо с использованием плагинов авторизации. 
    - Не использовать секреты в открытом виде в Docker-файлах образов. По возможности не использовать переменные окружения и не хранить секреты внутри контейнера. Хранение и управление секретами возложить на сторонний сервис.
    - Ограничивать и контролировать использование ресурсов контейнерами. Указывать ограничения на уровне самого ПО или на уровне контейнеров для использования ресурсов хоста.
    - Контролировать качество базовых образов контейнеров. Использовать официальные образы и использовать образы с минимально необходимым набором инструментов.
    - Сканировать образы на наличие уязвимостей и проверки требований ИБ (Compliance Checks)

- **Дополнительно**

В случае, если возникает проблема с вызовом `docker buildx` для macos `silicon`, следует использовать вот [это](https://gist.github.com/Aeonitis/cbd9f8b61eaec5a8a024c0a42f415ca3) описание из gistup для фикса `samelink`.

***

## Задание

- [x] 1. Поставьте `Docker` и `buildkit`

```bash
brew install buildkit   # Устанавливает BuildKit — движок сборки Docker-образов
brew install docker     # Устанавливает Docker для работы с контейнерами

```

- [x] 2. Перейдите в `source` и выведите на терминале, далее проанализируйте следующие команды консоли

```bash
# Сборка Docker-образа из Dockerfile в текущем каталоге с присвоением тега hellow-appsec-world
$ docker buildx build -t hellow-appsec-world .

┌──(kali㉿kali)-[~/course_labs/labs/lab05/source]
└─$ docker buildx build -t hellow-appsec-world .
[+] Building 34.3s (13/13) FINISHED                                                                                                                          docker:default
 => [internal] load build definition from Dockerfile                                                                                                                   0.1s
 => => transferring dockerfile: 429B                                                                                                                                   0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                                                                                    8.3s
 => [internal] load .dockerignore                                                                                                                                      0.0s
 => => transferring context: 2B                                                                                                                                        0.0s 
 => [builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                      6.6s 
 => => resolve docker.io/library/python:3.11-slim@sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c                                              0.0s
 => => sha256:3f0cdbca744e7bd0ce0ff6da73b9148829b04309925992954a314ba203f56e99 249B / 249B                                                                             1.6s 
 => => sha256:158caf0e080e2cd74ef2879ed3c4e697792ee65251c8208b7afb56683c32ea6c 10.37kB / 10.37kB                                                                       0.0s
 => => sha256:26fe52250f1b8012f5061c8f7228e6fca4f100aa3f99b41a8aa2608a42c5db43 1.75kB / 1.75kB                                                                         0.0s 
 => => sha256:cb352e69d7b69f39dbc2cc35ecc34d01ca14439abc55911a5f7932f3dd6bd079 5.48kB / 5.48kB                                                                         0.0s 
 => => sha256:72cf4c3b83019e176aba979aba419d35f56576bbcfc4f7249a1ab1d4b536730b 1.29MB / 1.29MB                                                                         1.9s 
 => => sha256:4d55cfecf3663813d03c369bcd532b89f41cf07b65d95887ef686538370a747c 14.36MB / 14.36MB                                                                       4.1s
 => => extracting sha256:72cf4c3b83019e176aba979aba419d35f56576bbcfc4f7249a1ab1d4b536730b                                                                              0.3s
 => => extracting sha256:4d55cfecf3663813d03c369bcd532b89f41cf07b65d95887ef686538370a747c                                                                              2.2s 
 => => extracting sha256:3f0cdbca744e7bd0ce0ff6da73b9148829b04309925992954a314ba203f56e99                                                                              0.0s 
 => [internal] load build context                                                                                                                                      0.0s 
 => => transferring context: 474B                                                                                                                                      0.0s 
 => [builder 2/4] WORKDIR /hello                                                                                                                                       0.3s 
 => [builder 3/4] COPY requirements.txt .                                                                                                                              0.1s
 => [builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r requirements.txt                                                                  15.0s 
 => [stage-1 3/6] COPY --from=builder /wheels /wheels                                                                                                                  0.0s 
 => [stage-1 4/6] COPY requirements.txt .                                                                                                                              0.0s 
 => [stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt                                                                                  2.9s 
 => [stage-1 6/6] COPY hello.py .                                                                                                                                      0.1s 
 => exporting to image                                                                                                                                                 0.2s 
 => => exporting layers                                                                                                                                                0.1s 
 => => writing image sha256:a79810c83f55ca120983c1168760eddd8c12d729c547e459e724aca66d1096f4                                                                           0.0s
 => => naming to docker.io/library/hellow-appsec-world

 
# Запуск контейнера из образа hello-appsec-world с выполнением команды по умолчанию
$ docker run hello-appsec-world


┌──(kali㉿kali)-[~/course_labs/labs/lab05/source]
└─$ docker run hellow-appsec-world 
hello appsec world


# Запуск контейнера в интерактивном режиме с автоматическим удалением после завершения
$ docker run --rm -it hello-appsec-world


┌──(kali㉿kali)-[~/course_labs/labs/lab05/source]
└─$ docker run --rm -it hellow-appsec-world
hello appsec world


# Экспорт Docker-образа hello-appsec-world в архив hello.tar
$ docker save -o hello.tar hello-appsec-world


┌──(kali㉿kali)-[~/course_labs/labs/lab05/source]
└─$ docker save -o hello.tar hellow-appsec-world


# Импорт Docker-образа из архива hello.tar в локальное хранилище
$ docker load -i hello.tar


┌──(kali㉿kali)-[~/course_labs/labs/lab05/source]
└─$ docker load -i hello.tar
Loaded image: hellow-appsec-world:latest

```

- [x] 3. Откройте `Dockerfile` и сделайте его анализ. Сделайте `commit`
- [x] 4. Замените в `Dockerfile`значение скрипта на `python` тем, который вы сделали ранее в прошлых лабораторных работах. Вложите свой файл `python` в директорию. Сделайте анализ своего измененного `Dockerfile` и внесите изменения. Сделайте `commit`. 

```dockerfile
# Использование официального образа Python версии 3.11 на базе slim
FROM python:3.11-slim

# Установка рабочей директории внутри контейнера
WORKDIR /hello

# Копирование файла зависимостей в контейнер
COPY requirements.txt .

# Установка зависимостей из файла requirements.txt без кэширования pip
RUN pip install --no-cache-dir -r requirements.txt

# Копирование основного Python-скрипта в контейнер
COPY screen.py .

# Команда запуска приложения при старте контейнера
CMD ["python", "screen.py"]
```

- [x] 5. Выведите на терминале и проанализируйте следующие команды консоли. Сравните хеш сумму вашего архива с `image.tar` из репозитория, выведите на терминал.

```bash
$ docker buildx build -t hellow-appsec-world .

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker buildx build -t hellow-appsec-world .
[+] Building 1.5s (10/10) FINISHED                                                           docker:default
 => [internal] load build definition from Dockerfile                                                   0.0s
 => => transferring dockerfile: 781B                                                                   0.0s
 => [internal] load metadata for docker.io/library/python:3.11-slim                                    1.3s
 => [internal] load .dockerignore                                                                      0.0s
 => => transferring context: 2B                                                                        0.0s
 => [1/5] FROM docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db522  0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db522  0.0s
 => [internal] load build context                                                                      0.0s
 => => transferring context: 66B                                                                       0.0s
 => CACHED [2/5] WORKDIR /hello                                                                        0.0s
 => CACHED [3/5] COPY requirements.txt .                                                               0.0s
 => CACHED [4/5] RUN pip install --no-cache-dir -r requirements.txt                                    0.0s
 => CACHED [5/5] COPY screen.py .                                                                      0.0s
 => exporting to image                                                                                 0.1s
 => => exporting layers                                                                                0.0s
 => => exporting manifest sha256:902f461a8e15494c032c0fe734b971afd20a45502323011063f4134483e5c121      0.0s
 => => exporting config sha256:8cee8d2ef455f2f094fa484244ba7de392e1468facb60dae0dc28bbfaa0d5e52        0.0s
 => => exporting attestation manifest sha256:21e261258c515d4eb38d81c953d97fbf787728e7854309d9ae4302bd  0.0s
 => => exporting manifest list sha256:ecb8a49f889029387ea66e0f85565c6f167d5c4640c3bbb4dba3920ca0ea27f  0.0s
 => => naming to docker.io/library/hellow-appsec-world:latest                                          0.0s
 => => unpacking to docker.io/library/hellow-appsec-world:latest                                       0.0s

$ docker run hello-appsec-world

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker run -it hellow-appsec-world python screen.py Ilia --formal
Добрый день, Ilia !

$ docker save -o hello_ypur_project.tar hello-appsec-world # Экспорт Docker-образа в tar-архив для переноса/хранения

$ docker load -i hello_ypur_project.tar # Импорт Docker-образа из tar-архива в локальное хранилище Docker

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker load -i hello_your_project.tar
Loaded image: hellow-appsec-world:latest

$ docker run hello-appsec-world

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker run -it hellow-appsec-world python screen.py ilia
Привет, ilia!

$ docker load -i image.tar # Отсутствует в репозитории
$ docker run hello-appsec-world

sha256sum hello_your_project.tar hello.tar # Сравнение SHA-256 хеш-сумм tar-архивов
fc038363d11e43caa9a8dc0d84f9ac406b869f2bd34f1c97c47414aaebb2dc22  hello_your_project.tar
f4ee477e47d161a2b481c45d07a2b7e96cab55c2434d41b75cd2d90a9bdc8887  hello.tar
```

- [x] 6. Доработайте свой `python` скрипт подключаемыми библиотеками, далее их необходимо разместить в `requirements.txt`.

```
typer==0.12.3
click==8.1.7
```

- [x] 7. Сделайте `commit`. Повторите сборку приложения по вашему `Dockerfile` для доработанного скрипта `python`. Сохраните `image` в виде .`tar` архива. Сделайте `commit`.

- [x] 8. Выведите на терминале и проанализируйте следующие команды консоли

```bash
$ docker login # Аутентификация в Docker Hub для выполнения операций push/pull с приватными/публичными репозиториями

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker login
Authenticating with existing credentials...
Login Succeeded

$ docker tag hellow-appsec-world ris4png/hellow-appsec-world  # Присваивает локальному образу новый тег в формате <username>/<repository> для публикации в Docker Hub
$ docker push ris4png/hellow-appsec-world # Загружает образ в репозиторий Docker Hub под тегом latest

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker push ris4png/hellow-appsec-world
Using default tag: latest
The push refers to repository [docker.io/ris4png/hellow-appsec-world]
ce2751bd8e70: Pushed
8e8e7b82c7e8: Pushed
654a090213c0: Pushed
2e4e98528339: Pushed
90c2ea222de4: Pushed
7cc13cb22d92: Pushed
18534482b4f8: Pushed
02d7611c4eae: Pushed
1473863bb010: Pushed
latest: digest: sha256:ecb8a49f889029387ea66e0f85565c6f167d5c4640c3bbb4dba3920ca0ea27f4 size: 856


$ docker inspect ris4png/hellow-appsec-world # Выводит полную информацию об образе: архитектура, команды запуска, переменные окружения, слои, хеши

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker inspect ris4png/hellow-appsec-world
[
    {
        "Id": "sha256:ecb8a49f889029387ea66e0f85565c6f167d5c4640c3bbb4dba3920ca0ea27f4",
        "RepoTags": [
            "hellow-appsec-world:latest",
            "ris4png/hellow-appsec-world:latest"
        ],
        "RepoDigests": [
            "hellow-appsec-world@sha256:ecb8a49f889029387ea66e0f85565c6f167d5c4640c3bbb4dba3920ca0ea27f4",
            "ris4png/hellow-appsec-world@sha256:ecb8a49f889029387ea66e0f85565c6f167d5c4640c3bbb4dba3920ca0ea27f4"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2026-01-11T18:27:12.835490526Z",
        "DockerVersion": "27.3.1",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78"
            ],
            "Cmd": [
                "python",
                "screen.py"
            ],
            "ArgsEscaped": true,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "/hello",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "amd64",
        "Os": "linux",
        "Size": 53660949,
        "GraphDriver": {
            "Data": null,
            "Name": "overlayfs"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:6a7f953ae30c9f480e6eaf7be8b1ba742bce57a3a83c43e927348e763cff7472",
                "sha256:501421e049a171e15631e0b0e231ffd456ee4685f5b5b22cd98163cde83f2c6c",
                "sha256:72533f233c8abf13e297ce15ecbd0ca43a452405a88cb704f3e43a8db89ffe90",
                "sha256:253032e9f52a50fa025102eb1834cb841de4963cbebf37c593c147ccc36f537c",
                "sha256:11ce9b496c39580d6d14f8c9e248fd341ce157a7b30e687363416bbe4b5027a3",
                "sha256:5344190aae7c3cd45ca8d28aaf7302f6b9fd61fbbd91ef406079aaa04cc739f1",
                "sha256:fb892b8271472eff0078fbaacd110c2f2841b1f21011a9b466d9e0ed1b4dff1e",
                "sha256:53975fd0e82e6b209832610f13fa6b0e8604ae34d3c1e1ecdd686663631b75e7"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-01-11T18:51:35.639748192Z"
        }
    }
]

$ docker container create --name first hello-appsec-world # Создаёт контейнер с именем first из указанного образа, не запуская его; выводит идентификатор контейнера

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker container create --name first hellow-appsec-worl
d
8720e74038eee75761b472bd965d98e3e113915b697c0805eb769273bec11155

$ docker image pull geminishkv/hello-appsec-world # Загружает образ из удалённого реестра (Docker Hub) в локальное хранилище Docker

 docker pull --platform linux/arm64 geminishkvdev/hello-appsec-world:latest
latest: Pulling from geminishkvdev/hello-appsec-world
61170947d8ae: Download complete
89477b9ce6a6: Download complete
44032d6d082a: Download complete
158b441f91fd: Download complete
b89cf3ec7a3e: Download complete
73c6786ffe40: Download complete
602731d4ffe4: Download complete
9673dc38d14b: Download complete
460204959e1c: Download complete
Digest: sha256:f9db3113962ac3bb47d0123dc8f16b2baa3a27fdef5db67b0d1bd0d6c7bdcdf2
Status: Downloaded newer image for geminishkvdev/hello-appsec-world:latest
docker.io/geminishkvdev/hello-appsec-world:latest

$ docker inspect geminishkvdev/hello-appsec-world

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker inspect geminishkvdev/hello-appsec-world
[
    {
        "Id": "sha256:f9db3113962ac3bb47d0123dc8f16b2baa3a27fdef5db67b0d1bd0d6c7bdcdf2",
        "RepoTags": [
            "geminishkvdev/hello-appsec-world:latest"
        ],
        "RepoDigests": [
            "geminishkvdev/hello-appsec-world@sha256:f9db3113962ac3bb47d0123dc8f16b2baa3a27fdef5db67b0d1bd0d6c7bdcdf2"
        ],
        "Parent": "",
        "Comment": "buildkit.dockerfile.v0",
        "Created": "2025-11-21T13:46:41.586622834Z",
        "DockerVersion": "27.3.1",
        "Author": "",
        "Config": {
            "Hostname": "",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
                "PYTHON_VERSION=3.11.14",
                "PYTHON_SHA256=8d3ed8ec5c88c1c95f5e558612a725450d2452813ddad5e58fdb1a53b1209b78",
                "PYTHONUNBUFFERED=1"
            ],
            "Cmd": [
                "python",
                "hello.py"
            ],
            "ArgsEscaped": true,
            "Image": "",
            "Volumes": null,
            "WorkingDir": "/hello",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": null
        },
        "Architecture": "arm64",
        "Os": "linux",
        "Size": 49801218,
        "GraphDriver": {
            "Data": null,
            "Name": "overlayfs"
        },
        "RootFS": {
            "Type": "layers",
            "Layers": [
                "sha256:f1b30ab9918326dc2f4c25f16c0e6c13e9a48427441ea41c0e4d8f3e6699da24",
                "sha256:c240010145420619581e4f7b7e4047e460c8555234e3e4db66f890a68e146f24",
                "sha256:7a4b2171e46dd80cd00f895405c44a867a96ab97e17b4e8c9651cc5e4f419369",
                "sha256:591779db32736fe4b356f6cecc88221a5fa8afa34cbced6e719e54584f63ef59",
                "sha256:efd49302dd30654a15a04a446a25ced6b712e90c6dd4e7791700e6cc57052500",
                "sha256:8fe7432c3de3dffd75d5c59ba9c0ab11f79fbafa983ee88df0ace1aa14d4a194",
                "sha256:e687a26fd0a6b3205299a590d71ae34d679adaaf2b653b0707449ebb676354b9",
                "sha256:71299f61dc2b0b021efdcf665174aae82972a5a8d32bc733c4e2fbc6f7c7a10f",
                "sha256:5b8b2e16a223e538a7cde134a8d2da34674bea14b95915fc1314cd8af5805608"
            ]
        },
        "Metadata": {
            "LastTagTime": "2026-01-11T18:58:15.490092058Z"
        }
    }
]

$ docker container create --name second hello-appsec-world

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker container create --name second geminishkvdev/hel
lo-appsec-world
WARNING: The requested image's platform (linux/arm64) does not match the detected host platform (linux/amd64/v3) and no specific platform was requested
647c1122d7c25f99085496ba3593babe870bbedf860402e3efd377201aa8bfcd

``` 

- [x] 9. Выведите на терминале и проанализируйте в консоли процессы, которые запущены, владельцев по пользователям

```bash 
 $ docker container run -it ubuntu /bin/bash # Запуск интерактивного контейнера на базе образа ubuntu с открытием оболочки /bin/bash

 
 ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker container run -it ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
Digest: sha256:c35e29c9450151419d9448b0fd75374fec4fff364a27f176fb458d472dfc9e54
Status: Downloaded newer image for ubuntu:latest
root@de170528ad2a:/# whoami
root
root@de170528ad2a:/# id
uid=0(root) gid=0(root) groups=0(root)
root@de170528ad2a:/# ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   4588  3712 pts/0    Ss   19:02   0:00 /bin/bash
root        11  0.0  0.0   7888  3968 pts/0    R+   19:03   0:00 ps aux
 
``` 
 
- [x] 10. Выведите оба контейнера first и second на терминал
```
ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05/source$ docker ps -a --filter "name=first|second"
CONTAINER ID   IMAGE                              COMMAND              CREATED          STATUS    PORTS     NAMES
647c1122d7c2   geminishkvdev/hello-appsec-world   "python hello.py"    3 minutes ago    Created             second
8720e74038ee   hellow-appsec-world                "python screen.py"   10 minutes ago   Created             first
```
- [x] 11. Перейдите в основной корень `lab05` и выведите на терминале, и проанализируйте

```bash 
$ docker-compose up --build

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05$ docker-compose up --build
WARN[0000] /home/ris/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] Building 1.4s (25/25) FINISHED                                                           docker:default
 => [server internal] load build definition from Dockerfile                                            0.0s
 => => transferring dockerfile: 419B                                                                   0.0s
 => [client internal] load metadata for docker.io/library/python:3.11-slim                             1.0s
 => [server internal] load .dockerignore                                                               0.0s
 => => transferring context: 2B                                                                        0.0s
 => [client builder 1/4] FROM docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7cca  0.0s
 => => resolve docker.io/library/python:3.11-slim@sha256:1dd3dca85e22886e44fcad1bb7ccab6691dfa83db522  0.0s
 => [server internal] load build context                                                               0.0s
 => => transferring context: 63B                                                                       0.0s
 => CACHED [client builder 2/4] WORKDIR /app                                                           0.0s
 => CACHED [server builder 3/4] COPY requirements.txt .                                                0.0s
 => CACHED [server builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r req  0.0s
 => CACHED [server stage-1 3/6] COPY --from=builder /wheels /wheels                                    0.0s
 => CACHED [server stage-1 4/6] COPY requirements.txt .                                                0.0s
 => CACHED [server stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt    0.0s
 => CACHED [server stage-1 6/6] COPY app.py .                                                          0.0s
 => [server] exporting to image                                                                        0.1s
 => => exporting layers                                                                                0.0s
 => => exporting manifest sha256:a32f6494bcbad769191189f119f6e39e685e717008b0f13d754f945a06c2f8e0      0.0s
 => => exporting config sha256:cd0bd5286e197403130e58cf4daa641142000a843a6ae6fb435571d44fd6bb85        0.0s
 => => exporting attestation manifest sha256:9f48113f7b6c7926a5c51bef01fc716cda5c0d039084051ba99d00d1  0.0s
 => => exporting manifest list sha256:90c05ba08c30779e046828644686eb5438a58ac8f3aa75be08f26a708fef1f3  0.0s
 => => naming to docker.io/library/lab05-server:latest                                                 0.0s
 => => unpacking to docker.io/library/lab05-server:latest                                              0.0s
 => [server] resolving provenance for metadata file                                                    0.0s
 => [client internal] load build definition from Dockerfile                                            0.0s
 => => transferring dockerfile: 425B                                                                   0.0s
 => [client internal] load .dockerignore                                                               0.0s
 => => transferring context: 2B                                                                        0.0s
 => [client internal] load build context                                                               0.0s
 => => transferring context: 66B                                                                       0.0s
 => CACHED [client builder 3/4] COPY requirements.txt .                                                0.0s
 => CACHED [client builder 4/4] RUN pip install --upgrade pip && pip wheel --wheel-dir=/wheels -r req  0.0s
 => CACHED [client stage-1 3/6] COPY --from=builder /wheels /wheels                                    0.0s
 => CACHED [client stage-1 4/6] COPY requirements.txt .                                                0.0s
 => CACHED [client stage-1 5/6] RUN pip install --no-index --find-links=/wheels -r requirements.txt    0.0s
 => CACHED [client stage-1 6/6] COPY client.py .                                                       0.0s
 => [client] exporting to image                                                                        0.0s
 => => exporting layers                                                                                0.0s
 => => exporting manifest sha256:388949ba7d9c82960f7796730b999dd4dc2dab396b20afed061bfd72ae8fdc8a      0.0s
 => => exporting config sha256:c12d6d3bd3e76472a38860e63518951c106fa4fae51e49ac6f150e5fbfb42ed3        0.0s
 => => exporting attestation manifest sha256:7d60c21252bf9cec65b2c1fad6736839351e9adafcbda259cb7ec736  0.0s
 => => exporting manifest list sha256:40c51ebeac166ae4fb6713870546d2c57fbfb1974d4d81f41043c8ca79a7a0b  0.0s
 => => naming to docker.io/library/lab05-client:latest                                                 0.0s
 => => unpacking to docker.io/library/lab05-client:latest                                              0.0s
 => [client] resolving provenance for metadata file                                                    0.0s
[+] Running 2/2
 ✔ Container lab05-client-1  Recreated                                                                 0.3s
 ✔ Container lab05-server-1  Recreated                                                                 0.1s
Attaching to client-1, server-1
server-1  |  * Serving Flask app 'app'
server-1  |  * Debug mode: off
server-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
server-1  |  * Running on all addresses (0.0.0.0)
server-1  |  * Running on http://127.0.0.1:8000
server-1  |  * Running on http://172.19.0.2:8000
server-1  | Press CTRL+C to quit
server-1  | 172.19.0.3 - - [11/Jan/2026 19:07:28] "GET / HTTP/1.1" 200 -
client-1  |
client-1  |     <html>
client-1  |     <head><title>Colorful Output</title></head>
client-1  |     <body style="font-family: monospace; font-size: 24px;">
server-1  | 172.19.0.1 - - [11/Jan/2026 19:09:53] "GET / HTTP/1.1" 200 -
server-1  | 172.19.0.1 - - [11/Jan/2026 19:09:53] "GET /favicon.ico HTTP/1.1" 404 -
client-1  |     <span style="color:red">h</span><span style="color:green">e</span><span style="color:yellow">l</span><span style="color:blue">l</span><span style="color:purple">o</span><span style="color:red"> </span><span style="color:green">a</span><span style="color:yellow">p</span><span style="color:blue">p</span><span style="color:purple">s</span><span style="color:red">e</span><span style="color:green">c</span><span style="color:yellow"> </span><span style="color:blue">w</span><span style="color:purple">o</span><span style="color:red">r</span><span style="color:green">l</span><span style="color:yellow">d</span>
client-1  |     </body>
client-1  |     </html>
client-1  |
client-1 exited with code 0

``` 

- [x] 12. Откройте соседнее окно терминала и и выведите на терминале

```bash 
$ open -a "Google Chrome" http://localhost:8000

ris@DESKTOP-HS8SF48:~$ cmd.exe /C start http://localhost:8000
'\\wsl.localhost\Ubuntu-22.04\home\ris'
CMD.EXE was started with the above path as the current directory.
UNC paths are not supported.  Defaulting to Windows directory.

```

- [x] 13. Остановите работу `docker-compose`.

```bash 
$ docker ps -a # Выводит список всех контейнеров (запущенных и остановленных) с их статусами и параметрами

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05$ docker ps -a
CONTAINER ID   IMAGE                              COMMAND                  CREATED             STATUS                          PORTS      NAMES
bf4e8a982f9a   lab05-client                       "python client.py"       3 minutes ago       Exited (0) About a minute ago              lab05-client-1
1776a4ea5cc9   lab05-server                       "python app.py"          3 minutes ago       Exited (137) 4 seconds ago                 lab05-server-1
de170528ad2a   ubuntu                             "/bin/bash"              8 minutes ago       Exited (127) 6 minutes ago                 tender_keller
647c1122d7c2   geminishkvdev/hello-appsec-world   "python hello.py"        10 minutes ago      Created                                    second
8720e74038ee   hellow-appsec-world                "python screen.py"       16 minutes ago      Created                                    first
333e40786732   hellow-appsec-world                "python screen.py il…"   34 minutes ago      Exited (0) 34 minutes ago                  elated_wing
3cacb12f9272   hellow-appsec-world                "python screen.py il…"   34 minutes ago      Exited (0) 34 minutes ago                  modest_yalow
faadae4b28f9   hellow-appsec-world                "ilia"                   34 minutes ago      Created                                    thirsty_cori
5b7a331a785b   hellow-appsec-world                "python screen.py Il…"   38 minutes ago      Exited (0) 38 minutes ago                  goofy_cohen
d42ada671fb3   hellow-appsec-world                "python screen.py"       38 minutes ago      Exited (2) 38 minutes ago                  objective_proskuriakova
3a533a91628f   8046b069cca9                       "python hello.py"        About an hour ago   Exited (0) About an hour ago               heuristic_hoover
e60327da1371   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   5 hours ago         Up 5 hours                                 openmp_stack_master.1.i0yldjsfif5t6f444da9ht3c4
082434bc3e2d   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   5 hours ago         Up 5 hours                                 openmp_stack_worker.1.k57ttflyoqsdzp82lx6vpduph
6f49029ece63   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   5 hours ago         Up 5 hours                                 openmp_stack_worker.4.phjbdfnrrxkfjjy4bucxp9zqx
340a3cce394d   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   5 hours ago         Up 5 hours                                 openmp_stack_worker.3.8wg439y4d9jlfsyhmq3ftjuu1
f89cb507cb4d   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   5 hours ago         Up 5 hours                                 openmp_stack_worker.2.3lbx8xnkf1yup2cjg4wf29aqi
5b19b38e44f9   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   5 hours ago         Up 5 hours                                 openmp_stack_worker.5.ej3m1gka9x77yuk2l6h5w267w
93f4a7384128   registry:2                         "/entrypoint.sh /etc…"   5 hours ago         Up 5 hours                      5000/tcp   registry.1.veanh8e9o5fgtf4ozdbjoz7z1
1e301691b9d8   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   2 weeks ago         Exited (0) 2 weeks ago                     openmp_stack_master.1.iszv3q1a2nmztetllazbn2ac4
d7a286e13671   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   2 weeks ago         Exited (0) 2 weeks ago                     openmp_stack_worker.2.vabq3e8mbqygu1iwkc9pcix5l
135d231e5b97   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   2 weeks ago         Exited (0) 2 weeks ago                     openmp_stack_worker.1.4hbbgcskyzxb86ze2mgphp68p
72aa3d2aeb71   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   2 weeks ago         Exited (0) 2 weeks ago                     openmp_stack_worker.3.zhad2ci24vjggx2207i9527lv
38b95ffd5900   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   2 weeks ago         Exited (0) 2 weeks ago                     openmp_stack_worker.4.sadakxu5s4eveqlbl2i0c3fyq
1dc1932a10c9   127.0.0.1:5000/mpi:latest          "tcpserver -HRDl0 0.…"   2 weeks ago         Exited (0) 2 weeks ago                     openmp_stack_worker.5.97ucrasmh2jpu0dygecdfva9p
c7a85352bc08   registry:2                         "/entrypoint.sh /etc…"   2 weeks ago         Exited (2) 2 weeks ago                     registry.1.xqy21h3h3owua8o8gyrwnq5gj
dc57dfc4a773   8046b069cca9                       "python hello.py"        2 weeks ago         Exited (0) 2 weeks ago                     objective_jemison

$ docker ps -q # Выводит только идентификаторы (ID) запущенных контейнеров

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05$ docker ps -q
e60327da1371
082434bc3e2d
6f49029ece63
340a3cce394d
f89cb507cb4d
5b19b38e44f9
93f4a7384128

$ docker images # Выводит список локально доступных Docker-образов (репозиторий, тег, ID, размер)

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05$ docker images
REPOSITORY                         TAG       IMAGE ID       CREATED          SIZE
lab05-client                       latest    40c51ebeac16   6 minutes ago    208MB
lab05-server                       latest    90c05ba08c30   6 minutes ago    211MB
hellow-appsec-world                latest    ecb8a49f8890   44 minutes ago   222MB
ris4png/hellow-appsec-world        latest    ecb8a49f8890   44 minutes ago   222MB
127.0.0.1:5000/mpi                 latest    b4ad8482751e   2 weeks ago      1.93GB
geminishkvdev/hello-appsec-world   latest    f9db3113962a   7 weeks ago      228MB
ubuntu                             latest    c35e29c94501   2 months ago     117MB
registry                           2         a3d8aaa63ed8   2 years ago      37.2MB

$ docker ps -q | xargs docker stop # Останавливает все запущенные контейнеры, передавая их ID из docker ps -q в команду docker stop

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05$ docker ps -q | xargs docker stop
9243549a34c8
b4a9975292aa
a3deebcc2f99
738100f31270
5bdb37e809c1
48bd98daf529
9a7a938fdd43
8ba420767545
b499759641f8

$ docker-compose down  # Останавливает и удаляет ресурсы docker-compose проекта

ris@DESKTOP-HS8SF48:~/course_labs/labs/lab05$ docker-compose down
WARN[0000] /home/ris/course_labs/labs/lab05/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion
[+] Running 3/3
 ✔ Container lab05-client-1  Removed                                                                  10.2s
 ✔ Container lab05-server-1  Removed                                                                  10.2s
 ✔ Network lab05_app_net     Removed  

```

- [x] 14. Доработайте `docker-compose` и скрипт, который вы подготовили ранее, что бы вы смогли воспроизвести шаги п.11 по п.13 с демонстрацией. Сделайте `commit`.
- [x] 15. Залейте изменения в свой удаленный репозиторий, проверьте историю `commit`.
- [x] 16. Подготовьте отчет `gist`.
 
***

## Links

- [Docker](https://docs.docker.com/)
- [Markdown](https://stackedit.io)
- [Gist](https://gist.github.com)
- [GitHub CLI](https://cli.github.com)
