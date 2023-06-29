
# 실습 (개인 프로젝트)
# 설문조사 애플리케이션 만들어 보기
# 데이터베이스 연동 필수, 완성 후 설계내용 및 소스코드 강사 이메일 제출

import sqlite3
import os

def create_table():

    conn = sqlite3.connect("파이썬/Day21,22,23/project2.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS favorite")

    cursor.execute("""
        CREATE TABLE favorite(
        no INTEGER PRIMARY KEY AUTOINCREMENT,
        typename TEXT NOT NULL,
        vote INTEGER 
        )
    """)

    foods = [("한식", 0), ("중식", 0), ("일식", 0), ("양식", 0)]

    try:
        cursor.executemany("INSERT INTO favorite (typename, vote) VALUES(?, ?)", foods)
        conn.commit()

    except Exception as e:
        conn.rollback()
        print(e)
    
    finally:
        cursor.close()
        conn.close()


def start_vote():

    while True:
        print()
        print("★ 좋아하는 음식 종류 설문조사 ★")
        print("="*30)
        print("1. 설문 참여하기")
        print("2. 설문 현황보기")
        print("3. 설문 종료")
        print("="*30)

        conn = sqlite3.connect("파이썬/Day21,22,23/project2.db")
        cursor = conn.cursor()
        
        choice = input("선택: ")

        if choice == "1":
            print("─"*17)
            cursor.execute("SELECT * FROM favorite")
            rows = cursor.fetchall()

            for row in rows:
                print(f"{row[0]}. {row[1]}")
            print("0. 기타(직접입력)")
            print("─"*17)

            try:
                menu = int(input("선택: "))

                if menu == rows[menu-1][0]:
                    cursor.execute(f"UPDATE favorite SET vote = vote + 1 WHERE no = {menu}")

                elif menu == 0:
                    food = input("음식 종류 입력: ")
                    cursor.execute("INSERT INTO favorite (typename, vote) VALUES(?, ?)", (food, 1))
                conn.commit()

            except Exception as e:
                conn.rollback()
                print(e)

            finally: 
                print("설문 완료")

        elif choice == "2":
            try:
                print("┌────────────────────────────────┐")
                cursor.execute("SELECT * FROM favorite")
                rows = cursor.fetchall()

                for row in rows:
                    if len(row[1]) > 4 :
                        print(f"│ {row[0]}. {row[1]} ===> {row[2]}표\t │")
                    else:
                        print(f"│ {row[0]}. {row[1]} ===> {row[2]}표\t\t │")
                print("└────────────────────────────────┘")
            except Exception as e:
                print(e)

        elif choice == "3":
            print("설문 종료")
            break

        else:
            print("선택 오류!! (1 또는 2를 입력하세요.)")

        cursor.close()
        conn.close()

        input("\n\n[MENU]")
        os.system("cls")



# create_table()
start_vote()