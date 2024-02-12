# class Solution(object):
#     def duplicateZeros(self, arr):
#         arr2 = [i for i in arr]
#         print("arr2:", arr2)
#         i = 0
#         j = 0
#         while i < len(arr):  # len(arr): 8
#             #  print("i:", i)
#             if not arr2[j]:

#                 # print("arr2[j]:", arr2[j])
#                 # arr[i] = 0
#                 i += 1
#                 if i < len(arr):
#                     arr[i] = 0
#             else:
#                 arr[i] = arr2[j]
#             j += 1
#             i += 1
#         return arr

#     def duplicateZeros2(self, arr):
#         arr2 = [i for i in arr]
#         j = 0
#         for i in range(len(arr)):

#             if not arr2[i]:
#                 i += 1
#                 if i < len(arr):
#                     arr[i] = 0
#             else:
#                 arr[i] = arr2[j]
#             j += 1
#             i += 1
#         return arr


# ob1 = Solution()
# print(ob1.duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
# print(ob1.duplicateZeros2([1, 0, 2, 3, 0, 4, 5, 0]))

# n = 1260
# count = 0
# coin_types = [500, 100, 50, 10]
# for coin in coin_types:
#     count += n // coin
#     n %= coin
#     print(n)

# print(count)

# # ------------------------------------------
# # 배열이 있을 떄 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# # n:배열크기, m:더해지는 횟수, k:연속가능한 횟수
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()  # 입력받은 수 정렬
# first = data[n-1]  # 가장 큰 수
# second = data[n-2]  # 두번째로 큰 수

# res = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         res += first
#         m -= 1
#     if m == 0:
#         break
#     res += second
#     m -= 1
# print(res)

# # 방법2
# n, m, k = map(int, input().split())
# data = list(map(int, input().split()))

# data.sort()  # 입력받은 수 정렬
# first = data[n-1]  # 가장 큰 수
# second = data[n-2]  # 두번째로 큰 수

# # 가장 큰 수가 더해지는 횟수
# count = int(m/(k+1)) * k
# count += m % (k+1)  # 나머지

# res = 0
# res += (count) * first
# res += (m-count) * second
# print(res)
# ---------------------------------------------------------
# 게임 개발 맵:4*4, 좌표:(1,1,0) (1,1) 북쪽
n, m = map(int, input(). split())

# 방문한 위치 저장
d = [[0]* m for _ in range(n)]
print("inital_d:", d)
# 현재 캐릭터 위치 입력받기 -> (1,1,0)
x,y,direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문처리 
print(d)

# 전제 맵정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction # 정수형 변수인 direction 변수가 함수 바깥에서 선언된 전역변수이기 때문
    direction -= 1 # 해당방향에서 왼쪽으로 돌면 방향이 -1 한만큼 바뀐다. 북>서>남>동>북
    if direction == -1:
        direction = 3 # 북에서 서로 변경된걸 의미 

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재, 육지면 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가본 칸이거나 바다인 경우
    else:
        turn_time += 1
    if turn_time == 4: # 네 방향 모두 갈 수 없는 경우
        nx = x - dx[direction]
        ny = y = dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤로 바다
        else:
            break
        turn_time = 0
print(count)


array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
  min_index = i # 가장 작은 원소 인덱스 
  for j in range(i + 1, len(array)):
    if array[min_index] < array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]

print(array)