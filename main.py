# main.py
import asyncio
import os
import sys
import uuid
import inquirer
from loguru import logger

# Import functions from other files
from _includes.banner import display_banner
from _includes.logging import setup_logging, log_status
from _includes.proxies_manager import update_file, load_proxies, get_proxy_ip, get_proxy_name
from _includes.accounts_manager import load_accounts, select_account
from _includes.core import connect_to_wss


async def main():
    removed_proxies = [0]
    stats = {'pings': 0, 'pongs': 0}

    display_banner()
    setup_logging()

    accounts = load_accounts()
    if not accounts:
        return

    selected_user_name, _user_id = select_account(accounts)
    if _user_id is None:
        return

    display_banner()
    local_proxies, selected_file_display = load_proxies()
    if not local_proxies:
        return

    display_banner()

    status_task = asyncio.create_task(log_status(stats, removed_proxies))

    device_ids = [str(uuid.uuid3(uuid.NAMESPACE_DNS, proxy.encode())) for proxy in local_proxies]
    tasks = [asyncio.ensure_future(connect_to_wss(proxy, device_id, _user_id, stats, removed_proxies)) for proxy, device_id in
             zip(local_proxies, device_ids)]

    device_count = len(local_proxies)

    logger.info(f"{selected_user_name} is selected with UID {_user_id}")
    logger.info(f"{device_count} devices will be generated using proxies")
    logger.info(f"Loading ...")

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        display_banner()
        logger.info("Script interrupted by user. Cleaning up...\n")