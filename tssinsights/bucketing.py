from sqlitecallback import SqliteCallback
import re

class Bucketing():
    
    def __init__(self) -> None:
        pass
    
    def analyze(self, sqlitecallback: SqliteCallback):
        sqlitecallback.cursor.execute("SELECT id, miniscript FROM PolicyTrees")
        rows = sqlitecallback.cursor.fetchall()
        
        for row in rows:
            script_id, miniscript = row
            
            if miniscript is None:
                continue
            
            anonymized = re.sub(r'pk\([^)]+\)', 'pk(anon)', miniscript)
            sqlitecallback.cursor.execute(
                "UPDATE PolicyTrees SET anonymized_miniscript = ? WHERE id = ?",
                (anonymized, script_id)
            )
        sqlitecallback.conn.commit()
        
        sqlitecallback.cursor.execute('''
        SELECT GROUP_CONCAT(structure), anonymized_miniscript, COUNT(*) as count, GROUP_CONCAT(miniscript) as miniscripts
        FROM PolicyTrees
        GROUP BY anonymized_miniscript
        HAVING count > 1
        ''')

        clusters = sqlitecallback.cursor.fetchall()
        for cluster in clusters:
            print(f"Common Structure: {cluster[0]}, Count: {cluster[2]}, Miniscripts: {cluster[3]}")



