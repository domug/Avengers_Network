from utils import *

def Main():
    """메인 모델"""
    run = True
    while run:
        Utils.Borderline()
        print("안녕하세요 DSL 마블 네트워크 프로젝트 입니다.")
        print("어떤 것을 확인하시겠습니까?")
        print("1. 인물별로 보기")
        print("2. 시리즈별로 보기")
        print("3. 종료하기")
        menu = input(":")
        while menu not in ["1", "2", "3"]:
            print("잘못된 입력입니다.")
            choice = input(":")

        Utils.Borderline()

        # 캐릭터별 분석
        if menu == "1":
            name = input("인물의 이름을 입력해주세요 (영어, 띄어쓰기 구분 O, 대소문자 구분 X): ").upper()
            character = Utils.name_check(name)
            while character == "unmatch":
                name = input("인물의 이름을 입력해주세요 (영어, 띄어쓰기 구분 O, 대소문자 구분 X): ").upper()
                character = Utils.name_check(name)

            menu = Analysis_byCharacter(character).script()

        # 시리즈별 분석
        elif menu == "2":
            series_no = input("확인하실 어벤져스 시리즈 번호를 입력해주세요 (1~4): ")
            while series_no not in ["1", "2", "3", "4"]:
                print("잘못된 입력입니다. 1~4 중 하나를 선택해주세요.")
                series_no = input("확인하실 시리즈 번호를 입력해주세요 (1~4): ")

            menu = Analysis_bySeries(series_no).script()


        elif menu == "3":
            print("모델을 종료합니다.")
            run = False

        else:
            print("잘못된 입력입니다.")







########################################################################################################
########################################################################################################

Main()