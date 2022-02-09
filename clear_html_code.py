def clear_1(src):
    is_open = '<'
    is_close = '>'
    is_content = False
    result = ''
    for i in src:
        if i == is_open:
            is_content = False
            result += ' '
            continue
        if i == is_close:
            is_content = True
            continue
        if is_content:
            result += i
    while result.count('  ') > 0:
        result = result.replace('  ', ' ')
    return result.strip()



def clear_2(src):
    is_open = '<'
    is_close = '>'
    result = ''
    num_close = src.find(is_close)
    num_open = src.find(is_open, num_close)
    while num_open != -1:
        if num_open - num_close == 1:
            num_close = src.find(is_close, num_open)
            num_open = src.find(is_open, num_close)
            result += ' '
            continue
        result += src[num_close + 1:num_open]
        num_close = src.find(is_close, num_open)
        num_open = src.find(is_open, num_close)
    while result.count('  ') > 0:
        result = result.replace('  ', ' ')
    return result.strip()

s = '<div class="main"><h1>Header</h1><div class="txt"><p class="ppp">Lorem ipsum dolor sit amet.</p><span ' \
    'class="dff">Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro, nemo?</span></div></div> '

print(clear_2(s))
