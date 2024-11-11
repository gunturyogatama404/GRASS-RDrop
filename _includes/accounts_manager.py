# _includes/accounts.py
import inquirer
from loguru import logger

def load_accounts():
    account_file = 'accounts.txt'
    try:
        with open(account_file, 'r') as f:
            accounts = [line.strip().split(",") for line in f if line.strip()]
            return accounts
    except FileNotFoundError:
        logger.error(f"Account file '{account_file}' not found. Please create the file with account entries.")
        return None

def sort_accounts(accounts):
    # Menyortir berdasarkan nomor ID atau nama akun
    return sorted(accounts, key=lambda x: x[0])  # Asumsi: x[0] adalah _user_id

def select_account(accounts):
    if not accounts:
        logger.error("No accounts found in accounts.txt.")
        return None, None

    # Menyortir akun sebelum ditampilkan
    sorted_accounts = sort_accounts(accounts)

    # Menampilkan daftar akun dengan nomor
    print("\nAvailable Accounts:")
    for idx, (user_id, user_name) in enumerate(sorted_accounts, start=1):
        print(f"{idx}. {user_name} (ID: {user_id})")

    # Meminta input nomor akun
    try:
        selected_number = int(input("\nSelect an account by number: "))
        if selected_number < 1 or selected_number > len(sorted_accounts):
            raise ValueError("Invalid selection.")

        selected_user_name, _user_id = sorted_accounts[selected_number - 1]
        return selected_user_name, _user_id

    except ValueError as e:
        logger.error(f"Invalid input: {e}. Please enter a valid number.\n")
        return None, None
