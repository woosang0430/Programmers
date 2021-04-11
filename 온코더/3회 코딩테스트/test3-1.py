def solution(document):
    limit_list = ['?','!']
    result = []
    # 공백까지 한번에 확인
    for i in document:
        # 물음표나 느낌표가 아니면 바로 붙이기
        if i not in limit_list:
            result.append(i)
        # 물음표나 느낌표면
        else:
            # 문장의 처음이나 앞에 알파벳이나 빈칸이면 바로 붙이기
            if len(result) == 0 or result[-1] not in limit_list:
                result.append(i)
            else:
                # 현재 문자가 물음표고 이전의 문자가 느낌표면 물음표로 바꾸기
                if i == '?' and result[-1] == '!':
                    result[-1] = i

    return ''.join(result)

s = "! !a!s!sD?sd???! a b c A B ! !!C?! ! ! !C ?!!? ?!? ??      "
print(solution(s))