import sqlite3
# 실습 8)
# 하나의 Row를 표현하기 위한 클래스
# VO (Value Object): 값을 표현하는 클래스
# DTO (Data Transfer OBject): 레이어 간 데이터 전송을 위해 정의하는 클래스

class InfoVO:
    def __init__ (self, no=None, name=None, age=None, btype=None, birth=None):
        self.no = no
        self.name = name
        self.age = age
        self.btype = btype
        self.birth = birth

    def __str__ (self):
        return f"InfoVO (no = {self.no}, name = {self.name}, age = {self.age}, btype = {self.btype}, birth = {self.birth})"
    

# DAO (Data Access Object): 데이터베이스에 접근하여 조작하는 기능을 정의한 클래스

class InfoDAO:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def create(self, vo):
        self.cursor.execute("INSERT INTO info (name, age, btype, birth) VALUES (?, ?, ?, ?)", (vo.name, vo.age, vo.btype, vo.birth))
        self.conn.commit()
        print("New row added.")

    def read_all(self):
        self.cursor.execute("SELECT * FROM info")
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            vo = InfoVO(*row)
            result.append(vo)
        return result

    def read_by_no(self, no):
        self.cursor.execute("SELECT * FROM info WHERE no=?", (no,))
        row = self.cursor.fetchone()
        if row:
            vo = InfoVO(*row)
            return vo
        else:
            return None
    
    def read_by_name(self, name):
        self.cursor.execute("SELECT * FROM info WHERE name=?", (name,))
        rows = self.cursor.fetchall()
        result = []
        for row in rows:
            vo = InfoVO(*row)
            result.append(vo)
        return result
            
    def update(self, vo):
        self.cursor.execute("UPDATE info SET name=?, age=?, btype=?, birth=?", (vo.name, vo.age, vo.btype, vo.birth))
        self.conn.commit()
        print(f"Row with No = {vo.no} updated.")

    def delete(self, no):
        self.cursor.execute("DELETE FROM info WHERE no=?", (no,))
        self.conn.commit()
        print(f"Row with No = {no} deleted.")


# 데이터베이스 연결
conn = sqlite3.connect("파이썬/Day20/example.db")

# cursor 생성
cursor = conn.cursor()

# 테이블 생성
cursor.execute("""DROP TABLE IF EXISTS info""")

cursor.execute("""
    CREATE TABLE info(
    no INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(20) NOT NULL,
    age INTEGER CHECK (1 < age AND age < 120),
    btype TEXT(2),
    birth TEXT
);
""")


dao = InfoDAO(conn)

# 데이터 추가
dao.create(InfoVO(1, 'John', 30, 'A', '1993-01-01'))

# 데이터 조회
rows = dao.read_all()
for row in rows:
    print(row)

# 데이터 수정
dao.update(InfoVO(1, 'Jane', 25, 'B', '1998-02-01'))

# 수정된 데이터 조회
rows = dao.read_by_name('Jane')
for row in rows:
    print(row)

# 데이터 삭제
dao.delete(1)

# 삭제된 데이터 조회
print(dao.read_by_no(1))


cursor.close()
conn.close()




