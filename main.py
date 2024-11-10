import os
import sys

_includes_dir = os.path.join(os.path.dirname(__file__), '_includes')
sys.path.append(_includes_dir)

from banner import print_banner

print_banner()