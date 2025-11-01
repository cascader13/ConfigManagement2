# Задание 2
## 16 вариант

### Этап 1. Минимальный прототип с конфигурацией

Цель: создать минимальное CLI-приложение и сделать его настраиваемым.
Требования:

1. Источником настраиваемых пользователем параметров является
конфигурационный файл формата INI.
2. К настраиваемым параметрам относятся:
– Имя анализируемого пакета.
– URL-адрес репозитория или путь к файлу тестового репозитория.
– Режим работы с тестовым репозиторием.
– Имя сгенерированного файла с изображением графа.
3. (только для этого этапа) При запуске приложения вывести все параметры,
настраиваемые пользователем, в формате ключ-значение.
4. Реализовать и продемонстрировать обработку ошибок для всех параметров.
5. Результат выполнения этапа сохранить в репозиторий стандартно
оформленным коммитом.

## Тестирование:

### Конфигурационного файла не существует(создаётся дефолтный)

```bash
Создан конфигурационный файл config.ini с настройками по умолчанию
package_name: requests
repository_url: https://pypi.org/pypi
test_mode: False
test_repository_path: test_repo.txt
output_image: dependency_graph.png
```

### Конфигурационный файл существует
```bash
package_name: pandas
repository_url: https://pypi.org/pypi
test_mode: True
test_repository_path: test_repo.txt
output_image: dependency_graph.png```
```
### Конфигурационный файл невозможно прочитать
```bash
Ошибка чтения конфигурационного файла: File contains no section headers.
file: 'config.ini', line: 2
'name = pandas\n'```
```
### Этап 2. Сбор данных
Цель: реализовать основную логику получения данных о зависимостях для их
дальнейшего анализа и визуализации. Запрещено пользоваться менеджерами
пакетов и сторонними библиотеками для получения информации о зависимостях
пакетов.
Требования:
1. Использовать формат пакетов Python (pip).
2. Извлечь информацию о прямых зависимостях заданного пользователем
пакета, используя URL-адрес репозитория.
3. (только для этого этапа) Вывести на экран все прямые зависимости
заданного пользователем пакета.
4. Результат выполнения этапа сохранить в репозиторий стандартно
оформленным коммитом.

## Тестирование:

