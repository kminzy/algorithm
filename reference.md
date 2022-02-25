# list에서 value 값으로 다중 index 찾기
```python
arr = [1, 2, 3, 4, 5, 3]

idx_list = list(filter(lambda x: arr[x] == 3, range(len(arr))))
print(idx_list) # [2, 5]
```
