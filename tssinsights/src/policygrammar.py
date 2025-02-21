
import subprocess
import sqlite3
import queue
import os
from bucketing import Bucketing
import cProfile
import time

class PolicyGrammar():
    def __init__(self, samples: int, depth: int) -> None:
        self.binary_path = "./../miniscript/miniscript"
        self.process = None 
        self.input_queue = queue.Queue()
        self.running = False
        
        self.conn = sqlite3.connect("policy(3,3,3).db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS PolicyTrees (
            id INTEGER PRIMARY KEY,
            structure TEXT,
            miniscript TEXT,
            anonymized_miniscript TEXT
        )
        ''')
        self.conn.commit()
        self.grammarinator_generate = f"unbuffer grammarinator-generate ThresholdPolicyGenerator.ThresholdPolicyGenerator -n {samples} --stdout -d {depth} | ../miniscript/miniscript"

#    def generatePolicyTrees(self, depth: int, width: int, compile_callback: BinaryFeeder, store_callback: SqliteCallback):
    def generatePolicyTrees(self):
        # TODO: Generate the ANTLR file based on the input parameters
        # Placeholder: use the prewritten file
        prepare_env = "mkdir -p grammarinator_output"
        grammarinator_process = "grammarinator-process adjusted.g4 -o ./grammarinator_output --no-action"
        try:
            subprocess.run(prepare_env, shell=True, stderr=subprocess.STDOUT)
            
            # Set PYTHONPATH
            os.environ["PYTHONPATH"] = os.path.join(os.getcwd(), "grammarinator_output")
            result = subprocess.check_output("echo $PYTHONPATH", shell=True, stderr=subprocess.STDOUT)
            print(result.decode('utf-8'))
            result = subprocess.check_output(grammarinator_process, shell=True, stderr=subprocess.STDOUT)
            print(result.decode('utf-8'))
            print("Environment prepared successufully")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e.output.decode('utf-8')}")
                       
        
    def populateDB(self):
        print("Compiler process has started")
        #self.cursor.execute("PRAGMA synchronous = OFF;")
        #self.cursor.execute("PRAGMA journal_mode = MEMORY;")
        #self.cursor.execute("BEGIN TRANSACTION;")
        proc = subprocess.Popen(
            (self.grammarinator_generate),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            shell=True
        )

        for line in proc.stdout: # type: ignore
            if line.startswith("X"):
                policy = line.split()[-1]
                miniscript = line.split()[-2]
            else:
                policy = line.split()[-1][11:] # cut miniscript=
                miniscript = ""
            
            self.cursor.execute('''
            INSERT OR IGNORE INTO PolicyTrees (structure, miniscript) VALUES (?, ?)
            ''', (policy, miniscript))
            self.conn.commit()

        proc.stdout.close() # type: ignore
        #proc.wait()
        #self.conn.commit()
 #       self.conn.close()

        
if __name__ == "__main__":
    grammar = PolicyGrammar(300000, 15)
    #grammar.generatePolicyTrees()
    start_time = time.time()
    grammar.populateDB()
    print(f"DB Population took {time.time() - start_time}")
    #grammar.populateDB()
    bucketing_worker = Bucketing()
    buckets = bucketing_worker.analyze(grammar)
    bucketing_worker.export_to_csv(buckets, f"../exports/new_report(3.3.3).csv")
    grammar.conn.close()
    