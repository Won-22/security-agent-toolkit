from rbac import check_permission, ROLES, USERS                  # 판정 함수와 역할 · 사용자 정보를 불러온다
from access_log import LOG                                       # access_log.py 의 기록 목록을 불러온다

allowed = 0                                                      # 허용 건수
denied = 0                                                       # 거부 건수
counts = {}                                                      # "사용자 허용" · "사용자 거부" → 건수
used = {}                                                        # 역할 → 실제로 쓴 권한 목록

for log_id, time, user, resource, action in LOG:                 # 기록을 하나씩 꺼낸다
    ok, reason = check_permission(user, resource, action)        # 판정 결과와 이유를 받는다
    if ok:                                                       # 허용이면
        allowed = allowed + 1                                    # 허용 건수를 1 늘리고
        counts[user + " 허용"] = counts.get(user + " 허용", 0) + 1   # 사용자별 허용 건수를 세고
        role = USERS[user]["role"]                               # 그 사용자의 역할을 꺼내고
        if role not in used:                                     # 이 역할이 처음이면
            used[role] = []                                      # 빈 목록을 만든 뒤
        used[role].append(f"{resource}:{action}")                # 쓴 권한을 목록에 더한다
    else:                                                        # 거부면 (쓴 권한으로 모으지 않는다)
        denied = denied + 1                                      # 거부 건수를 1 늘리고
        print("[거부]", log_id, time, user, resource, action, "-", reason)   # 거부된 기록을 출력하고
        counts[user + " 거부"] = counts.get(user + " 거부", 0) + 1   # 사용자별 거부 건수를 센다

# ← 1부: 기록을 하나씩 다시 판정하며 건수와 쓴 권한 모으기
# 1. LOG 에서 (번호, 시각, 사용자, 자원, 행위)를 하나씩 꺼낸다
# 2. check_permission 으로 판정해 ok, reason 으로 나눠 받는다
# 3. ok 이면 allowed 를 1 늘리고, counts 의 "사용자 허용" 을 1 늘리고, 그 사용자의 역할을 role 에 담는다
# 4. 같은 허용 기록에서, used 에 role 이 아직 없으면 used[role] = [] 로 빈 목록을 먼저 만들고,
#    used[role] 목록에 "자원:행위" 글자를 더한다
# 5. 아니면 denied 를 1 늘리고, "[거부]" 와 번호 · 시각 · 사용자 · 자원 · 행위 · 이유를 출력하고,
#    counts 의 "사용자 거부" 를 1 늘린다

print("허용", allowed, "거부", denied)                           # 전체 건수를 출력한다
print(counts)                                                    # 사용자별 건수를 출력한다

for role, permissions in ROLES.items():                          # 역할과 권한 목록을 하나씩 꺼낸다
    for permission in permissions:                               # 권한을 하나씩 꺼내
        if permission not in used.get(role, []):                 # 실제로 쓴 목록에 없으면
            print("쓰이지 않음", role, permission)                 # 쓰이지 않은 권한으로 출력한다

# ← 2부: 쓰이지 않은 권한 출력하기
# 6. ROLES 에서 역할과 권한 목록을 하나씩 꺼낸다
# 7. 그 목록의 권한을 하나씩 꺼내, used.get(역할, []) 에 없으면 "쓰이지 않음", 역할, 권한 을 출력한다

