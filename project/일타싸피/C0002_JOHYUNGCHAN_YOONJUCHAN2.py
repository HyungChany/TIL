import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'CHANCHANCHAN_before'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.


    r = 5.73
    def radToDeg(radian):
        return (360 + 90 - radian * 180 / math.pi) % 360


    myHOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
    for i in range(len(HOLES)):
        myHOLES[i][0] = HOLES[i][0] - (i % 3 - 1) * 2
        myHOLES[i][1] = HOLES[i][1] - (i // 3 * 2 - 1) * 2

    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]

    # 타겟공 정하기
    T = []
    passNum = 0
    lst = []
    if order == 1:
        order = [1, 3]
    elif order == 2:
        order = [2, 4]

    for i in order:
        if balls[i][0] != -1:

            tx = balls[i][0]
            ty = balls[i][1]

            # 경로상에 공이 있는 지-1 (흰공-목적구)
            
            flag = True
            for j in range(1, 6):
                if i == j:
                    continue
                bx, by = balls[i][0], balls[i][1]
                area = abs((bx - whiteBall_x) * (ty - whiteBall_y) - (tx - whiteBall_x) * (by - whiteBall_y))
                mit = math.sqrt(abs(whiteBall_x-tx)**2 + abs(whiteBall_y-ty)**2)
                dist = area / mit
                if dist >= r:
                    flag = False
                    break
            if flag or passNum == 1:
                targetBall_x = balls[i][0]
                targetBall_y = balls[i][1]
                T.append([targetBall_x, targetBall_y])
    if not T :
        T.append([balls[5][0], balls[5][1]])


    # 칠 위치 정하기
    for targetBall_x, targetBall_y in T :
    # width, height: 목적구와 흰 공의 X좌표 간의 거리, Y좌표 간의 거리
        width = abs(targetBall_x - whiteBall_x)
        height = abs(targetBall_y - whiteBall_y)

        # 구멍 정하기
        minHole = -1
        sub = 0
        for i in range(6):
            hx, hy = myHOLES[i][0], myHOLES[i][1]

            radian = math.atan2(targetBall_y - hy, targetBall_x - hx)
            tx = math.cos(radian) * r + targetBall_x
            ty = math.sin(radian) * r + targetBall_y

            radian1 = math.atan2(hy - ty, hx - tx)
            radian2 = math.atan2(whiteBall_y - ty, whiteBall_x - tx)
            degree1 = radToDeg(radian1)
            degree2 = radToDeg(radian2)

            s1 = (whiteBall_x - hx) ** 2 + (whiteBall_y - hy) ** 2
            s2 = (tx - hx) ** 2 + (ty - hy) ** 2
            s3 = (tx - whiteBall_x) ** 2 + (ty - whiteBall_y) ** 2
            
            cal = abs(degree1 - degree2)
            if  s2 > 0 and s3 > 0 :
                tmp = ((s2 + s3) - s1) / (2*math.sqrt(s2*s3))
                if tmp > 1 :
                    tmp = 1
                elif tmp < -1 :
                    tmp = -1
                new_a = math.acos(tmp)
                if new_a > sub :
                    tt_ball_x = targetBall_x
                    tt_ball_y = targetBall_y
                    minHole = i
                    sub = new_a

    hx, hy = myHOLES[minHole][0], myHOLES[minHole][1]

    radian = math.atan2(tt_ball_y - hy, tt_ball_x - hx)
    tx = math.cos(radian) * r + tt_ball_x
    ty = math.sin(radian) * r + tt_ball_y


    radian1 = math.atan2(ty - whiteBall_y, tx - whiteBall_x)
    angle = (360 + 90 - radian1 * 180 / math.pi) % 360
    

    # distance: 두 점(좌표) 사이의 거리를 계산
    # distance = math.sqrt(width**2 + height**2)
    distance = (math.sqrt(width**2 + height**2) + math.sqrt(abs(tx-hx)**2 + abs(ty-hy)**2)) / 2

    # power: 거리 distance에 따른 힘의 세기를 계산
    if distance > 180: power = distance * 0.62
    elif distance > 100: power = distance * 0.57
    elif distance > 60: power = distance * 0.48
    elif distance > 30: power = distance * 0.43
    elif distance < 30: power = distance * 0.5

    print(f'길이:{distance}')
    print(f'각도:{angle}')

    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')