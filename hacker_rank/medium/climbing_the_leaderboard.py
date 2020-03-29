# Alice is playing an arcade game and wants to climb to the top of the leaderboard and wants to track her ranking.

def climbingLeaderboard(scores, alice):
    def sorting(r):
        r.sort(reverse=True)
        return r
    new_scores = list(map(lambda x: scores + [x], alice))
    sort_ranking = list(map(lambda x: sorting(list(set(x))), new_scores))
    rank = list(map(lambda x, y: x.index(y) + 1, sort_ranking, alice))
    return rank

score = [0, 0, 0, 0, 0, 0]
al = [50, 65, 77, 99, 102]
print(climbingLeaderboard(score, al))

def climb_v2(scores, alice):
    def find_uniq(arr):
        new_arr = []
        for i in arr:
            if i in new_arr:
                new_arr
            else:
                new_arr += [i]
        return new_arr
    def sort(arr):
        arr.sort(reverse=True)
        return arr
    score = []
    for i in alice:
        s = sort(find_uniq(scores + [i])).index(i) + 1
        score += [s]
    return score

print(climb_v2(score, al))

def climb_v3(scores, alice):
    score = []
    for i in scores:
        
