import csv
from collections import Counter


def Weight():
    print('Weight')
    with open('./data/HeightWeight.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data.pop(0)
        weightData = []
        # mean
        for i in range(len(data)):
            _i = data[i][2]
            weightData.append(float(_i))
        dataLen = len(data)
        sum = 0
        for i in weightData:
            sum += i
        mean = sum/dataLen
        print(f'Mean: {int(mean*100)/100}')

        # median
        weightData.sort()
        idx = len(weightData)//2
        median = 0
        if len(weightData) % 2 == 0:
            _1 = float(weightData[idx])
            _2 = float(weightData[idx-1])
            median = (_1+_2)/2
            pass
        elif len(weightData) % 2 == 1:
            median = weightData[idx]
            pass
        print(f'Median: {int(median*100)/100}')

        # Mode
        _data = Counter(weightData)
        _range = {
            "110-120": 0,
            "120-130": 0,
            "130-140": 0,
            "140-150": 0,
        }
        for i, j in _data.items():
            for item in _range:
                start, end = item.split("-")
                start, end = [int(start), int(end)]
                if start < float(i) < end:
                    _range[item] += j
        _sorted = {k: v for k, v in sorted(
            _range.items(), key=lambda item: item[1])}
        _last = 0
        for key, val in _sorted.items():
            _last = {"key": key, "val": val}
        print(f'Mode: {_last["key"]} , ocurring {_last["val"]} times ')
        # print(_sorted)


def Height():
    print('Height')
    with open('./data/HeightWeight.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        data.pop(0)
        heightData = []
        # mean
        for i in range(len(data)):
            _i = data[i][1]
            heightData.append(float(_i))
        dataLen = len(data)
        sum = 0
        for i in heightData:
            sum += i
        mean = sum/dataLen
        print(f'Mean: {int(mean*100)/100}')

        # median
        heightData.sort()
        idx = len(heightData)//2
        median = 0
        if len(heightData) % 2 == 0:
            _1 = float(heightData[idx])
            _2 = float(heightData[idx-1])
            median = (_1+_2)/2
            pass
        elif len(heightData) % 2 == 1:
            median = heightData[idx]
            pass
        print(f'Median: {int(median*100)/100}')

        # Mode
        _data = Counter(heightData)
        _range = {
            "60-65": 0,
            "65-66": 0,
            "66-67": 0,
            "67-68": 0,
            "68-69": 0,
            "69-70": 0,
            "70-75": 0,
            "75-80": 0,
        }
        for i, j in _data.items():
            for item in _range:
                start, end = item.split("-")
                start, end = [int(start), int(end)]
                if start < float(i) < end:
                    _range[item] += j
        _sorted = {k: v for k, v in sorted(
            _range.items(), key=lambda item: item[1])}
        _last = 0
        for key, val in _sorted.items():
            _last = {"key": key, "val": val}

        # for i,j in
        print(
            f'Mode: {_last["key"]} , ocurring {_last["val"]} times')


Height()
Weight()
