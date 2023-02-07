def is_queue_full():
    global SIZE, queue, front, rear
    if rear == SIZE - 1:
        return True
    else:
        return False


def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def en_queue(data):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("Queue is full!")
        return
    rear += 1
    queue[rear] = data


def de_queue():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("Queue is empty!")
        return None
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None

    return data


def peek():
    global SIZE, queue, front, rear
    if is_queue_empty():
        print("Queue is empty")
        return None
    return queue[front + 1]


def sum_time():
    global SIZE, queue, front, rear
    timesum = 0
    for i in range(front + 1, rear + 1):
        timesum = timesum + people[i][1]
    return timesum


SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1
people = [('사용', 4), ('컴플레인', 20), ('명의변경', 10), ('환불요청', 3), ('고장', 5)]

if __name__ == "__main__":
    for i in range(SIZE):
        en_queue(people[i])
        print(f"귀하의 예상 대기 시간은 {sum_time()}분 입니다. ")
        if i == SIZE - 1:
            print(f'최종 대기 콜 : {queue}')
            print('프로그램 종료!')
            break
        print(f'대기 콜 : {queue}')
