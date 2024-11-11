import subprocess
import queue
from policytree import PolicyTree

class BinaryFeeder:
    """Miniscript process manager."""
    def __init__(self, binary_path: str) -> None:
        self.binary_path = binary_path
        self.process = None 
        self.input_queue = queue.Queue()
        self.running = False

    def start(self) -> None:
        """Start the binary and the feeder thread."""
        self.process = subprocess.Popen(
            [self.binary_path],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        self.running = True

    def feed(self, tree: PolicyTree) -> None:
        """Feed a PolicyTree instance to the binary and wait for the output."""
        self.process.stdin.write(repr(tree) + "\n")
        self.process.stdin.flush()

        output = self.process.stdout.readline().strip()
        
        #Sanitize the output
        if "type=(invalid)" in output:
            tree.miniscript = ""
        else:
            tree.miniscript = output.split(maxsplit=4)[-2]

    def stop(self) -> None:
        """Stop the binary process."""
        self.running = False
        if self.process:
            self.process.terminate()
            self.process.wait()
