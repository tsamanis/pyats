import os

from genie.harness.main import gRun

def main():
     test_path = os.path.dirname(os.path.abspath(__file__))
     gRun(trigger_uids=('TestBgpShutdown'), trigger_datafile='blitz.yml')
