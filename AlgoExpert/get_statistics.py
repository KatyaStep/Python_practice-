def get_statistics(input_list):
    """Mean of the list"""
    n = len(input_list)
    mean_val = sum(input_list) / n

    """Median of the list"""
    input_list.sort()

    if n % 2 == 0:
        median_val = (input_list[(n-1)//2] + input_list[(n+1)//2]) /2
    else:
        median_val = input_list[n//2]

    """Mode of the list"""
    counter_num = {input_list[i]: 0 for i in range(n)}

    for i in range(n):
        counter_num[input_list[i]] += 1

    max_value = max(counter_num.values())
    mode_val = [key for key, value in counter_num.items() if value == max_value]

    """Sample variance of the list"""
    variance_nominator = 0
    for i in range(n):
        variance_nominator += (input_list[i] - mean_val)**2

    variance_denominator = n - 1
    variance_val = variance_nominator / variance_denominator

    """Standard deviation"""
    st_deviation_val = variance_val ** 1/2

    """Mean_confidence_interval"""
    z_score = 1.96
    left_interval = mean_val - (z_score * (st_deviation_val / (n ** 0.5)))
    left_interval = float("{0:.4f}".format(left_interval))

    right_interval = mean_val + (z_score * (st_deviation_val / (n ** 0.5)))
    right_interval = float("{0:.4f}".format(right_interval))

    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val[0],
        "sample_variance": variance_val,
        "sample_standard_deviation": st_deviation_val,
        "mean_confidence_interval": [left_interval, right_interval]
    }


if __name__ == '__main__':
    print(get_statistics([0, 1]))