"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
  4-3. ')'를 다시 붙입니다.
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
  4-5. 생성된 문자열을 반환합니다.

"""


def check_valid(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True


def reverse_blank(b):
    if b == '(':
        return ')'
    return '('


def make_answer(l):

    if len(l) == 0:
        return l
    count = [0, 0]
    for i in range(len(l)):
        if l[i] == '(':
            count[0] += 1
        else:
            count[1] += 1
        if count[0] == count[1]:
            u, v = l[:i + 1], l[i+1:]
            break
    if check_valid(u) is True:
        return u + make_answer(v)
    else:
        u.pop(0)
        u.pop(-1)
        return ['('] + make_answer(v) + [')'] + list(map(reverse_blank, u))


def solution(p):
    l1 = list(p)
    ans = make_answer(l1)
    return ''.join(ans)


print(check_valid("()"))
print(solution("()))((()"))
