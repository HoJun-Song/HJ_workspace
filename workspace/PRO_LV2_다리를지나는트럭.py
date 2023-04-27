from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    stkTruckWeights = deque(truck_weights)
    bridge = deque()
    bridge_sum = 0
    while len(stkTruckWeights) > 0:
        answer += 1
        if bridge_length > len(bridge):
            curTruck = stkTruckWeights.popleft()
            if weight >= bridge_sum + curTruck:
                bridge.appendleft(curTruck)
                bridge_sum += curTruck
            else:
                stkTruckWeights.appendleft(curTruck)
                bridge.appendleft(0)
        else:
            bridge_sum -= bridge.pop()
            curTruck = stkTruckWeights.popleft()
            if weight >= bridge_sum + curTruck:
                bridge.appendleft(curTruck)
                bridge_sum += curTruck
            else:
                stkTruckWeights.appendleft(curTruck)
                bridge.appendleft(0)

    if len(bridge) > 0:
        answer += bridge_length

    return answer

print(solution(100, 100, [10]))

"""
SUM()을 여러번 -> 합계를 하나씩 + / - 헤주는 sum을 나타내는 변수로 사용하자!
"""