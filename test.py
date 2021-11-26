import numpy as np
import cv2

def auto_whiteBalance(img):
    b, g, r = cv2.split(img)
    Y = 0.299 * r + 0.587 * g + 0.114 * b
    Cr = 0.5 * r - 0.419 * g - 0.081 * b
    Cb = -0.169 * r - 0.331 * g + 0.5 * b

    Mr = np.mean(Cr)
    Mb = np.mean(Cb)

    Dr = np.var(Cr)
    Db = np.var(Cb)

    temp_arry = (np.abs(Cb - (Mb + Db * np.sign(Mb))) < 1.5 * Db) & (
                np.abs(Cr - (1.5 * Mr + Dr * np.sign(Mr))) < 1.5 * Dr)
    RL = Y * temp_arry

    # 选取候选白点数的最亮10%确定为最终白点，并选择其前10%中的最小亮度值
    L_list = list(np.reshape(RL, (RL.shape[0] * RL.shape[1],)).astype(np.uint8))
    hist_list = np.zeros(256)
    min_val = 0
    sum = 0
    for val in L_list:
        hist_list[val] += 1

    for l_val in range(255, 0, -1):
        sum += hist_list[l_val]
        if sum >= len(L_list) * 0.1:
            min_val = l_val
            break
    # 取最亮的前10%为最终的白点
    white_index = RL < min_val
    RL[white_index] = 0

    # 计算选取为白点的每个通道的增益
    b[white_index] = 0
    g[white_index] = 0
    r[white_index] = 0

    Y_max = np.max(RL)
    b_gain = Y_max / (np.sum(b) / np.sum(b > 0))
    g_gain = Y_max / (np.sum(g) / np.sum(g > 0))
    r_gain = Y_max / (np.sum(r) / np.sum(r > 0))

    b, g, r = cv2.split(img)
    b = b * b_gain
    g = g * g_gain
    r = r * r_gain

    # 溢出处理
    b[b > 255] = 255
    g[g > 255] = 255
    r[r > 255] = 255

    res_img = cv2.merge((b, g, r))
    res_img = res_img.fromarray(img.astype('uint8')).convert('RGB')
    return res_img


img_data = cv2.imread(r'C:\Users\wwwwssssww\Downloads\dark_result\2015_02434_fake_B.png')
img = auto_whiteBalance(img_data)
cv2.imshow('test',img)
cv2.waitKey(0)
#cv2.imwrite('1_auto.jpg', img)