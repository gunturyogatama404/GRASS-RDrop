# _includes/file_handling.py
import os
import inquirer
from loguru import logger

def get_proxy_ip(proxy_url):
    return proxy_url.split("://")[1].split(":")[0]

def get_proxy_name(proxy_url):
    proxy_ip = get_proxy_ip(proxy_url)
    return proxy_ip[:15]

def update_file(file_path, content, action="add"):
    if action == "add":
        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                pass
        with open(file_path, 'r+') as file:
            lines = file.read().splitlines()
            if content not in lines:
                file.write(content + "\n")
    elif action == "remove":
        with open(file_path, 'r') as file:
            lines = file.readlines()
        with open(file_path, 'w') as file:
            for line in lines:
                if line.strip() != content:
                    file.write(line)

def load_proxies():
    proxy_files = [f for f in os.listdir() if f.startswith('proxies') and f.endswith('.txt')]

    if not proxy_files:
        logger.error("No proxy files with prefix 'proxies' found.")
        return None, None

    # Menyortir proxy files berdasarkan nama file
    sorted_proxy_files = sorted(proxy_files)

    # Menampilkan daftar file dengan nomor
    print("\nAvailable Proxy Files:")
    for idx, file_name in enumerate(sorted_proxy_files, start=1):
        print(f"{idx}. {file_name}")

    # Meminta input nomor file
    try:
        selected_number = int(input("\nSelect a proxy file by number: "))
        if selected_number < 1 or selected_number > len(sorted_proxy_files):
            raise ValueError("Invalid selection.")

        selected_file = sorted_proxy_files[selected_number - 1]
        if selected_file == "Add All":
            local_proxies = []
            for file_name in sorted_proxy_files:
                with open(file_name, 'r') as file:
                    local_proxies.extend(file.read().splitlines())
            selected_file_display = "All proxy files"
        else:
            with open(selected_file, 'r') as file:
                local_proxies = file.read().splitlines()
            selected_file_display = selected_file

        return local_proxies, selected_file_display

    except ValueError as e:
        logger.error(f"Invalid input: {e}. Please enter a valid number.\n")
        return None, None
