#!/usr/bin/python
import os 

for file in os.listdir(os.getcwd()):
    if '.md' in file:
        current = os.path.join(os.getcwd(), file)
        with open(os.path.join(os.getcwd(),'full-research.md'), 'a') as writer:
            with open(current, 'r+') as currBuff:
                buffer = currBuff.read()
                writer.write(buffer)