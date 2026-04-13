import time
import datetime
from plyer import notification
def notiti():
 if now==t:
  notification.notify(
    title="REMINDER",
    message=n,
    timeout=20
)
print('24 hour format')
print("eg..15:30")
a=(input('enter time....'))
t=a# :{b}
# b=(input('enter minute..'))
n=input('enter message.. ')
while True:
  now=datetime.datetime.now().strftime("%H:%M")
  if now==t:
   notiti()
   break
  time.sleep(1)
     