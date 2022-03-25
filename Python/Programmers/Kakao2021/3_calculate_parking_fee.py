'''
https://programmers.co.kr/learn/courses/30/lessons/92341
'''
from collections import defaultdict

def solution(fees, records):
    basic_time, basic_fee, unit, fee_per_unit = fees
    in_out_log = defaultdict(list)
    ans = []
    
    for record in records:
        time_log, car_no, _ = record.split()
        in_out_log[car_no].append(time_log)
    
    for car_no in sorted(in_out_log.keys()):
        in_outs = in_out_log[car_no]
        time = 0
        
        if len(in_outs)%2 != 0:
            in_outs.append('23:59')
        for i in range(0, len(in_outs), 2):
            time += time_diff_in_min(in_outs[i], in_outs[i+1])
        ans.append(calculate_fee(time, basic_time, basic_fee, unit, fee_per_unit))
        
    return ans

def calculate_fee(time, basic_time, basic_fee, unit, fee_per_unit):
    if time <= basic_time:
        return basic_fee
    else:
        exceed_time = time-basic_time
        up = 0 if (exceed_time)%unit == 0 else 1
        exceed_fee = fee_per_unit*(exceed_time//unit+up)
        return basic_fee+exceed_fee
        
def time_diff_in_min(in_, out):
    in_time = map(int, in_.split(':'))
    out_time = map(int, out.split(':'))
    return (next(out_time)-next(in_time))*60+next(out_time)-next(in_time)