def gen_short(num):
    url_len = 5
    alphabet_cap = 26
    code_arr = []
    for i in range(url_len):
        code_arr.append(num % alphabet_cap)
        num = num // alphabet_cap
    chr_arr = [chr(code_arr[i] + 65) for i in range(url_len)]
    short_url = "".join(chr_arr)
    return short_url
