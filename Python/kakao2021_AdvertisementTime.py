"""
    [문제]
    죠르디의 동영상 재생시간 길이 play_time, 공익광고의 재생시간 길이 adv_time, 시청자들이 해당 동영상을 재생했던 구간 정보 logs가 매개변수로 주어질 때, 시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고를 삽입하려고 합니다. 이때, 공익광고가 들어갈 시작 시각을 구해서 return 하도록 solution 함수를 완성해주세요. 만약, 시청자들의 누적 재생시간이 가장 많은 곳이 여러 곳이라면, 그 중에서 가장 빠른 시작 시각을 return 하도록 합니다.

    [제한사항]
    play_time, adv_time은 길이 8로 고정된 문자열입니다.
    play_time, adv_time은 HH:MM:SS 형식이며, 00:00:01 이상 99:59:59 이하입니다.
    즉, 동영상 재생시간과 공익광고 재생시간은 00시간 00분 01초 이상 99시간 59분 59초 이하입니다.
    공익광고 재생시간은 동영상 재생시간보다 짧거나 같게 주어집니다.
    logs는 크기가 1 이상 300,000 이하인 문자열 배열입니다.

    logs 배열의 각 원소는 시청자의 재생 구간을 나타냅니다.
    logs 배열의 각 원소는 길이가 17로 고정된 문자열입니다.
    logs 배열의 각 원소는 H1:M1:S1-H2:M2:S2 형식입니다.
    H1:M1:S1은 동영상이 시작된 시각, H2:M2:S2는 동영상이 종료된 시각을 나타냅니다.
    H1:M1:S1는 H2:M2:S2보다 1초 이상 이전 시각으로 주어집니다.
    H1:M1:S1와 H2:M2:S2는 play_time 이내의 시각입니다.
    시간을 나타내는 HH, H1, H2의 범위는 00~99, 분을 나타내는 MM, M1, M2의 범위는 00~59, 초를 나타내는 SS, S1, S2의 범위는 00~59까지 사용됩니다. 잘못된 시각은 입력으로 주어지지 않습니다. (예: 04:60:24, 11:12:78, 123:12:45 등)

    return 값의 형식

    공익광고를 삽입할 시각을 HH:MM:SS 형식의 8자리 문자열로 반환합니다.
"""


def str_to_time(str_time):
    return int(str_time[0:2]) * 3600 + int(str_time[3:5]) * 60 + int(str_time[6:8])


def time_to_str(num_time):
    hour = num_time // 3600
    num_time -= 3600 * hour
    minute = num_time // 60
    sec = num_time % 60
    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(sec).zfill(2)


def solution(play_time, adv_time, logs):
    max_t = str_to_time(play_time)
    adv_t = str_to_time(adv_time)
    log_t = []
    for str_log in logs:
        log_t.append((str_to_time(str_log[0:8]), str_to_time(str_log[9:17])))
    weight_t = [0] * max_t
    for t_s, t_e in log_t:
        for i in range(t_s, t_e):
            weight_t[i] += 1
    # use sliding window of size adv_time
    window = 0
    for i in range(adv_t):
        window += weight_t[i]
    ans_v = window
    ans_t = 0
    print("window : " + time_to_str(window))
    for j in range(adv_t, max_t):
        window = window - weight_t[j - adv_t] + weight_t[j]

        if window > ans_v:
            ans_v = window
            ans_t = j - adv_t + 1

    return time_to_str(ans_t)


print(solution("00:30:00", "00:10:00", ["00:00:10-00:10:10"]))
print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
# print(time_to_str(str_to_time("21:54:32")))