def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    ls1  =  len ( s1 )
    ls2  =  len ( s2 )
    ls3  =  len ( s3 )

    if ls1 % 2 > 0 and ls2 % 2 > 0 and ls3 % 2 > 0:
        return f"[{s1}, {s2}, {s3}]"

    if ls1 % 2 > 0 and ls2 % 2 > 0 and ls3 % 2 <= 0:
        return f"[{s1}, {s2}]"

    if ls1 % 2 > 0 and ls2 % 2 <= 0 and ls3 % 2 <= 0:
        return f"[{s1}]"

    if ls1 % 2 <= 0 and ls2 % 2 > 0 and ls3 % 2 <= 0:
        return f"[{s2}]"

    if ls1 % 2 <= 0 and ls2 % 2 <= 0 and ls3 % 2 > 0:
        return f"[{s3}]"

    if ls1 % 2 > 0 and ls2 % 2 <= 0 and ls3 % 2 > 0:
        return f"[{s1}, {s3}]"

    if ls1 % 2 <= 0 and ls2 % 2 > 0 and ls3 % 2 > 0:
        return f"[{s2}, {s3}]"