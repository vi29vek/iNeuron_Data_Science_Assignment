import mysql.connector as connector
from flask import Flask, request, jsonify

conn = connector.connect(host='localhost',user='root',password='vsingh')
cursor = conn.cursor(buffered=True)
# cursor.execute("show databases")

cursor.execute("use assignment")
cursor.execute("""
    create table CRUDUsingFlask(
        Customer_Name varchar(50) NOT NULL,
        Due varchar(5),
        PhoneNum varchar(10) NOT NULL,
        Address varchar(50)
    )
""")

app = Flask(__name__)

@app.route('/insert',methods=['GET','POST'])
def insertIntoDB():
    if(request.method=='POST'):
        cust_Name = request.json['Name']
        due = request.json['Due']
        phone = request.json['Phone']
        address = request.json['Address']
        cust_detail_list = [cust_Name,due,phone,address]
        cursor.execute('Insert into CRUDUsingFlask values({});'.format(','.join(['"'+val+'"' for val in cust_detail_list])))
        conn.commit()
        print('insert into CRUDUsingFlask values({});'.format(','.join(['"'+val+'"' for val in cust_detail_list])))
        return jsonify(("Success"))

@app.route('/retrieve',methods=['GET','POST'])
def retrieveFromDB():
    if(request.method=='POST'):
        cust_Name = request.json['Name']
        print("select * from CRUDUsingFlask where Customer_Name={};".format('"'+cust_Name+'"'))
        cursor.execute("select * from CRUDUsingFlask where Customer_Name={};".format('"'+cust_Name+'"'))
        return jsonify((str(cursor.fetchall())))

@app.route('/delete',methods=['GET','POST'])
def deleteFromDB():
    if(request.method=='POST'):
        cust_Name = request.json['Name']
        print("DELETE FROM CRUDUsingFlask WHERE Customer_Name={};".format('"'+cust_Name+'"'))
        cursor.execute("DELETE FROM CRUDUsingFlask WHERE Customer_Name={};".format('"'+cust_Name+'"'))
        conn.commit()
        return jsonify(("Success"))

if __name__=='__main__':
    app.run()

