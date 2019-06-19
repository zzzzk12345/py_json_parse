import json
import csv

jsonstr ="[{'id': 1612059772279, 'name': '2栋', 'short_name': '', 'elevator_count': 0, 'frame_count': 0,\
  'unit_count': 4, 'build_type': '板塔结合', 'build_years': [1998], 'point_lat': 30.664112,\
  'point_lng': 104.103286, 'distance': 7.7905000003441e-08},\
 {'id': 1612061409967, 'name': '4栋', 'short_name': '', 'elevator_count': 0, 'frame_count': 3,\
  'unit_count': 1, 'build_type': '板塔结合', 'build_years': [1998],\
  'point_lat': 30.664486, 'point_lng': 104.103485, 'distance': 1.5232400000095e-07},\
 {'id': 1612059772238, 'name': '1栋', 'short_name': '', 'elevator_count': 0, 'frame_count': 1,\
  'unit_count': 5, 'build_type': '板塔结合', 'build_years': [1998],\
  'point_lat': 30.663895, 'point_lng': 104.103134, 'distance': 2.2944200000445e-07},\
 {'id': 1612361633640965, 'name': '5栋', 'short_name': '', 'elevator_count': 0, 'frame_count': 3,\
  'unit_count': 1, 'build_type': '板楼', 'build_years': [1998],\
  'point_lat': 30.664663, 'point_lng': 104.103165, 'distance': 4.7248100000221e-07},\
 {'id': 1612059772312, 'name': '3栋', 'short_name': '', 'elevator_count': 0, 'frame_count': 2,\
  'unit_count': 2, 'build_type': '板塔结合', 'build_years': [1998],\
  'point_lat': 30.664322, 'point_lng': 104.102788, 'distance': 6.5125299999913e-07}]"

def parsetool(jsonstr,url,city,district,business_district,community_name):
    data_map = json.loads(jsonstr.replace("\'", "\""))
    print(jsonstr.replace("\'", "\""))
    for i in range(len(data_map)):
        data = data_map[i]
        if data:
            print(data["id"],data["name"],data["short_name"],data["elevator_count"],data["frame_count"],data["unit_count"],data["build_type"],data["build_years"][0],data["point_lat"],data["point_lng"],data["distance"])

parsetool(jsonstr,1,2,3,4,5)
