import paho.mqtt.client as paho
import json 

def on_subscribe(client, userdata, mid, granted_qos):
    
    """
    This method is called after one topic subscribed 
    """
   
    print("Subscribed: "+str(mid)+" "+str(granted_qos)) #prints data relented to the  subtribe topic 

def on_message(client, userdata, msg):
    
    """
    method "on_message" is called when ever a new message is arrived to the topic 
    """
    
    print("\nMessage received from the topic -  " + msg.topic + "\n") #prints the topic name from where the message is received

   
    message_string=str(msg.payload.decode("utf-8","ignore")) # converts the message to byte to string 

    message_json=json.loads(message_string) # convert the message to JSON 

   

    print("The payload is \n") #prints the message receive, covert the byte message to string  
    print(message_json)


    check_humidity (message_json) # calls the check_humidity function with argument 


def check_humidity(message_json):
    
    """
    The method "check_humidity" checks the Humidity of the incoming messages, 
    if the Humidity is more than 20 %  then it will  show a alert message,
    other wise prints no warning. 

    """
    
    if message_json["Humidity"] > 20 :

        print("\n!!!!  Alert !!!  Humidity is more than 20% \n")
    else :
        print ("\nHumidity is in normal range \n")
    


def subscribe():
   
    """
    "subscribe" method  creates the client and subscribe to a topic 

    this method also initialise the  "on_subscribe" & "on_message" callbacks, 
    
    start the loop to listen to a subscribed topic 
    """
    client = paho.Client()  # creates the client
    client.on_subscribe = on_subscribe # sets the on_subscribe callback function 
    client.on_message = on_message  # sets the on_message callback function 
    client.connect("broker.mqttdashboard.com", 1883) # connects to the broker 
    client.subscribe("storageDevice/simulator", qos=1) #subcries to a topic 

    client.loop_forever() # runs the loop forever 

if __name__ == "__main__":
    
    subscribe()