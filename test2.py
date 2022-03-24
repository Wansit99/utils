import cv2
import time
url = "http://cmgw-vpc.lechange.com:8888/LCO/6G00BC2PAZC74E9/0/0/20211104T063134/55414094b9e38f2ee07ad32a1d4e625d.m3u8"
capture=cv2.VideoCapture(url)

fps = 0.0
while (True):
    t1 = time.time()
    # 读取某一帧
    ref, frame = capture.read()
    if not ref:
        break
    # 格式转变，BGRtoRGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # RGBtoBGR满足opencv显示格式
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    fps = (fps + (1. / (time.time() - t1))) / 2
    print("fps= %.2f" % (fps))
    frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("video", frame)
    c = cv2.waitKey(1) & 0xff

    if c == 27:
        capture.release()
        break