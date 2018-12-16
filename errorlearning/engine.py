import time
import read_file
from threading import Thread
from emailAttachment import sendemail 
from utils import clickpic

imageval = 0
tiltval = 0
ldrval = 0

#need to synchronise each function call 
#currently it is in serialise way
#will do later as it is not top priority

x = [0] * 10
y = [0] * 10
z = [0] * 10
w = [0] * 10

class compute(Thread):
    def run(self):
        while 1:
#            imageval = getimageval()
#            tiltval = gettiltval()
#            ldrval = getldrval()
            getimageval().start()
            gettiltval().start()
            getldrval().start()
            getheartbeat().start()
            time.sleep(12)


class getheartbeat(Thread):
    def run(self):
        for i in range(0,10) :
            w[i] = getvalfromheartbeatsensor()
            time.sleep(1)

class getimageval(Thread):
    def run(self):
        for i in range(0,10) :
            x[i] = getvalfromimagefile()
            time.sleep(1)


class gettiltval(Thread):
    def run(self):
        for i in range(0,10) :
            y[i] = getvalfromtiltsensor()
            time.sleep(1)

class getldrval(Thread):
    def run(self):
        for i in range(0,10) :
            z[i] = getvalfromldrsensor()
            time.sleep(1)


#we can have another thread that can coexist


#implement some server code here, getting value once in 10sec

#def getimageval() :
#    return 0


#def gettiltval() :
#    x = [0] * 10
#    for i in range(0,10):
#        x[i] = getvalfromtiltsensor()
#        time.sleep(0.1)

#    cnt0 = sum(n==0 for n in x)
#    cnt1 = sum(n==1 for n in x)

#    print(cnt0, cnt1)
#    return 1

#def getldrval() :
#    x = [0] * 10
#    for i in range(0,10):
#        x[i] = getvalfromldrsensor()
#        time.sleep(0.1)

#    cnt0 = sum(n==0 for n in x)
#    cnt1 = sum(n==1 for n in x)

#    print(cnt0, cnt1)
#    return 0



cntx0 = cnty0 = cntz0 = cntw0 = 0
cntx1 = cnty1 = cntz1 = cntw1 = 0

class checkformishap(Thread):
    def run(self):
        #raisealarm()
        while 1 :
            time.sleep(12.5)
            cntx0 = sum(n == 0 for n in x) #x is image
            cnty0 = sum(n == 0 for n in y) #y is tilt
            cntz0 = sum(n == 0 for n in z) #z is ldr
            cntw0 = sum(n == 0 for n in w) #w is heartbeat

            val = checkformishapfinal(cntx0, cnty0, cntz0, cntw0)
            if (val == 3) :
                raisealarm3()
            if (val == 2) :
                raisealarm2()
            if (val == 1) :
                raisealarm1()        

def checkformishapfinal(x0,y0,z0,w0) : 
    x1 = 10 - x0
    y1 = 10 - y0
    z1 = 10 - z0
    w1 = 10 - w0

    print(x1,y1,z1,w1)
    finalval = dangerlevel(x1, y1, z1, w1)
    return finalval

def dangerlevel(xx, yy, zz, ww) : 
    if zz == 10 and ww == 10 and yy == 10:
        return 3
    if xx == 10 : 
        return 3
    if zz >= 8 and ww >= 8 and yy >= 8 :
        return 2
    if xx >= 7 :
        return 2
    if zz >= 6 and ww >= 6 and yy >= 6 :
        return 1
    if xx >= 5 :
        return 1
    return 0
 
    
def raisealarm3() :
    clickpic()
    read_file.led_glow(3)
    sendemail("17.4405884,78.3786465")


def raisealarm2() :
    clickpic()
    read_file.led_glow(2)
    sendemail("17.4405884,78.3786465")


def raisealarm1() :
    clickpic()
    read_file.led_glow(1)
    sendemail("17.4405884,78.3786465")
#integrate map, alarm, and buzzer here 


#write the code for mishap detection here and send it outside


def getvalfromimagefile() :
    return 0

def getvalfromtiltsensor() :
    return read_file.read_tilt()

def getvalfromldrsensor() :
    return read_file.read_light()

def getvalfromheartbeatsensor() :
    return read_file.read_heartrate()

def run():
    compute().start()
    checkformishap().start()

run()

