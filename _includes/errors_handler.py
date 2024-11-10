# _includes/errors_handler.py
from loguru import logger
from _includes.proxies_manager import update_file, get_proxy_name
from _includes.core import get_proxy_name

async def handle_generic_error(proxy_url, removed_proxies, e):
    proxy_ip = get_proxy_name(proxy_url)
    error_messages = {
        "Invalid proxy response": f"Invalid proxy response - {proxy_ip}",
        "Connection closed unexpectedly": f"Connection closed unexpectedly - {proxy_ip}",
        "Request rejected or failed": f"Request rejected or failed - {proxy_ip}",
        "Server rejected WebSocket connection: HTTP 404": f"Request rejected by server - {proxy_ip}",
        "server rejected WebSocket connection: HTTP 404": f"Request rejected by server - {proxy_ip}",  # Duplicate but lowercase start
        "[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1000)": f"SSL wrong version number - {proxy_ip}",
        "407 Proxy Authentication Required": f"Authentication required - {proxy_ip}",
        "502 Bad Gateway": f"Bad gateway - {proxy_ip}",
        "503 Service Unavailable": f"Service unavailable - {proxy_ip}",
        "503 Too many open connections": f"Too many open connections - {proxy_ip}",
        "[WinError 64] The specified network name is no longer available": f"Network name unavailable - {proxy_ip}",
        "[WinError 121]": f"Semaphore timeout expired - {proxy_ip}",
        "[WinError 10054] An existing connection was forcibly closed by the remote host": f"Connection forcibly closed - {proxy_ip}",
    }

    for error_string, log_message in error_messages.items():
        if error_string in str(e):
            logger.error(log_message)
            update_file("proxies_error.txt", proxy_url)
            logger.warning(f"Removing proxy: {proxy_ip}")
            removed_proxies[0] += 1
            return  # Exit after handling the specific error

    logger.error(f"Unexpected error - {proxy_ip}: {e}")  # Handle unexpected errors