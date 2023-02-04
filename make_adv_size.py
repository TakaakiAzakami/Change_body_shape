import xml.etree.ElementTree as ET 
import time
import random

tree = ET.parse('ant.xml')

root = tree.getroot()

size_ratio = {}

size_list = {"torso_geom":0.25,"aux_1_geom":0.08,"aux_2_geom":0.08,"aux_3_geom":0.08,"aux_4_geom":0.08
			,"front_left_leg_geom":0.08,"front_right_leg_geom":0.08,"back_left_leg_geom":0.08,"back_right_leg_geom":0.08
			,"front_left_ankle_geom":0.08,"front_right_ankle_geom":0.08,"back_left_ankle_geom":0.08,"back_right_ankle_geom":0.08}

size_epsilon = 0.05

def set_size(epsilon):
	random.seed(time.time())
	r = random.random()	
	ratio = 1.0 - epsilon + r*(epsilon*2)
	return ratio

for geom in root.iter("geom"):
	for name in size_list:
		if name in str(geom.attrib):
			if name in size_list.keys():	
				size_ratio[name] = set_size(size_epsilon)
				geom.set("size",str(size_ratio[name]*size_list[name]))

tree.write('ant.xml',encoding='UTF-8')
