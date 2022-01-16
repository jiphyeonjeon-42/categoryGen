from pathlib import Path

names = [
    "프로그래밍 언어",
    "웹 프로그래밍",
    "네트워크",
    "모바일 프로그래밍",
    "클라우드",
    "데이터베이스",
    "운영체제-컴퓨터시스템",
    "개발방법론",
    "자료구조-알고리즘",
    "게임",
    "데이터분석-AI-ML",
    "보안-해킹-블록체인",
    "컴퓨터 개론",
    "디자인-그래픽",
    "IT 일반",
    "자격증",
    "비개발",
]

for i, names in enumerate(zip(names, Path().glob("*.png")), start=1):
    new, img = names
    to_change = f"{i:02}.{new}.png"
    print(f"{img} -> {to_change}")
    img.rename(to_change)
