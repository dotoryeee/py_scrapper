import re

# https://www.w3schools.com/python/python_regex.asp
# https://docs.python.org/3/library/re.html

# 정규식 작성
p = re.compile("ca.e")


def printMatch(word):
    if word:
        print(word)
        print("일치하는 부분 : ", word.group())  # 단어 전체가 출력되지 않고 일치하는 부분만 출력됨
        print("전체 단어 : ", word.string)
        print("매칭 인덱스 : ", word.span())
        print("매칭 시작 인덱스 : ", word.start())
        print("매칭 마지막 인덱스 : ", word.end())
    else:
        print('정규식에 일치하지 않음')


# 검사할 단어
word = p.search("careless")
printMatch(word)
print("==============================================")
word2 = p.search("cave")
printMatch(word2)
print("==============================================")
word3 = p.search("safe")
printMatch(word3)
print("==============================================")
word4 = p.search("scare")
printMatch(word4)

# 문장에서 여러 단어를 찾아 리스트를 반환
li = p.findall("careless cafe supercave")
print(li)
