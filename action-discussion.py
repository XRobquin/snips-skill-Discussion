#!/usr/bin/env python2

from hermes_python.hermes import Hermes

INTENT_START_QUIZ = "start_lesson"
INTENT_ANSWER = "give_answer"
INTENT_INTERRUPT = "interrupt"
INTENT_DOES_NOT_KNOW = "does_not_know"

def user_request_quiz(hermes, intent_message):     
  sentence = "What is 5 times 9 ?"    
  print("User is asking for a quiz")    
  hermes.publish_continue_session(intent_message.session_id, sentence, [ INTENT_ANSWER, INTENT_INTERRUPT, INTENT_DOES_NOT_KNOW ])


with Hermes(MQTT_ADDR) as h: h.subscribe_intent(INTENT_START_QUIZ, user_request_quiz)
