## 기준에 따라 데이터 정렬
---

### 선택정렬
이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고 , 그 다음 데이터를 선택해 두번째 데이터와 바꾸는 과정을 반복
```python
# 선택정렬 소스 코드
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
  min_index = i # 가장 작은 원소 인덱스 
  for j in range(i + 1, len(array)):
    if array[min_index] < array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index] array[i]

print(array)
```

### 삽입정렬
앞의 데이터는 이미 정렬 되었다고 가정하고 정렬되어 있는 데이터에서 적절한 위치를 찾은 뒤, 특정 데이터를 그 위치에 삽입하는 정렬
(삽입 데이터는 두번째 부터 시작, 앞의 데이터는 이미 정렬되어 있다고 가정하기 때문)
```python
array = [7,5,9,0,3,1,6,2,4,8]

# 두번째 데이터 부터 시작
for i in range(1, len(array)):
  # 그 다음 데이터 부터 왼쪽으로 크기 비교하여 스와프
  for j in range(i, 1, -1):  # range(start, end, step)
    if array[j] < array[j-1]:
      array[j], array[j-1] = array[j-1], array[j]
    else:
      break

print(array)
```

### 퀵정렬
기준 데이터를 정하고 그 데이터를 기준으로 큰데이터와 작은 데이터의 위치를 바꿔 리스트를 반으로 나누는 방식으로 동작
- 피벗 : 큰 숫자와 작은 숫자를 교환하기 위한 '기준'으로 피벗을 어떻게 설정할 것인지 미리 명시
- 호어 분할 : 리스트에서 첫번째 데이터를 피벗으로 설정
```python
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
  if start >= end:  # 원소가 1개인 경우 종료  
    return
  pivot = start  # 피벗은 첫번째 원소
  left = start + 1
  right = end
  while left <= right:  # while문은 조건이 참일 동안 계속 반복
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while left <= end and array[left] < array[pivot]:
      left += 1
    # 피벗보다 작은 데이터 찾을 때까지 반복
    while right >= start and array[right] > array[pivot]:
      right -= 1
    if left > right:  # 엇갈렸다면 작은 데이터와 피봇 스와프
      array[left], array[pivot] = array[pivot], array[left]
    else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체 
      array[left], array[right] = array[right], array[left]
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
  quick_sort(array, start, right -1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array)-1)
print(array)
```
```python
# python의 장점을 살린 퀵정렬 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
  # 리스트가 하나 이하의 원소를 담고 있다면 종료
  if len(array) <= 1:
    return
   pivot = array[0]
   tail = array[1:]

   left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽
   right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽

  # 분할 이후 왼쪽부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

