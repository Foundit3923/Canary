import wmi
import os
import subprocess
import time
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
temperature_infos = w.Sensor()
gpu_power = None
gpu_mem_temp = None
first = True

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())
#print(w.Sensor())
#print(temperature_infos)

for sensor in temperature_infos:
    # print(sensor.SensorType)
    if sensor.Name==u'GPU Memory':
        gpu_mem_temp = sensor
    if sensor.Name==u'GPU Total':
        gpu_power = sensor
        #print(sensor.Parent)
        #print(sensor.Name)
        #print(sensor.Identifier)
        #print(sensor.Index)
        #print(sensor.SensorType)
        #print(sensor.Value)
while gpu_power.Value > 0:
      if first == True:
          wait = 10
          while wait > 0:
              print(wait)
              wait = wait - 1
              time.sleep(1)
          first = False
          print("Monitoring GPU Power Usage")
      else:
          temperature_infos = w.Sensor()
          for sensor in temperature_infos:
              if sensor.Name == u'GPU Memory':
                  gpu_mem_temp = sensor
              if sensor.Name == u'GPU Total':
                  gpu_power = sensor
          if process_exists('teamredminer.exe'):
              if gpu_power.Value < 60.0:
                  print(gpu_power.Value)
                  print(gpu_mem_temp.Value * 1000)
                  print('The canary died!')
                  print('Close the mine!')
                  os.system("start cmd.exe /c sendemail.bat")
                  os.system("start cmd.exe /c kill_miner.bat")
                  print('Miner Closed')
                  os.system("start cmd.exe /c start_miner.bat")
                  print('Miner Restarted')
                  first = True

             