### Пакет без указания версии
```bash
{'package_name': 'pandas', 'version': '', 'repository_url': 'https://pypi.org/pypi', 'test_mode': True, 'test_repository_path': 'test_repo.txt', 'output_image': 'dependency_graph.png'}
['numpy>=1.22.4; python_version < "3.11"', 'numpy>=1.23.2; python_version == "3.11"', 'numpy>=1.26.0; python_version >= "3.12"', 'python-dateutil>=2.8.2', 'pytz>=2020.1', 'tzdata>=2022.7', 'hypothesis>=6.46.1; extra == "test"', 'pytest>=7.3.2; extra == "test"', 'pytest-xdist>=2.2.0; extra == "test"', 'pyarrow>=10.0.1; extra == "pyarrow"', 'bottleneck>=1.3.6; extra == "performance"', 'numba>=0.56.4; extra == "performance"', 'numexpr>=2.8.4; extra == "performance"', 'scipy>=1.10.0; extra == "computation"', 'xarray>=2022.12.0; extra == "computation"', 'fsspec>=2022.11.0; extra == "fss"', 's3fs>=2022.11.0; extra == "aws"', 'gcsfs>=2022.11.0; extra == "gcp"', 'pandas-gbq>=0.19.0; extra == "gcp"', 'odfpy>=1.4.1; extra == "excel"', 'openpyxl>=3.1.0; extra == "excel"', 'python-calamine>=0.1.7; extra == "excel"', 'pyxlsb>=1.0.10; extra == "excel"', 'xlrd>=2.0.1; extra == "excel"', 'xlsxwriter>=3.0.5; extra == "excel"', 'pyarrow>=10.0.1; extra == "parquet"', 'pyarrow>=10.0.1; extra == "feather"', 'tables>=3.8.0; extra == "hdf5"', 'pyreadstat>=1.2.0; extra == "spss"', 'SQLAlchemy>=2.0.0; extra == "postgresql"', 'psycopg2>=2.9.6; extra == "postgresql"', 'adbc-driver-postgresql>=0.8.0; extra == "postgresql"', 'SQLAlchemy>=2.0.0; extra == "mysql"', 'pymysql>=1.0.2; extra == "mysql"', 'SQLAlchemy>=2.0.0; extra == "sql-other"', 'adbc-driver-postgresql>=0.8.0; extra == "sql-other"', 'adbc-driver-sqlite>=0.8.0; extra == "sql-other"', 'beautifulsoup4>=4.11.2; extra == "html"', 'html5lib>=1.1; extra == "html"', 'lxml>=4.9.2; extra == "html"', 'lxml>=4.9.2; extra == "xml"', 'matplotlib>=3.6.3; extra == "plot"', 'jinja2>=3.1.2; extra == "output-formatting"', 'tabulate>=0.9.0; extra == "output-formatting"', 'PyQt5>=5.15.9; extra == "clipboard"', 'qtpy>=2.3.0; extra == "clipboard"', 'zstandard>=0.19.0; extra == "compression"', 'dataframe-api-compat>=0.1.7; extra == "consortium-standard"', 'adbc-driver-postgresql>=0.8.0; extra == "all"', 'adbc-driver-sqlite>=0.8.0; extra == "all"', 'beautifulsoup4>=4.11.2; extra == "all"', 'bottleneck>=1.3.6; extra == "all"', 'dataframe-api-compat>=0.1.7; extra == "all"', 'fastparquet>=2022.12.0; extra == "all"', 'fsspec>=2022.11.0; extra == "all"', 'gcsfs>=2022.11.0; extra == "all"', 'html5lib>=1.1; extra == "all"', 'hypothesis>=6.46.1; extra == "all"', 'jinja2>=3.1.2; extra == "all"', 'lxml>=4.9.2; extra == "all"', 'matplotlib>=3.6.3; extra == "all"', 'numba>=0.56.4; extra == "all"', 'numexpr>=2.8.4; extra == "all"', 'odfpy>=1.4.1; extra == "all"', 'openpyxl>=3.1.0; extra == "all"', 'pandas-gbq>=0.19.0; extra == "all"', 'psycopg2>=2.9.6; extra == "all"', 'pyarrow>=10.0.1; extra == "all"', 'pymysql>=1.0.2; extra == "all"', 'PyQt5>=5.15.9; extra == "all"', 'pyreadstat>=1.2.0; extra == "all"', 'pytest>=7.3.2; extra == "all"', 'pytest-xdist>=2.2.0; extra == "all"', 'python-calamine>=0.1.7; extra == "all"', 'pyxlsb>=1.0.10; extra == "all"', 'qtpy>=2.3.0; extra == "all"', 'scipy>=1.10.0; extra == "all"', 's3fs>=2022.11.0; extra == "all"', 'SQLAlchemy>=2.0.0; extra == "all"', 'tables>=3.8.0; extra == "all"', 'tabulate>=0.9.0; extra == "all"', 'xarray>=2022.12.0; extra == "all"', 'xlrd>=2.0.1; extra == "all"', 'xlsxwriter>=3.0.5; extra == "all"', 'zstandard>=0.19.0; extra == "all"']

Process finished with exit code 0

```

### Пакет с указанием версии

