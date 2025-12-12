
num1 = 1
num2 = 2

def add(a, b):
    result = a + b
    return result

print(add(num1, num2))


def making_sentence(subject, object, verb):
    sentence = f"{subject}는 {object}를 {verb}했다."
    return sentence

print(making_sentence("철수", "사과", "구매"))

def making_HTML(title, body):
    result = f"""
    <htmi>
        "<h1>{title}</h1>
        <p>{body}</p>"
    </htmi>
    """
    print(result)

making_HTML("타이틀", "안녕하세요, 반갑습니다.")