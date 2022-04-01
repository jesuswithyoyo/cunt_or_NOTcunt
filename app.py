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
text = input("Paste text: ")
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
