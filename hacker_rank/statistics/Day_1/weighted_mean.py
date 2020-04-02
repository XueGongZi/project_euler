def weighted_mean(data):
    input_data = data[1]
    weight = data[2]
    sum_weighted_input = sum(list(map(lambda x, y: x * y, input_data, weight)))
    sum_weight = sum(weight)
    return round(sum_weighted_input / sum_weight, 1)

if __name__ == '__main__':

    arr = []

    for _ in range(3):
        arr.append(list(map(int, input().rstrip().split())))

    print(weighted_mean(arr))
