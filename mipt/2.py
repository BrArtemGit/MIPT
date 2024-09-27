def replace(text: str, origin_str: str, new_str: str, limit: int) -> [str, None]:
    """выполняет замену в строке text подстрок origin_str на подстроку new_str столько раз, сколько указано в limit"""
    a = text.split(origin_str)
    res = []
    cnt = 0

    if limit <= text.count(origin_str) and origin_str != "" and text != "":
        for i in range(len(a) - 1):
            if cnt < limit:
                res.append(a[i])
                res.append(new_str)
            else:
                res.append(a[i])
                res.append(origin_str)
            cnt += 1

        if len(a) % 2 == 1:
            res.append(a[-1])

        return "".join(res)
    else:
        return None


if __name__ == "__main__":
    print(replace.__doc__)

    assert replace("ddss assss dddss s sdds ssrs", "ss", "A", 3) == "ddA aAA dddss s sdds ss", "1"
    assert replace("", "g", "s", 8) is None, "2"
    assert replace("1232123454321", "1", "Q", 3) == "Q232Q2345432Q", "3"
    assert replace("n4Q5o87Q34vbQ3e24Q4", "Q", "g", 3) == "n4g5o87g34vbg3e24Q4", "4"
    assert replace("1234567890", "1234567890", "0987654321", 2) is None, "5"
    assert replace("1234567890", "1234567890", "0987654321", 1) == "0987654321", "6"

    print("tests passed")

