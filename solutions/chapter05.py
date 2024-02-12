# def rec_function(i):
#     # 100번째 출력했을 떄 종료되도록 종료 조건 명시
#     if i == 10:
#         return
#     print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
#     rec_function(i+1)
#     print(i, '번째 함수를 종료합니다.')
# rec_function(1)




# 실전 문제 - 음료수 얼려먹기
n,m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기 
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#dsf로 특정한 노드를 방문한 뒤에 연결된 모든 노드들 방문
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        # 상,하,좌,우의 위치도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
res = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j) == True:
            res += 1
print(res)
