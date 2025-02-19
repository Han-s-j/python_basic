# 배열
# 1. 파이썬에서 기본적으로 제공하는 배열 (기능이 적음)
# 2. 다른 사람이 만든 배열 라이브러리 사용 (기능이 많고 복잡함)


# 로또 번호 7자리 숫자를 변수에 담겠다
num1 = 7
num2 = 15
num3 = 19
num4 = 23
num5 = 27
num6 = 32
num7 = 45

# 7개의 숫자를 한 곳에 담아서 처리하면 편하지 않을까?

# 배열의 선언
lotto = []  # []는 비어있는 배열을 의미함

print(lotto)

# lotto는 배열을 담고 있는 변수가 됨
# 내부에 값을 추가하는 함수를 가지고 있음
lotto.append(7)

print(lotto)

lotto.append(15)
lotto.append(19)
lotto.append(23)
lotto.append(27)
lotto.append(32)
lotto.append(45)

print(lotto)

# 배열의 길이 확인 (값이 몇 개 들어있는지)
print("배열의 길이:", len(lotto))

# 배열의 인덱싱, 슬라이싱
print(lotto[1])  # 15
print(lotto[:3]) # [7, 15, 19]
print(lotto[1:2]) # [15] 하나만 꺼내기 가능

# 배열 내 값 제거
# 인덱스 1번의 13을 제거
lotto.pop(1) # 지우고자 하는 인덱스 번호 입력
print(lotto)

# 값 21을 제거
lotto.remove(19) # 지우고자 하는 값을 입력
print(lotto)

# 배열 내 값 전부 제거
lotto.clear()
print(lotto)


# 값을 넣은 채로 배열을 선언
lotto = [23, 10, 7, 5, 21, 30]
print(lotto)

# 8 9 18 35 39 45

# 배열을 정렬하기
lotto.sort() #오름차순 정렬이 일어남
print(lotto)

# 내림차순 정렬
lotto.sort(reverse=True)
print("내림차순:",lotto)

lotto2 = [34, 12, 15, 7, 43, 23]
print(lotto2)

# 배열을 오름차순으로 정렬을 한 후, 배열의 첫번째 값 꺼내기(최소값)
# 배열의 마지막 값 꺼내기(최대값)

# 배열을 오름차순 정렬 시켜!!
lotto2.sort()
print(lotto2)
# 배열의 첫번째 값을 꺼내!!
print("최솟값:",lotto2[0])

# 배열의 마지막 값 꺼내!!
print("최댓값:",(lotto2 [len(lotto2)-1]))
print("최댓값:",lotto2[-1])

# 2차원 데이터를 다룬다면?
# 로또용지 (5000원) - 5줄
lotto1 = [2, 7, 14, 15, 18, 20]
lotto2 = [5, 9, 16, 25, 28, 33]
lotto3 = [4, 7, 24, 25, 38, 41]
lotto4 = [6, 12, 14, 25, 33, 38]
lotto5 = [3, 8, 17, 21, 23, 37]

lotto = []
lotto.append(lotto1)
lotto.append(lotto2)
lotto.append(lotto3)
lotto.append(lotto4)
lotto.append(lotto5)

print(lotto)
print(lotto[1]) #lotto2
print(lotto[2]) #lotto3

print(lotto2[2]) #16

# 인덱스 1번의 배열을 꺼낸 후, 해당 배열에서 인덱스 2번의 값을 꺼냄
print(lotto[1][2])

# 로또용지(5줄) 3장 - 3차원 데이터

books = "이것이자바다,자바의정석,데이터경영론"

# ["이것이자바다", "자바의정석", "데이터경영론"] 로 확보
bookArray = books.split(",")
print(books)
print(bookArray)
