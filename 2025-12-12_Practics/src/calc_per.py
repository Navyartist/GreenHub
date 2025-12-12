def percentage(part, whole):
    """
    두 수가 주어졌을 때 백분율을 계산하는 함수
    
    Args:
        part: 부분 값
        whole: 전체 값
    
    Returns:
        float: 백분율 (%)
    """
    if whole == 0:
        return 0
    return (part / whole) * 100


# 사용 예시
if __name__ == "__main__":
    num1 = 25
    num2 = 100
    result = percentage(num1, num2)
    print(f"{num1}은 {num2}의 {result}%입니다")