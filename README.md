#Automatization of hydroponic system

Use for **virtualenv** in home-assistant  
Run hass by script **hydro_hass.sh**. This script contains all constant and threshold used in automation.  
- HA_TEMPERATURE_FAN_THRESHOLD - If temperature is higher then fan is turn on
- HA_HUMIDITY_FAN_THRESHOLD - If humidity is higher then fan is turn on
- HA_TIME_HYSTERESIS_TEMPERATURE - Hysteresis for temperature. Value of temperature needs to be above some threshold for this time to trigger automatization.
- HA_TIME_HYSTERESIS_HUMIDITY - Hysteresis for humidity. Value of humidity needs to be above some threshold for this time to trigger automatization.
- HA_TIME_LAMP_ON_THRESHOLD - Time when lamp should turn on
- HA_TIME_LAMP_OFF_THRESHOLD - Time when lamp should turn off

##Actuators
- Lamp
- Fan

##Sensors
- Temperature
- Humidity

