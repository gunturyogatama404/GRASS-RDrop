# main.py
import asyncio
import os
import sys
import uuid
import inquirer
import time
from loguru import logger

# Includes
from _includes.banner import display_banner
from _includes.logging import setup_logging, log_status
from _includes.proxies_manager import update_file, load_proxies, get_proxy_ip, get_proxy_name
from _includes.accounts_manager import load_accounts, select_account
from _includes.core import connect_to_wss
from _includes.errors_handler import handle_generic_error

setup_logging()

async def main():
    start_time = time.time()
    restart_interval = 1200
    removed_proxies = 0
    stats = {'pings': 0, 'pongs': 0}
    retry_counts = {}

    display_banner()
    accounts = load_accounts()
    if not accounts:
        return

    selected_user_name, user_id = select_account(accounts)
    if user_id is None:
        return

    display_banner()
    local_proxies, selected_file_display = load_proxies()
    if not local_proxies:
        return

    while True:
        display_banner()

        status_task = asyncio.create_task(log_status(stats, removed_proxies))

        device_ids = [str(uuid.uuid3(uuid.NAMESPACE_DNS, proxy.encode())) for proxy in local_proxies]
        tasks = [connect_to_wss(proxy, device_id, user_id, stats, removed_proxies, retry_counts)
                 for proxy, device_id in zip(local_proxies, device_ids)]

        device_count = len(local_proxies)

        logger.info(f"{selected_user_name} selected (UID: {user_id})")
        logger.info(f"Generating {device_count} devices using proxies")
        logger.info("Loading...")

        try:
            await asyncio.wait_for(asyncio.gather(*tasks), timeout=restart_interval)
        except asyncio.TimeoutError:
            logger.info("20 minutes elapsed. Restarting...")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        finally:
            status_task.cancel()

        elapsed_time = time.time() - start_time
        if elapsed_time >= restart_interval:
            logger.info("20 minutes elapsed. Restarting...")
            start_time = time.time()
            await asyncio.sleep(5)
            continue
        else:
            break

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        display_banner()
        logger.info("Script interrupted by user. Cleaning up...\n")