import os

def get_full_path_to_virtual_env():
    return os.environ.get('VIRTUAL_ENV', 'No active virtual environment')

if __name__ == "__main__":
    full_path = get_full_path_to_virtual_env()
    if full_path != 'No active virtual environment':
        print(f"Your current virtual env is {full_path}")
    else:
        print("No active virtual environment")