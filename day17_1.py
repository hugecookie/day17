def is_queue_full():
    global SIZE, queue, front, rear
    if (rear + 1) % SIZE == front:
        return True
    else:
        return False


def is_queue_empty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False


def enqueue(dat):
    global SIZE, queue, front, rear
    if is_queue_full():
        print("Queue is full!")
        return
    rear = (rear + 1) % SIZE
    queue[rear] = dat


def dequeue():
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
        print("Queue is empty!")
        return None
    return queue[(front + 1) % SIZE]


SIZE = int(input("SIZE of Queue : "))
queue = [None for _ in range(SIZE)]
front = rear = 0

if __name__ == "__main__":

    while True:
        select = input("Insert(i)/Extract(e)/Veripy(v)/eXit(x) : ")
        if select == 'X' or select == 'x':
            break
        elif select == 'I' or select == 'i':
            data = input("Insert data : ")
            enqueue(data)
            print("queue status : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'E' or select == 'e':
            data = dequeue()
            print("extract data ==> ", data)
            print("queue status : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'V' or select == 'v':
            data = peek()
            print("veripy data ==> ", data)
            print("queue status : ", queue)
            print("front : ", front, ", rear : ", rear)
        else:
            print("input mismatch")

    print("program exit!")
