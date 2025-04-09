import base64


def base64_encode(string: str) -> str:
    """
    返回字符串的base64编码内容
    """
    str_bytes = string.encode("ascii")
    str_bytes = base64.b64encode(str_bytes)
    str_bytes = str_bytes.decode("ascii")
    return str_bytes
