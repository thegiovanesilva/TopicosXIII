import paho.mqtt.client as mqtt
import time

class Subscriber:
  def on_message(client, userdata, message):
      print("received message: " ,str(message.payload.decode("utf-8")))

  mqttBroker ="mqtt.eclipseprojects.io"

  client = mqtt.Client("Smartphone")
  def subscribe():
    client.connect(mqttBroker) 

    client.loop_start()

    client.subscribe("TEMPERATURE")
    client.on_message=on_message 

    client.loop_stop()