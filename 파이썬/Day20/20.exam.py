
# 파이썬에서 SQLite3 연동
"""
< SQLite3 모듈 >
1) 접속 관련 함수
- connect(): SQLite 데이터베이스에 연결
  ex) conn = sqlite3.connect("example.db")
- cursor(): 데이터베이스와 상호작용. cursor 객체는 SQL쿼리를 실행하고, 결과를 가져옴
  ex) cursor = conn.cursor()
- close(): 데이터베이스 연결을 닫음. cursor 객체와 데이터베이스 연결 객체 모두 호출 필요.
  ex) cursor.close()    conn.close()

  
2) 쿼리 전송 관련 함수
- execute(): 지정된 SQL쿼리를 실행
  ex) cursor.execute("SELECT * FROM users WHERE name=?", ('John',))
- executemany(): 같은 SQL 쿼리를 반복적으로 실행
  ex) data = [('John', 30), ('Jane',25)] 
      cursor.executemany("INSERT INTO users (name, age) VALUES(?,?)", data)


3) 쿼리 결과 관련 함수 (select 쿼리 결과를 이용할 때 사용)
- fetchone(): 결과 세트에서 다음 행(row)을 반환
  ex) row = cursor.fetchone()
- fetchmany(): 결과 세트에서 다음 여러개의 행을 가져옴. size 파라미터를 지정하지 않으면
               기본값으로 cursor.arraysize를 사용(default: 1)
               cursor.arraysize = 100 과 같이 변경 가능.
  ex) rows = cursor.fetchmany(5)
- fetchall(): 결과 세트에서 모든 행을 가져옴
  ex) rows = cursor.fetchall()


4) 트랜젝션 관련 함수 (자동 커밋 모드로 동작. 수동으로 begin을 전송하여 직접 트랜젝션 제어 가능)
- commit(): 데이터베이스에 변경 사항을 영구적으로 적용하기 위해서는 반드시 이 함수를 호출.
  ex) conn.commit()
- rollback(): 이전 커밋 시점으로 데이터베이스를 되돌림.
              이 함수를 호출하면, 이전 커밋 이후에 변경된 데이터는 모두 삭제됨.
  ex) conn.rollback()

"""