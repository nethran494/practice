import sqlite3
con = sqlite3.connect("data.db")
cr = con.cursor()
fname = 'KV'
lname = 'Nethra'
email = 'nethran494@gmail.com'
username = 'nethravijay'
password = 'nethra@123'


cr.execute("create table if not exists User(id intger primary key, fname TEXT,lname TEXT, email TEXT,username TEXT,password TEXT)")
# cr.execute("insert into user values('"+fname+"','"+lname+"','"+email+"','"+username+"','"+password+"')")
# con.commit()
cr.execute("insert into user(fname,lname, email,user) values('"+fname+"','"+lname+"')")
con.commit()

# cr.execute("select * from user where fname = '"+fname+"'and lname='"+lname+"' and password = '"+password+"'")
# cr.execute("update user  set fname = 'Nethra', lname = 'Vathi' where username = 'nethravijay' ")
# con.commit()
# cr.execute("select * from user")
# cr.execute("delete from user where fname = 'KV'")
# con.commit()
# cr.execute("select * from user")
# cr.execute("alter table user add lname")
# cr.execute("alter table user drop lname")
cr.execute("drop table user")
con.commit()
cr.execute("select * from user")
var = cr.fetchall()
print(var)
# data=[fname,lname,email,username,password,photo]

# cr.execute("insert into user value(?,?,?,?,?,?,)",[data])
