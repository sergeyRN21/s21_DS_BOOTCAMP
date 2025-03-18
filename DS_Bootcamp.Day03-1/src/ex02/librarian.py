import os
import subprocess

def install_lib():
    if 'VIRTUAL_ENV' not in os.environ:
        raise RuntimeError("Не найдено актуальное виртуальное окружение.")
    libraries = ['beautifulsoup4', 'pytest']
    result = subprocess.run(['pip', 'install']+ libraries, capture_output=True, text=True)
    return result

def list_installed_lib():
    result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
    return result.stdout

def create_txt_file():
    with open("requirements.txt", 'w') as file:
        file.write(list_installed_lib())

if __name__ == '__main__':
    try:
        output = install_lib()
        print(output)
        installed_lib_list = list_installed_lib()
        print(installed_lib_list)
        create_txt_file()
    except RuntimeError as e:
        print(e)