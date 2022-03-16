import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

class Publisher:
    mqttBroker ="mqtt.eclipseprojects.io" 
    client = mqtt.Client("Temperature_Inside")
    client.connect(mqttBroker) 

    def publish(topic, content):
        client.publish(topic, content)
        print(f"Just published {str(content)} to topic {topic}")
        time.sleep(1)