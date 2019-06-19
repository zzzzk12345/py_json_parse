import mysql.connector
import json
import csv
import os


class JsonParse():

    def __init__(self):
        # 连接数据库
        self.mydb = mysql.connector.connect(
            host="rr-2zetk6oj0m9p6g95j.mysql.rds.aliyuncs.com",
            user="zhuchenxiao",
            passwd="HPFbLZsQZ9MRr1dT92NH",
            database="Monitor"
        )
        print("数据库连接成功！")
        self.mycursor = self.mydb.cursor()

        self.mycursor.execute("SELECT url,city,district,business_district,community_name,building_distribution FROM archive_lianjia_xiaoqu WHERE SUBSTRING(date_created,1,10)='2019-05-06'")

    def __del__(self):
        if self.mydb:
            self.mydb.close()

    def getTitle(self):
        tb_title = ['id','url', 'city', 'district', 'business_district', 'community_name','building_id','name','short_name','elevator_count','frame_count','unit_count','build_type','build_years','point_lat','point_lng','distance']
        return tb_title

    def getResult(self):
        res = self.mycursor.fetchall()
        print("数据量：",len(res))
        return res

    def parsetool(self,url,city,district,business_district,community_name,jsonstr):
        rows = []
        data_map = json.loads(jsonstr.replace("\'", "\""))
        for i in range(len(data_map)):
            data = data_map[i]
            if data:
                rows.append([id,url,city,district,business_district,community_name,str(data["building_id"]),data["name"],\
                             data["short_name"],data["elevator_count"],data["frame_count"],data["unit_count"],\
                             data["build_type"],data["build_years"][0] if data["build_years"] else '',data["point_lat"],data["point_lng"],str(data["distance"])])
        return rows

if __name__ == "__main__":
    jp = JsonParse()
    if os.path.exists('../archeive_lianjie_xiaoqu_20190506.csv'):
        os.remove('../archeive_lianjie_xiaoqu_20190506.csv')
    with open('../archeive_lianjie_xiaoqu_20190506.csv','w',encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(jp.getTitle()) # 写入字段名
        for lst in jp.getResult(): # 遍历每个元素
            if lst[-1]:
                rows = jp.parsetool(*lst)
                # print(rows)
                if rows:
                    writer.writerows(rows)
                    # print(rows)
    print('csv写入完成！')
