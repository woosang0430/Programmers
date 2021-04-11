def solution(document):
    x = 0
    if document[0] == ' ':
        x = True
    document = document.split()
    result_list = []
    limit_str = ['?', '!']
    for string in document:
        result = []
        for i in string:
            if i not in limit_str:
                result.append(i)
                continue
            else:
                if len(result) == 0 or result[-1] not in limit_str:
                    result.append(i)
                    continue
                else:
                    if result[-1] == '!' and i == '?':
                        result[-1] = '?'
        
        result_list.append(''.join(result))
    ret = ' '.join(result_list)
    if x:
        ret = ' ' + ret
    return ret

print(solution(" a b c A B ! !!C!?! ! ! !C ?!!? ?!? ??"))