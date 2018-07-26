import serial
import time


class Read:
    def ConnectToDevice(self):
        self.sp=serial.Serial("COM3",9600,timeout=5)
        #self.sp.open()
    def CloseDevice(self):
        self.sp.close()
    def ReceivedData(self):
        data=self.sp.readline()
        return data.decode()

RD=Read()
RD.ConnectToDevice()


import pymysql
try:
    db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='1234', db='parking')
    cmd = db.cursor()
    q = "insert into mmmpark values('{}')".format(RD.ReceivedData())
    print(q)
    cmd.execute(q)
    db.commit()
    db.close()
    print("Record submit...")
except pymysql.InternalError as e:
    print("Error:",e)


