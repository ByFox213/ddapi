sum_to_encoding = {"␣": "%20", "!": "%21", "\"": "%22", "#": "%23",
                   "$": "%24", "%": "%25", "&": "%26", "\'": "%27",
                   "(": "%28", ")": "%29", "*": "%2A", "+": "%2B",
                   ",": "%2C", "/": "%2F", ":": "%3A", ";": "%3B",
                   "=": "%3D", "?": "%3F", "@": "%40", "[": "%5B",
                   "]": "%5D", "-": "%2D", ".": "%2E", "<": "%3C",
                   ">": "%3E", "\\": "%5C", "^": "%5E", "_": "%5F",
                   "`": "%60", "{": "%7B", "|": "%7C", "}": "%7D",
                   "~": "%7E"}


def username_encode(username: str) -> str:
    """Decodes the line so that http gives out information about the player.
    :param username:
        :type: str
    :return:
        :type: str
    """
    result: str = ""
    for i in username:
        add: str = sum_to_encoding.get(i)
        if add is not None:
            result += add
        else:
            result += i
    return result
