import time
def bubble_sort(data, drawData, sleep):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1 else "#12232E" for x in range(len(data))])
                time.sleep(sleep)
    drawData(data, ['green' for x in range(len(data))])