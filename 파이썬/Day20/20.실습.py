
# # 파이썬에서 SQLite3 연동

# # 실습 1. Table users 생성
# import sqlite3

# # 데이터베이스 연결 (connect())
# conn = sqlite3.connect("파이썬/Day20/example.db")

# # 커서 생성(cursor())
# cursor = conn.cursor()

# # users 테이블 생성
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL
#     )    
# """)

# # 커밋
# conn.commit()

# # 커서와 연결 닫기
# cursor.close()
# conn.close()



# # 실습 2. execute() 함수
# import sqlite3

# conn = sqlite3.connect("파이썬/Day20/example.db")   # 데이터베이스 연결
# cursor = conn.cursor()      # 커서 생성

# try:
#     # 데이터 삽입
#     cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 20))
#     cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Bob', 25))
#     cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Charlie', 30))
#     conn.commit()         # 커밋
# except Exception as e:
#     conn.rollback()       # 롤백
#     print(e)
# finally:
#     cursor.close()
#     conn.close()



# # 실습 3. executemany() 함수
# import sqlite3

# conn = sqlite3.connect("파이썬/Day20/example.db")
# cursor = conn.cursor()

# # 데이터 삽입을 위한 파라미터 세트
# data = [('John', 30), ('Jane', 25), ('Mike', 40)]

# try:
#     # executemany() 메서드를 사용하여 여러 개의 데이터 삽입
#     cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", data)
#     conn.commit()           
# except Exception as e:
#     conn.rollback()
#     print(e)
# finally:
#     cursor.close()
#     conn.close()



# # 실습 4. fetchone()함수
# import sqlite3

# conn = sqlite3.connect("파이썬/Day20/example.db")
# cursor = conn.cursor()

# try:
#     # users 테이블에서 한 행 가져오기
#     cursor.execute("SELECT * FROM users")
#     row = cursor.fetchone()

#     # 결과 출력
#     if row:
#         print(row)
#     else:
#         print("No data")
# except Exception as e:
#     print(e)
# finally:
#     cursor.close()
#     conn.close()



# # 실습 5. fetchmany() 함수
# import sqlite3

# conn = sqlite3.connect("파이썬/Day20/example.db")
# cursor = conn.cursor()

# try:
#     cursor.execute("SELECT * FROM users")
#     rows = cursor.fetchmany(2)

#     # 결과 출력
#     for row in rows:
#         print(row)
# except Exception as e:
#     print(e)
# finally:
#     cursor.close()
#     conn.close()
    
#                                   fetchmany(size=x) - x줄 읽기


# # 실습 6. fetchall() 함수
# import sqlite3

# conn = sqlite3.connect("파이썬/Day20/example.db")
# cursor = conn.cursor()

# try:
#     cursor.execute("SELECT * FROM users")
#     rows = cursor.fetchall()

#     for row in rows:
#         print(row)
# except Exception as e:
#     print(e)
# finally:
#     cursor.close()
#     conn.close()



# # 실습 7. def 함수 적용
# import sqlite3

# # 데이터베이스 연결
# conn = sqlite3.connect("파이썬/Day20/example.db")

# # cursor 생성
# cursor = conn.cursor()

# # 테이블 생성
# cursor.execute("""DROP TABLE IF EXISTS info""")

# cursor.execute("""
#     CREATE TABLE info (
#     no INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT(20) NOT NULL,
#     age INTEGER CHECK (1 < age AND age < 120),
#     btype TEXT(2),
#     birth TEXT
# );
# """)

# # create 함수
# def create_info(name, age, btype, birth):
#     cursor.execute("INSERT INTO info (name, age, btype, birth) VALUES(?, ?, ?, ?)", (name, age, btype, birth))
#     conn.commit()
#     print("New row added.")

# # read 함수 - 모든 자료
# def read_info():
#     cursor.execute("SELECT * FROM info")
#     return cursor.fetchall()

# # read 함수 - 입력 번호와 일치하는 자료
# def read_info_no(no):
#     cursor.execute("SELECT * FROM info WHERE no = ?", (no,))
#     return cursor.fetchall()

# # read 함수 - 이름과 일치하는 자료 
# def read_info_name(name):
#     cursor.execute("SELECT * FROM info WHERE name = ?", (name,))
#     return cursor.fetchall()

# # update 함수
# def update_info(no, name, age, btype, birth):
#     cursor.execute("UPDATE info SET name=?, age=?, btype=?, birth=? WHERE no=?", (name, age, btype, birth, no))
#     conn.commit()
#     print(f"Row with No = {no} updated.")

# # delete 함수
# def delete_info(no):
#     cursor.execute("DELETE FROM info WHERE no=?", (no,))
#     conn.commit()
#     print(f"Row with No = {no} deleted.")



# # 데이터 추가
# create_info('John', 30, 'A', '1993-01-01')

# # 데이터 조회
# rows = read_info()
# for row in rows:
#     print(row)

# # 데이터 수정
# update_info(1, 'Jane', 25, 'B', '1998-02-01')

# # 수정된 데이터 조회
# print(read_info_name('Jane'))

# # 데이터 삭제
# delete_info(1)

# # 삭제된 데이터 조회
# print(read_info_no(1))

# # cursor, conn 연결 닫기
# cursor.close()
# conn.close()