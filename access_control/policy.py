from rbac import check_permission                                # 어제 만든 역할 판정 함수를 불러온다
from exception_policy import find_exception                      # 3교시에 만든 예외 판정 함수를 불러온다


def evaluate_access(user, resource, action, now):                # 사용자 · 자원 · 행위 · 지금 시각을 받는 함수
    """(허용 여부, 이유)를 리턴한다. 역할 권한 → 유효한 예외 → 거부 순서로 본다."""
    # ← 아래를 직접 씁니다 (주석은 두고 각 주석 바로 아래 줄에 씁니다)
    # 1. check_permission 으로 판정해 ok, reason 으로 나눠 받는다
    ok, reason = check_permission(user, resource, action)
    if ok:
        return True, "역할 권한"
    # 2. ok 이면 True, "역할 권한" 을 리턴한다
    if reason != "권한 없음":
        return False, reason
    found, exc_id = find_exception(user, f"{resource}:{action}", now)
    if found:
        return True, f"예외 {exc_id}번"
    return False, "권한 없음"
    # 3. reason 이 "권한 없음" 이 아니면 False 와 그 reason 을 그대로 리턴한다
    # 4. find_exception 에 user, "자원:행위" 글자(f"{resource}:{action}"), now 를 넣어 found, exc_id 로 나눠 받는다
    # 5. found 이면 True, f"예외 {exc_id}번" 을 리턴한다
    # 6. 여기까지 왔으면 False, "권한 없음" 을 리턴한다

