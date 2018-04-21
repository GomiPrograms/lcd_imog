import RPi.GPIO as GPIO
import os

def printLCD(input1, input2):
    lenCheck(input1)
    lenCheck(input2)
    line1 = ''
    for currentStr in list(input1):
        currentStr = str(currentStr.encode('shift-jis'))
        # b' ' を削除
        currentStr = currentStr[2:-1]
        currentStr = currentStr.replace('\\', '0')
        if len(currentStr) < 2:
            currentStr = str(hex(ord(currentStr)))
        currentStr = currentStr + ' '
        line1 = line1 + currentStr

    line2 = ''
    for currentStr in list(input2):
        currentStr = str(currentStr.encode('shift-jis'))
        # b' ' を削除
        currentStr = currentStr[2:-1]
        currentStr = currentStr.replace('\\', '0')
        if len(currentStr) < 2:
            currentStr = str(hex(ord(currentStr)))
        currentStr = currentStr + ' '
        line2 = line2 + currentStr

    # 文字列を1文字ずつにリスト化
    line1_list = line1.split()
    line2_list = line2.split()

    line1 = ' '.join(line1_list)
    line2 = ' '.join(line2_list)

    # ---DEBUG---
    # print(line1)
    # print(line2)

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    backLED = GPIO.input(4)
    if backLED == 0:
        GPIO.output(4, 1)

    # LCD初期化
    resetLED()

    # LCD一行目の制御
    os.system('sudo i2cset -y 1 0x3e 0x00 0x00 b')
    os.system('sudo i2cset -y 1 0x3e 0x40 ' + line1 + ' i')
    # LCDニ行目の制御
    os.system('sudo i2cset -y 1 0x3e 0x00 0xC0 b')
    os.system('sudo i2cset -y 1 0x3e 0x40 ' + line2 + ' i')

# LCD初期化
def resetLED():
    os.system('sudo i2cset -y 1 0x3e 0x00 0x38 0x39 0x14 0x70 0x56 0x6c 0x38 0x0C 0x01 i')

# 文字数チェック
def lenCheck(self):
    if len(self) > 8:
        print('許容文字数をオーバーしました。8文字以内で設定してください。')
        exit()

def cleanupLCD():
    GPIO.cleanup()

# バックライトを消して文字も消す
def clearAll():
    os.system('sudo i2cset -y 1 0x3e 0x00 0x38 0x39 0x14 0x70 0x56 0x6c 0x38 0x0C 0x01 i')
    GPIO.cleanup()

if __name__ == '__main__':
    print('You can use this module when you import another scripts.')
    exit()