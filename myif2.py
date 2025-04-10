def print_smiley():
    smiley = [
        "  ^_^  ",
        " (o_o) ",
        " (___) "
    ]
    for line in smiley:
        print(line)

def print_alien():
    alien = [
        "  (•_•) ",
        " ( •_•)>⌐■-■",
        " (⌐■_■) "
    ]
    for line in alien:
        print(line)

def print_ghost():
    ghost = [
        " .-. ",
        "(o o)",
        "| O |",
        "'~~~'"
    ]
    for line in ghost:
        print(line)

def play():
    print("캐릭터 출력 프로그램")
    print("======================")
    print("1. 스마일이")
    print("2. 외계인")
    print("3. 유령")
    print("======================")
    choice = input("선택 (0을 누르면 종료): ")

    if choice == "1":
        print("스마일이 등장!")
        print_smiley()
    elif choice == "2":
        print("외계인 등장!")
        print_alien()
    elif choice == "3":
        print("유령 등장!")
        print_ghost()
    elif choice == "0":
        return False
    else:
        print("잘못된 입력입니다.")
    return True

print("무한 반복 프로그램 시작 (0 입력 시 종료)")
while True:
    if not play():
        break
print("프로그램 종료!")