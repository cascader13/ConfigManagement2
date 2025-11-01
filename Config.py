# config.py
import configparser
import json
import os
import sys
import urllib.request
from typing import Dict, Any


class Config:
    def __init__(self, config_file: str = "config.ini"):
        self.config_file = config_file
        self.default_config = {
            'package': {
                'name': 'requests',
                'version': '0.1.0',
                'repository_url': 'https://pypi.org/pypi',
                'test_mode': 'false',
                'test_repository_path': 'test_repo.txt',
                'output_image': 'dependency_graph.png'
            }
        }
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        config = configparser.ConfigParser()
        if not os.path.exists(self.config_file):
            self.create_default_config(config)
        try:
            config.read(self.config_file)
            self.validate_config(config)
            return {
                'package_name': config.get('package', 'name', fallback=self.default_config['package']['name']),
                'version': config.get('package', 'version', fallback=self.default_config['package']['version']),
                'repository_url': config.get('package', 'repository_url',
                                             fallback=self.default_config['package']['repository_url']),
                'test_mode': config.getboolean('package', 'test_mode', fallback=False),
                'test_repository_path': config.get('package', 'test_repository_path',
                                                   fallback=self.default_config['package']['test_repository_path']),
                'output_image': config.get('package', 'output_image',
                                           fallback=self.default_config['package']['output_image'])
            }

        except configparser.Error as e:
            print(f"Ошибка чтения конфигурационного файла: {e}")
            sys.exit(1)

    def create_default_config(self, config: configparser.ConfigParser):
        config.read_dict(self.default_config)
        with open(self.config_file, 'w') as f:
            config.write(f)
        print(f"Создан конфигурационный файл {self.config_file} с настройками по умолчанию")

    def validate_config(self, config: configparser.ConfigParser):
        if not config.has_section('package'):
            raise ValueError("Отсутствует секция [package] в конфигурационном файле")

        package_name = config.get('package', 'name', fallback='')
        if not package_name:
            raise ValueError("Имя пакета не может быть пустым")

        test_mode = config.getboolean('package', 'test_mode', fallback=False)
        if test_mode:
            test_path = config.get('package', 'test_repository_path', fallback='')
            if not test_path:
                raise ValueError("В тестовом режиме должен быть указан путь к тестовому репозиторию")

    def load_package_info(self, name, version: str = ''):
        if not version:
            url = f"{self.config['repository_url']}/{name}/json"
        else:
            url = f"{self.config['repository_url']}/{name}/{version}/json"

        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode('utf-8'))
            return data
        except Exception as e:
            print(f"Ошибка при получении {name}: {e}")

    def get_dependencies(self):
        package_name = self.config['package_name']
        package_version = self.config['version']
        package_info = self.load_package_info(package_name, package_version)
        print(package_info['info']['requires_dist'])



    def display_config(self):
        for key, value in self.config.items():
            print(f"{key}: {value}")



if __name__ == "__main__":
    config = Config()
    print(config.config)
    config.get_dependencies()
