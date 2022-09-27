import random



body = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def randomaizer():
    number = 2 if int(random.randint(0, 11)) else 4

    a = []


    for strng in range(len(body)):
        for indx in range(len(body[strng])):
            if not body[strng][indx]:
                a.append(indx + 4*strng)

    rplace = random.choice(a)

    place = rplace-(rplace//4)*4
    rplace = rplace//4

    body[rplace][place] = number
    [print(i) for i in body]

def game_over():
    if not [1 for i in body if 0 in i] and [[1 for ii in range(len(i[:3])) if i[ii] == i[ii + 1]] for i in body] == [[], [], [], []] and [[1 for ii in range(len(body[:3])) if body[i][ii] == body[i+1][ii]] for i in range(3)] == [[], [], []]:
        return 1
    elif [2048 for i in body if 2048 in i]:
        return 2
    else:
        return 0

randomaizer()
while 1:
    inp = input()

    if inp == '4':
        for strng in body:
            for iiii in range(3):
                for i in range(len(strng)):
                    if strng[i] and i and not strng[i - 1]:
                        a = strng[i]
                        strng[i] = 0
                        strng[i - 1] = a
            for i in range(len(strng)):
                if strng[i] and i and strng[i] == strng[i - 1]:
                    a = strng[i]
                    strng[i] = 0
                    strng[i - 1] = a * 2
            for i in range(len(strng)):
                if strng[i] and i and not strng[i - 1]:
                    a = strng[i]
                    strng[i] = 0
                    strng[i - 1] = a

    elif inp == '8':
        for ind in range(4):
            for iiii in range(3):
                for strng_number in range(len(body)):
                    if body[strng_number][ind] and strng_number and not body[strng_number - 1][ind]:
                        a = body[strng_number][ind]
                        body[strng_number][ind] = 0
                        body[strng_number - 1][ind] = a
            for strng_number in range(len(body)):
                if body[strng_number][ind] and strng_number and body[strng_number][ind] == body[strng_number - 1][ind]:
                    a = body[strng_number][ind]
                    body[strng_number][ind] = 0
                    body[strng_number - 1][ind] = a*2
            for strng_number in range(len(body)):
                if body[strng_number][ind] and strng_number and not body[strng_number - 1][ind]:
                    a = body[strng_number][ind]
                    body[strng_number][ind] = 0
                    body[strng_number - 1][ind] = a

    elif inp == '6':
        for strng in body:
            strng.reverse()
            for iiii in range(3):
                for i in range(len(strng)):
                    if strng[i] and i and not strng[i - 1]:
                        a = strng[i]
                        strng[i] = 0
                        strng[i-1] = a
            for i in range(len(strng)):
                if strng[i] and i and strng[i] == strng[i - 1]:
                    a = strng[i]
                    strng[i] = 0
                    strng[i - 1] = a*2
            for i in range(len(strng)):
                if strng[i] and i and not strng[i - 1]:
                    a = strng[i]
                    strng[i] = 0
                    strng[i-1] = a
            strng.reverse()

    elif inp == '2':
        body.reverse()
        for ind in range(4):
            for iiii in range(3):
                for strng_number in range(len(body)):
                    if body[strng_number][ind] and strng_number and not body[strng_number - 1][ind]:
                        a = body[strng_number][ind]
                        body[strng_number][ind] = 0
                        body[strng_number - 1][ind] = a
            for strng_number in range(len(body)):
                if body[strng_number][ind] and strng_number and body[strng_number][ind] == body[strng_number - 1][ind]:
                    a = body[strng_number][ind]
                    body[strng_number][ind] = 0
                    body[strng_number - 1][ind] = a*2
            for strng_number in range(len(body)):
                if body[strng_number][ind] and strng_number and not body[strng_number - 1][ind]:
                    a = body[strng_number][ind]
                    body[strng_number][ind] = 0
                    body[strng_number - 1][ind] = a
        body.reverse()
    if game_over() == 2:
        print('Win')
        break
    elif game_over():
        print('GG WP')
        break
    print('========================')
    randomaizer()


