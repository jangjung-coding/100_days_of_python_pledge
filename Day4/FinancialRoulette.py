print("Welcome to Financial Roulette!")
friends = ["Alice", "Bob", "charlie", "David", "Emanuel"]

import random
# 랜덤 모듈을 사용해서 정수를 랜덤으로 생성하기(친구 리스트의 길이 만큼)
random_index = random.randint(0, len(friends)-1)
# 인덱싱을 사용해서 랜덤으로 선택된 친구 출력하기
print(friends[random_index] + " is going to pay for the meal today, thank you!")


# Other option
# print(random.choice(friends))