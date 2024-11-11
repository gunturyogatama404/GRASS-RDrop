## GRASS RDrop v0.2 - Grass Bot

based on https://github.com/ylasgamers/getgrass/

**Features:**
* Accounts selector
* Proxy selector
* Proxy support (SOCKS4, SOCKS5, HTTP)
* Proxy rotation (with retry attempts and error handling)
* Status logging
* Error handling and reporting

**Prerequisites:**
* an account, register here [https://app.getgrass.io/register/?referralCode=zUQ3Gcre5EvVp5a](https://app.getgrass.io/register/?referralCode=XQJPaWPVbfvRfq5)
* Python 3.2 or higher
* `pip` package manager
* `websockets`
* `websockets-proxy`
* `fake-useragent`
* `python-socks`
* `inquirer`
* `loguru`
* `colorama`

**Installation:**

0. Install softwares:

   windows
      ```bash
      winget install Microsoft.Git Python.Python.3.12 --accept-source-agreements --accept-package-agreements
      ```
   linux
      ```bash
      sudo apt update && sudo apt upgrade -y && sudo apt install python3 nano git -y
      ```

1. Clone the repository:
   ```bash
   git clone https://github.com/dualkeyboards/GRASS-RDrop.git
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

**Usage:**
1. **Accounts File:**
   - Create a file named `accounts.txt` in the project directory.
   - Format each line as `user_id,user_name`.
   - Example:
     ```
     1234567890,JohnDoe
     9876543210,JaneSmith
     ```

2. **Proxy Files:**
   - Create one or more proxy files with the prefix `proxies_` and a `.txt` extension.
   - Each proxy should be on a separate line in the format `protocol://address:port`.
   - Example:
     ```
     socks5://127.0.0.1:9050
     http://192.168.1.100:8080
     ```

3. **Run the script:**
   ```bash
   python main.py
   ```

4. **Select an account and proxy file:**
   - The script will present a menu to choose from your available accounts and proxy files.

5. **Start the bot:**
   - The script will start creating and connecting devices using the selected proxies.

6. **Monitor the log:**
   - The script will log real-time information about the bot's activity, including connection statuses, ping/pong messages, and errors.

**Configuration:**
- **`restart_interval`:** Specifies the interval (in seconds) for restarting the bot (default is 1200 seconds - 20 minutes). 
- **`retry_counts`:** Defines the number of retry attempts for proxies that encounter errors before they are removed from the pool (default is 5). 

You can modify these settings in the `main.py` file.

**Notes:**
* Make sure your proxies are working and configured correctly.
* You may need to adjust the `restart_interval` and `retry_counts` values based on your network and proxy configuration.
* The script will automatically update the proxy files with information about which proxies are working, which are encountering errors, and which have been pinged or ponged successfully. This will allow you to identify and remove inactive or problematic proxies.

**Disclaimer:**

This script is provided as-is without warranty of any kind. The author is not responsible for any damage or misuse of this script. Use at your own risk.
