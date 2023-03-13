# 230312

# join()
# 문자 결합 메서드

strings = ["안녕하세요", "개발자가", "꿈인", "취준생입니다."]
print(strings)
print(" ".join(strings))
print("***".join(strings))


# format()
# 위치의 값으로 데이터를 지정
# 만약 숫자를 입력하지 않은 경우 처음부터 차례대로 값을 대입
# !x => x의 형태에 따라 타입을 지정 s:문자열 f:실수 a:아스키코드
print("{0} {1}".format("Hello", "World!"))
print("{0!s} {1!a}".format("Hello", "World!"))
#  target을 지정
print("이름: {who}, 목표:{goal}".format(who="이영재", goal="개발자"))

# ljust(width,fillchar),rjust(width,fillchar)
print("이영재".ljust(50, "-"))
print("project".rjust(50, "*"))

# 문자열 언팩킹 **함수로 전달하기에 적한한 키-값 딕셔너리가 생성(feat locals()-> 해당 지역변수를 딕션어리화 해주는)
name = "이영재"
goal = "개발자"
print("{name}, {goal}".format(**locals()))


# split()
print("이영재입니다.\n취업하고 싶어요\nㅠㅠ".splitlines())
print("이영재입니다.+취업하고 싶어요+ㅠㅠ".split("+"))
print("이영재입니다.+취업하고 싶어요+ㅠㅠ".split("+", 1))
print("이영재입니다.+취업하고 싶어요+ㅠㅠ".rsplit("+", 1))

# strip() -> lstrip(),rstrip()
print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".strip("|||"))
print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".lstrip("|||"))
print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".rstrip("|||"))

# index() ,find()
print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".find("|||"))
print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".index("|||"))
print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".find("***"))
# print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".index("***"))

# count()
print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".count("|||"))
print("|||이영재입니다. ||| 취업하고 ||| 싶어요ㅠㅠ|||".count("|||", 0, 20))