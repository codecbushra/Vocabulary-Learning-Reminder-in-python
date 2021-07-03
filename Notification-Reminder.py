import time 
from plyer import notification
import random
my_EngDictionary = {'hospitality': 'Mehman nawazi','stumble':'thokarkhana','blasphamous': 'Gustakhana','gratitude':'Shukar guzari','Betray':'dhoka dyna','Morph': 'shakal badalna','Spectacular': 'shandaar','Dorky': 'ahmaq, baywaqoof, bawla','Roll up': 'belna','Organising': 'tarteeb dyna step by step','Check through':'to examine or check that it is correct or not','Back n forth': 'agay peechay, idhr udhr, Bari bari','Slaughter': 'zibaah','Traditional': 'rawayati','Prompt': 'fori Tor per','Enchanting': 'dilfareb','Adorable': 'pyara'}
        
if __name__ == '__main__':
    while True:
 	    notification.notify(
 		    title = "***Vocabulary Learn Reminder***",
 			message = f'{random.choice(list(my_EngDictionary.items()))}',
 			app_icon = "F:/B Python and ML Docs/Vocabulary Learning App in python/reminder.ico",
 			timeout = 12
 			)
 	    time.sleep(6)
