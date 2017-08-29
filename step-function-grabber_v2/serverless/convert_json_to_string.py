import sys
import json

f=open('state-machine.json', 'r')
sys.stdout.write( json.dumps( json.dumps(json.loads(f.read()))))