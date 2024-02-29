import sqlite3

class db_handler:
    def __init__(self, db_file_path : str) -> None:        
        try:
            self.conn = sqlite3.connect(db_file_path)
            self.cur = self.conn.cursor()
        except:
            print("can not open db file")
            exit(-1)
    
    def execute_sql(self, query : str):
        try:
            return self.cur.execute(query)            
        except:
            print("can not execute sql query")
            self.conn.close()
            exit(-1)

    def execute_sql_commit(self, query : str):
        try:
            self.cur.execute(query)
            self.conn.commit()
            return
        except:
            print("can not execute sql query")
            self.conn.close()
            exit(-1)


if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    test = db_handler('./target/echo_db')
    output = test.execute_sql("select * from echo_events;")