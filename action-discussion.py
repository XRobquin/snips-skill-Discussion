#!/usr/bin/env python2

from hermes_python.hermes import Hermes

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

INTENT_VOYAGE = "voyage"
INTENT_REACTION = "reaction"

def discussion_voyage(hermes, intent_message):  
  name = intent_message.slots.Proche.first().value
  lieu = intent_message.slots.Lieu.first().value
  action = intent_message.slots.Action.first().value
  sentence = "Fantastique, dites-moi "
  sentence += name
  sentence += " j'ai toujours voulu visiter "
  sentence += lieu
  sentence += " comment etait-ce ?" 
  hermes.publish_continue_session(intent_message.session_id, sentence, [ INTENT_REACTION ])


with Hermes(MQTT_ADDR) as h: 
  h.subscribe_intent(INTENT_VOYAGE, discussion_voyage).start()
