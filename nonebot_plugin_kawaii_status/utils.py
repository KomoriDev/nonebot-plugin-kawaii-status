def truncate_string(string: str, length: int = 32):
    """
    将字符串截断为给定长度。

    参数：
        string (str)：要截断的字符串。
        length (int)：截断字符串的最大长度。

    返回：
        str：截断的字符串。
    """
    if len(string) > length:
        return string[: length - 3] + "..."
    else:
        return string
