# Threshold Signature Schemes Analysis tool

## Introduction
This experiment consists of two main parts:
- Generator
- - Brute-force, or
- - TODO smart generation
- Analyzer
- - Export to csv
- - Export to stdin
- - TODO graphical report

Each can be used as separate API calls or run consecutively as shown in full_experiment.py.

## Installation
Works on UNIX systems only. Make sure you have g++, make and cargo installed. To build the project and it's modules, use
```bash
git clone --recursive https://github.com/mseckar/tssinsights
cd tssinsights; make -C miniscript; chmod +x miniscript/miniscript
```

## Usage
To run the full experiment, use
```bash
python tssinsights/full_experiment.py <roles> <depth> <width>
ex.
python tssinsights/full_experiment.py 3 3 2
```
