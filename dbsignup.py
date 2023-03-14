import mysql.connector
import json
from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template("homepage.html",msg=0)

@app.route('/signinsub',methods=['POST'])
def getvalue():
    conn=mysql.connector.connect(host="localhost",password="1729",user="root",database="dbwpcc")
    cur=conn.cursor()
    cur.execute("SELECT username,pass FROM students;")
    data=cur.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    name=request.form['user']
    password=request.form['pass']
    if name not in l:
        return render_template("homepage.html",msg=1)
    else:
        if(data[l.index(name)][1]==password):
            return render_template("page2.html",un=name,msg=5)
        else:
            return render_template("homepage.html",msg=2)

@app.route('/page1',methods=['POST'])
def page1():
    return render_template("page1.html")

@app.route('/signupsub',methods=['POST'])
def signupsub():
    conn=mysql.connector.connect(host="localhost",password="1729",user="root",database="dbwpcc")
    cur=conn.cursor()
    cur.execute("SELECT username,pass FROM students;")
    data=cur.fetchall()
    l=[]
    for i in data:
        l.append(i[0])
    name=request.form['user']
    password=request.form['pass']
    if name in l:
        return render_template("page1.html",msg=True)
    else:
        query='INSERT INTO students SET username=%s, pass=%s;'
        values=(name,password)
        cur.execute(query,values);
        conn.commit();
        return render_template("homepage.html",msg=3)

@app.route('/already',methods=['POST'])
def already():
    return render_template("homepage.html")

@app.route('/detsub',methods=['POST'])
def detsub():
    conn=mysql.connector.connect(host="localhost",password="1729",user="root",database="dbwpcc")
    cur=conn.cursor()
    uname=request.form['uname']
    fname=request.form['fname']
    add=request.form['add']
    email=request.form['email']
    gen=request.form['gen']
    coun=request.form['coun']
    grad=request.form['grad']
    exp=request.form['exp']
    phn=request.form['phn']
    linkd=request.form['linkd']
    dob=request.form['dob']
    work=request.form['work']
    query="UPDATE students SET fullname=%s,address=%s,email=%s,phone=%s,gender=%s,country=%s,graduation=%s,experience=%s,linkedin=%s,dob=%s,workmode=%s WHERE username=%s;"
    values=(fname,add,email,phn,gen,coun,grad,exp,linkd,dob,work,uname)
    cur.execute(query,values)
    conn.commit();
    return render_template("homepage.html")

if __name__ == '__main__':
    app.run(debug=True)
