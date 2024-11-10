# _includes/errors_handler.py
from loguru import logger
from _includes.proxies_manager import update_file, get_proxy_name

async def handle_generic_error(proxy_url, removed_proxies, retry_counts, e):  # Add retry_counts
    proxy_ip = get_proxy_name(proxy_url)
    error_messages = {
        "Connection closed unexpectedly": f"Connection closed unexpectedly - {proxy_ip}",
        "Empty connect reply": f"Empty connect reply - {proxy_ip}",
        "General SOCKS server failure": f"General SOCKS server failure - {proxy_ip}",
        "Invalid proxy response": f"Invalid proxy response - {proxy_ip}",
        "Proxy connection timed out": f"Proxy connection timed out - {proxy_ip}",
        "Request rejected or failed": f"Request rejected or failed - {proxy_ip}",
        "Server rejected WebSocket connection: HTTP 404": f"Request rejected by server - {proxy_ip}",
        "server rejected WebSocket connection: HTTP 404": f"Request rejected by server - {proxy_ip}",  # Duplicate but lowercase start
        "TTL expired": f"TTL Expired - {proxy_ip}",
        "[SSL: WRONG_VERSION_NUMBER] wrong version number (_ssl.c:1000)": f"SSL wrong version number - {proxy_ip}",
        "403 Forbidden": f"Forbidden - {proxy_ip}",
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
            retry_counts[proxy_url] = retry_counts.get(proxy_url, 0) + 1  # Increment retry count
            update_file("proxies_error.txt", proxy_url)

            if retry_counts[proxy_url] >= 5: #Check retry count
                logger.warning(f"Removing proxy {proxy_ip} after 5 retries.")
                removed_proxies[0] += 1
                # Optionally remove the proxy from your list here if you're maintaining one
            else:
                logger.warning(f"Retrying proxy {proxy_ip}, attempt {retry_counts[proxy_url]} / 5 ")
            return  # Exit after handling

    logger.error(f"Unexpected error - {proxy_ip}: {e}")  # Handle unexpected errors