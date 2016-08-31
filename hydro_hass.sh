#!/bin/bash
echo "===================== hass hydrophonic starting ====================="
export HA_TIME_HYSTERESIS_TEMPERATURE="5"
export HA_TIME_HYSTERESIS_HUMIDITY="5"
export HA_TEMPERATURE_FAN_THRESHOLD="40"
export HA_HUMIDITY_FAN_THRESHOLD="40"
export HA_TIME_LAMP_ON_THRESHOLD="19:12:00"
export HA_TIME_LAMP_OFF_THRESHOLD="19:13:05"
hass -c ./

