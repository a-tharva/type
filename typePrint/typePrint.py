import sys
import time

line1 = ['1','2','3','4','5','6','7','8','9','0','-','=']
line2 = ['q','w','e','r','t','y','u','i','o','p','[',']']
line3 = ['a','s','d','f','g','h','j','k','l',';']
line4 = ['z','x','c','v','b','n','m',',','.','/']

start_speed = 9./90
#print(type(11./90))
#print(11./90)

def typeNormal(str):
    for c in str + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3./90)
        
#normal_type_print(input(":"))


def typeHuman(str):
    speed = start_speed
    for c in str:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)
        speed = speed - .08/90
#        print(speed)
        if c == ' ':
            time.sleep(.008)
            speed = start_speed
#    sys.stdout.write('\b')
#    time.sleep(11./90)
#    sys.stdout.write(' ')
#    time.sleep(11./90)
#    sys.stdout.write(':')
    
human('''Itself set open together over face. Place stars you're was called his night. Subdue together that us, give divided all. In open divided in seed so set over i.

Thing cattle. First brought there likeness a, together. Air dominion one all also won't multiply, he. Signs. Stars under very, fish days our. Without forth brought, stars creature won't. Gathering creeping let you their.

Every. That divide third gathered. Whales two dry dominion. To, yielding lesser to you'll open god forth. Let living won't moveth meat above fly greater unto divide living firmament may sea saying can't the for whose divide.''')
