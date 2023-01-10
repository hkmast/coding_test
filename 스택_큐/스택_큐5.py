# https://school.programmers.co.kr/learn/courses/30/lessons/42583
def solution(bridge_length, weight, truck_weights):
    time = 0

    maxtruck = len(truck_weights)
    maxtime = bridge_length * maxtruck + 1

    waits = [[truck_weights[i], bridge_length] for i in range(maxtruck)]
    dones = []
    ons = []

    while time <= maxtime:

        # print(f'{time}:\t{waits}\t\t / {ons}\t\t / {dones}')

        # 아직 차가 다 도착 안했으면
        if len(dones) != maxtruck:
            time += 1

            # 다리 위에 있는 차들 한칸씩 전진
            if ons:
                for on in ons:
                    on[1] -= 1

                # 다리를 지난 맨 앞차는 dones로 옮김
                if ons[0][1] <= 0:
                    dones.append(ons.pop(0))

            # 대기 중인 차량이 있다면 다리 위에 한대 추가
            if waits:

                # 만약 추가될 때 차량 무게가 다리 하중 보다 적거나 같고, 차량의 길이가 다리의 길이 보다 짧거나 같을때 추가
                if (waits[0][0] + sum(x[0] for x in ons) <= weight) and (
                    len(ons) + 1 <= bridge_length
                ):
                    ons.append(waits.pop(0))

        # 차량이 전부 도착 했으면
        else:
            break

    return time


print(solution(2, 10, [7, 4, 5, 6]))
