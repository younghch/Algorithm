'''
https://programmers.co.kr/learn/courses/30/lessons/92342
'''
def solution(n, info):
    arrow_to_score = list(map(lambda x: x+1, info))
    arrow_left = n
    score_diff = -float('inf')

    ryan_arrows = [False]*11
    best_ryan_arrows = []

    def calculate_diff():
        score_apache = 0
        score_ryan = 0
        for i in range(10):
            if ryan_arrows[i]:
                score_ryan += 10-i
            elif info[i]:
                score_apache += 10-i
        return score_ryan-score_apache
    
    def back_track_recusive(score):
        nonlocal arrow_left
        nonlocal score_diff
        nonlocal best_ryan_arrows

        if score == 0 or arrow_left == 0:
            diff = calculate_diff()
            if diff >= score_diff:
                score_diff = diff
                best_ryan_arrows = ryan_arrows[::]
            return
        
        idx = 10-score
        arrow_needed = arrow_to_score[idx]
        if arrow_left < arrow_needed:
            back_track_recusive(score-1)
        else:
            arrow_left -= arrow_needed
            ryan_arrows[idx] = True
            back_track_recusive(score-1)

            arrow_left += arrow_needed
            ryan_arrows[idx] = False
            back_track_recusive(score-1)
    
    def get_ans():
        nonlocal score_diff

        if score_diff <= 0:         
            return [-1]
        else:
            ans = list(map(lambda x: arrow_to_score[x[0]] if x[1] else 0, enumerate(best_ryan_arrows)))
            if sum(ans) != n:
                ans[-1] += n-sum(ans)
            return ans

    back_track_recusive(10)
    return get_ans()