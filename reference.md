# list에서 value 값으로 다중 index 찾기
```python
arr = [1, 2, 3, 4, 5, 3]

idx_list = list(filter(lambda x: arr[x] == 3, range(len(arr))))
print(idx_list) # [2, 5]
```

# 2차원 배열 선언
```python
# 1. 2중 for문 사용
arr = [[0 for col in range(11)] for row in range(10)] # 10행 x 11열 리스트 생성

#2. 연산자와 for문 사용
arr = [[0] * 11 for i in range(10)] # 10행 x 11열 리스트 생성
```
