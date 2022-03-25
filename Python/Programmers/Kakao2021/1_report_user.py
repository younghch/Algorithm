'''
https://programmers.co.kr/learn/courses/30/lessons/92334
'''
from collections import defaultdict

def solution(id_list, report, k):
    abuser_reporters = defaultdict(set)
    mail_counts = defaultdict(int)
    
    for log in report:
        reporter, abuser = log.split()
        abuser_reporters[abuser].add(reporter)
        
    for reporters in abuser_reporters.values():
        if len(reporters) >= k:
            for reporter in reporters:
                mail_counts[reporter] += 1
    return list(map(lambda x: mail_counts[x], id_list))