```bash
{'package_name': 'pandas', 'version': '2.3.3', 'repository_url': 'https://pypi.org/pypi', 'test_mode': True, 'test_repository_path': 'test_repo.txt', 'output_image': 'dependency_graph.png'}
['numpy>=1.22.4; python_version < "3.11"', 'numpy>=1.23.2; python_version == "3.11"', 'numpy>=1.26.0; python_version >= "3.12"', 'python-dateutil>=2.8.2', 'pytz>=2020.1', 'tzdata>=2022.7', 'hypothesis>=6.46.1; extra == "test"', 'pytest>=7.3.2; extra == "test"', 'pytest-xdist>=2.2.0; extra == "test"', 'pyarrow>=10.0.1; extra == "pyarrow"', 'bottleneck>=1.3.6; extra == "performance"', 'numba>=0.56.4; extra == "performance"', 'numexpr>=2.8.4; extra == "performance"', 'scipy>=1.10.0; extra == "computation"', 'xarray>=2022.12.0; extra == "computation"', 'fsspec>=2022.11.0; extra == "fss"', 's3fs>=2022.11.0; extra == "aws"', 'gcsfs>=2022.11.0; extra == "gcp"', 'pandas-gbq>=0.19.0; extra == "gcp"', 'odfpy>=1.4.1; extra == "excel"', 'openpyxl>=3.1.0; extra == "excel"', 'python-calamine>=0.1.7; extra == "excel"', 'pyxlsb>=1.0.10; extra == "excel"', 'xlrd>=2.0.1; extra == "excel"', 'xlsxwriter>=3.0.5; extra == "excel"', 'pyarrow>=10.0.1; extra == "parquet"', 'pyarrow>=10.0.1; extra == "feather"', 'tables>=3.8.0; extra == "hdf5"', 'pyreadstat>=1.2.0; extra == "spss"', 'SQLAlchemy>=2.0.0; extra == "postgresql"', 'psycopg2>=2.9.6; extra == "postgresql"', 'adbc-driver-postgresql>=0.8.0; extra == "postgresql"', 'SQLAlchemy>=2.0.0; extra == "mysql"', 'pymysql>=1.0.2; extra == "mysql"', 'SQLAlchemy>=2.0.0; extra == "sql-other"', 'adbc-driver-postgresql>=0.8.0; extra == "sql-other"', 'adbc-driver-sqlite>=0.8.0; extra == "sql-other"', 'beautifulsoup4>=4.11.2; extra == "html"', 'html5lib>=1.1; extra == "html"', 'lxml>=4.9.2; extra == "html"', 'lxml>=4.9.2; extra == "xml"', 'matplotlib>=3.6.3; extra == "plot"', 'jinja2>=3.1.2; extra == "output-formatting"', 'tabulate>=0.9.0; extra == "output-formatting"', 'PyQt5>=5.15.9; extra == "clipboard"', 'qtpy>=2.3.0; extra == "clipboard"', 'zstandard>=0.19.0; extra == "compression"', 'dataframe-api-compat>=0.1.7; extra == "consortium-standard"', 'adbc-driver-postgresql>=0.8.0; extra == "all"', 'adbc-driver-sqlite>=0.8.0; extra == "all"', 'beautifulsoup4>=4.11.2; extra == "all"', 'bottleneck>=1.3.6; extra == "all"', 'dataframe-api-compat>=0.1.7; extra == "all"', 'fastparquet>=2022.12.0; extra == "all"', 'fsspec>=2022.11.0; extra == "all"', 'gcsfs>=2022.11.0; extra == "all"', 'html5lib>=1.1; extra == "all"', 'hypothesis>=6.46.1; extra == "all"', 'jinja2>=3.1.2; extra == "all"', 'lxml>=4.9.2; extra == "all"', 'matplotlib>=3.6.3; extra == "all"', 'numba>=0.56.4; extra == "all"', 'numexpr>=2.8.4; extra == "all"', 'odfpy>=1.4.1; extra == "all"', 'openpyxl>=3.1.0; extra == "all"', 'pandas-gbq>=0.19.0; extra == "all"', 'psycopg2>=2.9.6; extra == "all"', 'pyarrow>=10.0.1; extra == "all"', 'pymysql>=1.0.2; extra == "all"', 'PyQt5>=5.15.9; extra == "all"', 'pyreadstat>=1.2.0; extra == "all"', 'pytest>=7.3.2; extra == "all"', 'pytest-xdist>=2.2.0; extra == "all"', 'python-calamine>=0.1.7; extra == "all"', 'pyxlsb>=1.0.10; extra == "all"', 'qtpy>=2.3.0; extra == "all"', 'scipy>=1.10.0; extra == "all"', 's3fs>=2022.11.0; extra == "all"', 'SQLAlchemy>=2.0.0; extra == "all"', 'tables>=3.8.0; extra == "all"', 'tabulate>=0.9.0; extra == "all"', 'xarray>=2022.12.0; extra == "all"', 'xlrd>=2.0.1; extra == "all"', 'xlsxwriter>=3.0.5; extra == "all"', 'zstandard>=0.19.0; extra == "all"']

```

### Пакет с неверным именем
```bash
{'package_name': 'psandas', 'version': '2.3.3', 'repository_url': 'https://pypi.org/pypi', 'test_mode': True, 'test_repository_path': 'test_repo.txt', 'output_image': 'dependency_graph.png'}
Ошибка при получении psandas: HTTP Error 404: Not Found
```
