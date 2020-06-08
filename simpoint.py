import os, time, sys, json

with open('configure_auto.json', 'r', encoding = 'utf-8') as f:
    json_data = json.load(f)

simpoint_interval = json_data['simpoint-interval']
maxK = json_data['maxK']
warmup = json_data['warmup']
path = json_data['path']
name = json_data['name']

simpoint_cmd = path + 'gem5_auto/SimPoint.3.2/bin/simpoint -loadFVFile ' + path + 'simpoint.bb -maxK ' + str(maxK) + ' -saveSimpoints ' + path + name + '.simpoints -saveSimpointWeights ' + path + name + '.weights'

print('simpoint_cmd : '+ simpoint_cmd)
input_user = input("Whether to contiune? [y/n] : ")
if input_user == 'y':
    os.system(simpoint_cmd)


