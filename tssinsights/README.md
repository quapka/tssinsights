# Grammarinator
Install the expect package and grammarinator or use the provided venv
```bash
pip install grammarinator
apt install expect
```
Process the grammar and generate the outputs (make sure the output folder is in the PYTHONPATH environment variable)
```bash
mkdir -p grammarinator_output; export PYTHONPATH=$(pwd)/grammarinator_output
grammarinator-process adjusted.g4 -o ./grammarinator_output --no-action
unbuffer grammarinator-generate ThresholdPolicyGenerator.ThresholdPolicyGenerator -n 10000 --stdout -d 10 > output.txt
```
10k in 6 sec
100k in 6 mins
200k in 14 mins
300k in 23 mins

214k in 13354s = 3.7h