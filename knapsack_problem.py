import numpy as np

stereo = {
    'weight': 4,
    'value' : 3000 
}

laptop = {
    'weight': 3,
    'value' : 2000 
}

guitar = {
    'weight': 1,
    'value' : 1500 
}

iphone = {
    'weight': 1,
    'value' : 2000 
}

goods = [guitar, stereo, laptop, iphone]


def knapsack(goods):
    ratio = 1
    for i in range(len(goods)):
        if goods[i]['weight'] < 1:
            ratio = 1//goods[i]['weight']
    max_weight = int(ratio * max(weight['weight'] for weight in goods))

    table = np.zeros((len(goods), int(ratio*(max_weight)+1)))

    for good_idx in range(0, len(goods)):
        for w in range(0, int(ratio * max_weight+1)):
            if ratio*goods[good_idx]['weight'] <= w:

                table [good_idx, w] = max(table[good_idx-1, w], goods[good_idx]['value'] + table [good_idx-1][int(w - ratio*goods[good_idx]['weight'])])
            else:
                table[good_idx, w] = table[good_idx-1, w]

    print(table)

knapsack(goods)

colosseo = {
    'weight': 0.5,
    'value' : 9 
}

duomo = {
    'weight': 0.5,
    'value' : 6 
}

porta_palazzo = {
    'weight': 1,
    'value' : 1 
}

monza = {
    'weight': 1.5,
    'value' : 10 
}

monuments = [colosseo, duomo, porta_palazzo, monza]

knapsack(monuments)
