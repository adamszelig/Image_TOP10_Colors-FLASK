import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import math

SENSITIVITY = 50

def color(file):

    def dist(a, b):
        d = math.floor(math.sqrt(pow(b[0]-a[0], 2)+pow(b[1]-a[1], 2)+pow(b[2]-a[2], 2)))
        return d

    def new_color(colors, pixel):
        new = True
        for color in colors:
            if dist(pixel, color['rgb']) < SENSITIVITY and new:
                color['count'] += 1
                new = False
                break
        if new:
            colors.append({'rgb': [pixel[0], pixel[1], pixel[2]], 'count': 1})

    img_org = Image.open(file)
    img = img_org.resize((200, 100))
    img_array = np.array(img)
    img_array = img_array.tolist()

    colors = []
    colors.append({'rgb':[img_array[0][0][0],img_array[0][0][1],img_array[0][0][2]], 'count':1})

    width, height = img.size

    for i in range(height):
        for j in range(width):
            new_color(colors, img_array[i][j])
            # pass

    # colors=[{'rgb': [5, 8, 13], 'count': 2514}, {'rgb': [5, 9, 13], 'count': 179}, {'rgb': [6, 11, 15], 'count': 419}, {'rgb': [9, 14, 18], 'count': 654}, {'rgb': [11, 16, 20], 'count': 377}, {'rgb': [12, 17, 21], 'count': 179}, {'rgb': [37, 45, 50], 'count': 5631}, {'rgb': [44, 55, 61], 'count': 1634}, {'rgb': [44, 60, 60], 'count': 135}, {'rgb': [51, 62, 64], 'count': 864}, {'rgb': [53, 64, 66], 'count': 285}, {'rgb': [55, 65, 67], 'count': 180}, {'rgb': [59, 68, 70], 'count': 442}, {'rgb': [61, 66, 69], 'count': 70}, {'rgb': [62, 67, 70], 'count': 38}, {'rgb': [68, 74, 73], 'count': 562}, {'rgb': [69, 75, 73], 'count': 66}, {'rgb': [71, 79, 76], 'count': 288}, {'rgb': [74, 85, 81], 'count': 352}, {'rgb': [75, 86, 82], 'count': 75}, {'rgb': [88, 100, 96], 'count': 790}, {'rgb': [97, 109, 105], 'count': 372}, {'rgb': [103, 114, 113], 'count': 248}, {'rgb': [110, 115, 117], 'count': 139}, {'rgb': [113, 124, 116], 'count': 110}, {'rgb': [131, 141, 133], 'count': 527}, {'rgb': [140, 148, 141], 'count': 229}, {'rgb': [136, 150, 141], 'count': 8}, {'rgb': [138, 152, 146], 'count': 77}, {'rgb': [149, 160, 157], 'count': 242}, {'rgb': [155, 168, 161], 'count': 133}, {'rgb': [160, 173, 164], 'count': 67}, {'rgb': [163, 175, 171], 'count': 127}, {'rgb': [165, 177, 173], 'count': 48}, {'rgb': [169, 184, 182], 'count': 138}, {'rgb': [172, 188, 188], 'count': 99}, {'rgb': [181, 195, 189], 'count': 104}, {'rgb': [188, 199, 195], 'count': 120}, {'rgb': [178, 197, 197], 'count': 13}, {'rgb': [179, 198, 198], 'count': 2}, {'rgb': [177, 206, 202], 'count': 21}, {'rgb': [187, 212, 209], 'count': 100}, {'rgb': [199, 221, 219], 'count': 185}, {'rgb': [210, 232, 230], 'count': 167}, {'rgb': [215, 237, 235], 'count': 84}, {'rgb': [216, 236, 235], 'count': 6}, {'rgb': [220, 239, 238], 'count': 48}, {'rgb': [219, 244, 242], 'count': 28}, {'rgb': [221, 245, 242], 'count': 16}, {'rgb': [222, 241, 241], 'count': 5}, {'rgb': [224, 241, 241], 'count': 13}, {'rgb': [223, 242, 241], 'count': 4}, {'rgb': [6, 18, 21], 'count': 1}, {'rgb': [10, 13, 22], 'count': 10}, {'rgb': [219, 241, 243], 'count': 3}, {'rgb': [223, 243, 244], 'count': 4}, {'rgb': [6, 15, 24], 'count': 5}, {'rgb': [211, 245, 248], 'count': 5}, {'rgb': [214, 248, 248], 'count': 2}, {'rgb': [9, 13, 23], 'count': 2}, {'rgb': [12, 18, 16], 'count': 48}, {'rgb': [19, 16, 12], 'count': 55}, {'rgb': [221, 245, 245], 'count': 3}, {'rgb': [106, 144, 159], 'count': 53}, {'rgb': [49, 105, 127], 'count': 37}, {'rgb': [51, 96, 118], 'count': 11}, {'rgb': [90, 112, 123], 'count': 19}, {'rgb': [93, 153, 174], 'count': 29}, {'rgb': [52, 119, 146], 'count': 19}, {'rgb': [58, 100, 124], 'count': 1}, {'rgb': [57, 105, 127], 'count': 1}, {'rgb': [58, 120, 146], 'count': 5}, {'rgb': [98, 146, 164], 'count': 2}, {'rgb': [92, 157, 184], 'count': 12}, {'rgb': [77, 67, 60], 'count': 8}, {'rgb': [59, 111, 131], 'count': 1}, {'rgb': [42, 114, 150], 'count': 2}, {'rgb': [130, 183, 194], 'count': 24}, {'rgb': [1, 16, 29], 'count': 1}, {'rgb': [7, 18, 20], 'count': 1}, {'rgb': [23, 63, 77], 'count': 2}, {'rgb': [30, 60, 85], 'count': 2}, {'rgb': [47, 124, 155], 'count': 5}, {'rgb': [2, 19, 24], 'count': 1}, {'rgb': [22, 13, 12], 'count': 8}, {'rgb': [13, 13, 14], 'count': 22}, {'rgb': [13, 15, 14], 'count': 1}, {'rgb': [71, 111, 124], 'count': 1}, {'rgb': [89, 75, 65], 'count': 13}, {'rgb': [61, 114, 130], 'count': 1}, {'rgb': [23, 11, 12], 'count': 3}, {'rgb': [24, 9, 9], 'count': 1}, {'rgb': [26, 10, 10], 'count': 1}, {'rgb': [24, 10, 11], 'count': 1}, {'rgb': [15, 15, 15], 'count': 54}, {'rgb': [74, 117, 126], 'count': 2}, {'rgb': [222, 244, 241], 'count': 1}, {'rgb': [17, 10, 13], 'count': 1}, {'rgb': [54, 31, 25], 'count': 164}, {'rgb': [224, 243, 235], 'count': 1}, {'rgb': [91, 75, 68], 'count': 2}, {'rgb': [55, 119, 151], 'count': 3}, {'rgb': [79, 151, 186], 'count': 1}, {'rgb': [3, 17, 23], 'count': 1}, {'rgb': [3, 17, 26], 'count': 2}, {'rgb': [52, 32, 27], 'count': 2}, {'rgb': [58, 121, 146], 'count': 1}, {'rgb': [98, 145, 171], 'count': 1}, {'rgb': [5, 15, 25], 'count': 2}, {'rgb': [86, 161, 184], 'count': 1}, {'rgb': [69, 107, 133], 'count': 1}, {'rgb': [59, 104, 135], 'count': 1}, {'rgb': [102, 80, 72], 'count': 7}, {'rgb': [75, 109, 131], 'count': 1}, {'rgb': [95, 149, 174], 'count': 1}, {'rgb': [55, 121, 147], 'count': 1}, {'rgb': [157, 130, 129], 'count': 3}, {'rgb': [116, 88, 82], 'count': 12}, {'rgb': [103, 149, 163], 'count': 3}, {'rgb': [229, 243, 235], 'count': 2}, {'rgb': [57, 32, 27], 'count': 1}, {'rgb': [67, 118, 134], 'count': 1}, {'rgb': [85, 154, 185], 'count': 1}, {'rgb': [225, 244, 239], 'count': 1}, {'rgb': [78, 113, 121], 'count': 1}, {'rgb': [125, 93, 94], 'count': 7}, {'rgb': [227, 238, 237], 'count': 1}, {'rgb': [225, 242, 242], 'count': 3}, {'rgb': [117, 97, 91], 'count': 2}, {'rgb': [232, 233, 233], 'count': 1}, {'rgb': [119, 101, 97], 'count': 2}, {'rgb': [227, 239, 241], 'count': 2}, {'rgb': [124, 104, 100], 'count': 3}, {'rgb': [114, 101, 106], 'count': 1}, {'rgb': [86, 113, 120], 'count': 2}, {'rgb': [125, 103, 93], 'count': 1}, {'rgb': [190, 180, 180], 'count': 1}, {'rgb': [3, 18, 25], 'count': 1}, {'rgb': [190, 206, 170], 'count': 2}, {'rgb': [24, 69, 85], 'count': 1}, {'rgb': [28, 67, 82], 'count': 1}, {'rgb': [190, 207, 171], 'count': 1}, {'rgb': [30, 65, 84], 'count': 1}, {'rgb': [79, 113, 125], 'count': 3}, {'rgb': [106, 147, 162], 'count': 2}, {'rgb': [80, 113, 125], 'count': 1}, {'rgb': [77, 111, 129], 'count': 1}, {'rgb': [120, 113, 91], 'count': 1}, {'rgb': [118, 111, 92], 'count': 1}, {'rgb': [90, 115, 118], 'count': 1}, {'rgb': [115, 114, 94], 'count': 2}, {'rgb': [118, 113, 92], 'count': 1}, {'rgb': [119, 112, 92], 'count': 1}, {'rgb': [121, 115, 90], 'count': 1}, {'rgb': [77, 115, 128], 'count': 2}, {'rgb': [126, 176, 196], 'count': 2}, {'rgb': [87, 118, 119], 'count': 1}, {'rgb': [87, 117, 120], 'count': 1}, {'rgb': [86, 116, 121], 'count': 1}, {'rgb': [83, 114, 125], 'count': 1}, {'rgb': [211, 249, 246], 'count': 1}, {'rgb': [158, 210, 223], 'count': 8}, {'rgb': [222, 245, 243], 'count': 1}, {'rgb': [161, 209, 233], 'count': 3}, {'rgb': [162, 204, 223], 'count': 2}, {'rgb': [166, 220, 237], 'count': 5}, {'rgb': [84, 110, 124], 'count': 1}, {'rgb': [220, 246, 245], 'count': 1}, {'rgb': [221, 247, 244], 'count': 1}, {'rgb': [218, 247, 246], 'count': 1}, {'rgb': [167, 220, 234], 'count': 1}, {'rgb': [173, 231, 249], 'count': 1}, {'rgb': [109, 147, 158], 'count': 1}, {'rgb': [89, 114, 121], 'count': 1}, {'rgb': [208, 246, 249], 'count': 1}]

    sorted_colors = sorted(colors, key = lambda i: i['count'],reverse=True)[:10]

    sorted_tuple = []
    for i in sorted_colors:
        sorted_tuple.append((i['rgb'][0], i['rgb'][1], i['rgb'][2]))

    return sorted_tuple

