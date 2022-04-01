from requests import get
import cgi
from transformers import pipeline
import torch
import torch.nn.functional as F




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
print("text = : ", text)
print("")
print("THIS TEXT HAS BEEN SUMBITTED FOR JUDGEMENT")


model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
classifier = pipeline('sentiment-analysis', model=model_name)

results = classifier([(text)])

for results in results:
    print(results)
