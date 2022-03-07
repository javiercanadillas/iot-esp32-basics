from sht3x import SHT3x

sht3x_sensor = SHT3x(freq=400000, sdapin=21, sclpin=22)
measure_data = sht3x_sensor.read_temp_humd()
# measure_data = [22.9759, 73.8277]
# The default decimal place is 4 digits
temp = measure_data[0]
humd = measure_data[1]

print('Temp:', temp)
# Temp: 22.9759
print('Humd:', humd)
# Humd: 73.8277
