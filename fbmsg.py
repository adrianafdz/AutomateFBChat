print("Wainting")
# Mensajes que estaré mandando
MENSAJES = [
	"Goodnight baby",
	"See you tomorrow",
	"K bamos a comer mañana"
]

# Libraries
import fbchat 
from getpass import getpass 
import schedule 
import time
import random


def send_message(lista):
	# mi username y pass
	username = "adriana.fernandezlopez.1"
	paswd = "ideaPad1197!$("

	# selecciona mensaje al azar
	sel_msg = lista[random.randint(0, len(MENSAJES)-1)]

	# log in
	client = fbchat.Client(username, paswd)

	# uid de Ramiro
	# que saqué del url de su conversacion
	rami_uid="100009879074235"

	sent = client.sendMessage(sel_msg, thread_id=rami_uid)

	if sent: 
		print("Message sent successfully!")


	# a cuantas personas le quiero manfar mensaje
	# no_of_friends = int(input("Number of friends: ")) 
	# for i in range(no_of_friends): 
	#     name = str(input("Name: ")) 
	#     friends = client.searchForUsers(name)  # return a list of names 
	#     friend = friends[0] 
	#     msg = input("Message: ")
	#     print(friend.uid)
	#     sent = client.sendMessage(msg, thread_id=friend.uid)
	#     #sent = client.send(msg, friend.uid) 
	#     #client.send(Message(text=msg), thread_id=friend.uid, thread_type=ThreadType.USER)
	#     if sent: 
	#         print("Message sent successfully!")


	client.logout()

	schedule.clear()


# SCHEDULE
schedule.every().day.at("01:00").do(send_message, MENSAJES)


while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(60)