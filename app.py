#!/bin/python3.9
#
# __Cunt OR Not Cunt__ by DumbNerd
#
# Copy test from anywhere.
#       eg.Your frends fb posts.
# Paste into this app.
# Wait for processing and judgement.
# Results display Cunt or Not Cunt
#   and a % percentage rating of 
#   their cuntness.

from requests import get
from transformers import pipeline
import torch.nn.functional as F
import time
import sys


print("                    )              )   (         )     )                            )          ")
print("     (           ( /(   *   )   ( /(   )\ )   ( /(  ( /(   *   )     (           ( /(   *   )  ")
print("     )\      (   )\())` )  /(   )\()) (()/(   )\()) )\())` )  /(     )\      (   )\())` )  /(  ")
print("   (((_)     )\ ((_)\  ( )(_)) ((_)\   /(_)) ((_)\ ((_)\  ( )(_))  (((_)     )\ ((_)\  ( )(_)) ")
print("   )\___  _ ((_) _((_)(_(_())    ((_) (_))    _((_)  ((_)(_(_())   )\___  _ ((_) _((_)(_(_())  ")
print("  ((/ __|| | | || \| ||_   _|   / _ \ | _ \  | \| | / _ \|_   _|  ((/ __|| | | || \| ||_   _|  ")
print("   | (__ | |_| || .` |  | |    | (_) ||   /  | .` || (_) | | |     | (__ | |_| || .` |  | |    ")
print("    \___| \___/ |_|\_|  |_|     \___/ |_|_\  |_|\_| \___/  |_|      \___| \___/ |_|\_|  |_|    ")
print("")                                                                                              
print("")
print("Note: you may need to reformat your text to remove multi lines. only 3 inputs allowed. ")
inputtext1 = input("Paste text {1 of 3} : ")
inputtext2 = input("Paste more {2 of 3} : ")
inputtext3 = input("Paste even more {3 of 3} : ")

textgroup = (str(inputtext1), str(inputtext2), str(inputtext3))

text=''.join(textgroup)

print("")
print("Text recived = : ", text)
print("")

print("YOUR TEXT HAS BEEN SUMBITTED FOR JUDGEMENT")    
animation = "|/-\\"

#animation code for spinny thing
for i in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("Still Processing...")
print("watch the spinny thing.")
for w in range(10):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()  
print("Still Processing.... Give me 1 second.")

animation2 = "|/-\\"

for t in range(100):
    time.sleep(0.1)
    sys.stdout.write("\r" + animation2[t % len(animation2)])
    sys.stdout.flush()  


#AI Send 
model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
classifier = pipeline('sentiment-analysis', model=model_name)

#AI Results
results = classifier([(text)])

for results in results:
    #print(results)
    results=results

for value in results.values():
	#print(value)
    value=value

perc = (value)
#print('{:,.2%}'.format(x))

la = results.get('label')

if (la == 'POSITIVE'):
    print("")
    print("")
    print("        )     )                            )      ")  
    print(" ( /(  ( /(   *   )     (           ( /(   *   )  ")
    print(" )\()) )\())` )  /(     )\      (   )\())` )  /(  ")
    print("((_)\ ((_)\  ( )(_))  (((_)     )\ ((_)\  ( )(_)) ")
    print(" _((_)  ((_)(_(_())   )\___  _ ((_) _((_)(_(_())  ")
    print("| \| | / _ \|_   _|  ((/ __|| | | || \| ||_   _|  ")
    print("| .` || (_) | | |     | (__ | |_| || .` |  | |    ")
    print("|_|\_| \___/  |_|      \___| \___/ |_|\_|  |_|    ")
    print("                                                  ")
    print('{:,.2%}'.format(perc) + "  NOT A CUNT")
    #print("NOT A CUNT")
else:
    print("")
    print("")
    print("                  )          ")
    print("   (           ( /(   *   )  ")
    print("   )\      (   )\())` )  /(  ")
    print(" (((_)     )\ ((_)\  ( )(_)) ")
    print(" )\___  _ ((_) _((_)(_(_())  ")
    print("((/ __|| | | || \| ||_   _|  ")
    print(" | (__ | |_| || .` |  | |    ")
    print("  \___| \___/ |_|\_|  |_|    ")
    print("                             ")
    print('{:,.2%}'.format(perc) + "  IS A CUNT")

print("")
print("")
print("= DumbNerd.net")
print("")
