# Tip Calculator
print("Welcome to the tip calculator.")
# 전체 금액 입력
total = input("What was the total bill? $ ")
# 팁 금액 입력
tip = input("How much tip would you like to give? 10, 12, or 15? ")
# 인원 수 입력
people = input("How many people to split the bill? ")
# 최종 계산
result = (float(total)+float(tip))/int(people)
print(f"Each person should pay: ${round(result, 2)}")