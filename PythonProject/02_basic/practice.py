# 문자열 가지고 놀기
my_famliy = "수정, 풍현, 미란, 홍구, 순구"

#  자동완선 단축키 [Ctrl + Space]
print(my_famliy)

# 문자열의 글자수 확인
# length의 약자를 써서 len() 사용
print(len(my_famliy))

# 문자열의 인덱스(넘버링)를 이용하여 특정 문자 꺼내기

print(my_famliy[1])  # 부
print(my_famliy[5])  # 사
print(my_famliy[9], "ㅎ")  # 사

# 어떤 문자열이든 첫번째 문자만 꺼내겠다
aespaA = "카리나"
aespaB = "윈터"
aespaC = "닝닝"
aespaD = "지젤"

print(aespaA[0])
print(aespaB[0])
print(aespaC[0])
print(aespaD[0])

# 어떤 문자열이든 마지막 문자만 꺼내겠다
# stuA (3글자)의 마지막 문자의 인덱스 : 2
# stuB (2글자)의 마지막 문자의 인덱스 : 1
# stuC (4글자)의 마지막 문자의 인덱스 : 3

stuX = "김하얀푸른"
last = len(stuX) - 1
print(last)
print(stuX[last])

# 코드 자동 정렬(포맷팅) 단축키 [Ctrl + Shift + F]
print(aespaA[len(aespaA) - 1])
print(aespaB[len(aespaB) - 1])
print(aespaC[len(aespaC) - 1])
print(aespaD[len(aespaD) - 1])
