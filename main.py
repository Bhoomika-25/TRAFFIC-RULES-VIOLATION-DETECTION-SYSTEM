from flask import *
import sqlite3

app = Flask(__name__)


@app.route("/")
def start():
    return render_template("navbar.html");

@app.route("/contact")
def contact():
    return render_template("contact.html");

@app.route("/info")
def info():
    return render_template("info.html");

@app.route("/policelogin")
def policelogin():
    return render_template("policelogin.html");

@app.route("/login")
def login():
    return render_template("login.html");

@app.route("/multilogin")
def multilogin():
    return render_template("multilogin.html");

@app.route("/multiregister")
def multiregister():
    return render_template("multiregister.html");


@app.route("/savedetails", methods=["POST", "GET"])
def saveDetails():
    msg = "msg"
    if request.method == "POST":
        try:
            vno = request.form["vno"]
            viol = request.form["viol"]
            with sqlite3.connect("vio1.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into culprits (vno, viol) values (?,?)", (vno,viol))
                con.commit()
                msg = "Violation successfully Added"
        except:
            con.rollback()
            msg = "We can not add the Violation."
        finally:
            return render_template("success.html", msg=msg)
            con.close()

@app.route("/savechallans", methods=["POST", "GET"])
def saveChallans():
    msg = "msg"
    if request.method == "POST":
        try:
            vechno = request.form["vechno"]
            viola = request.form["viola"]
            amt1 = request.form["amt1"]
            with sqlite3.connect("challans.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into amount(vechno, viola, amt1) values (?,?,?)", (vechno,viola,amt1))
                con.commit()
                msg = "Challan successfully Added"
        except:
            con.rollback()
            msg = "We can not add the Challan Details."
        finally:
            return render_template("success1.html", msg=msg)
            con.close()


@app.route("/searchchallans", methods=["POST", "GET"])
def searchChallans():
    msg = "msg"
    if request.method == "POST":
        try:
            vechno = request.form["vechno"]
            print(vechno)
            with sqlite3.connect("challans.db") as con:
                cur = con.cursor()
                print('Step 1')
                cur.execute("select * from amount where vechno = ?", vechno)
                print('Step 2')
                con.commit()
                msg = "Challan Details"
        except:
            con.rollback()
            msg = "We can not show the Challan Details."
        finally:
            return render_template("success2.html", msg=msg)
            con.close()


@app.route("/viewsearch")
def viewsearch():
    con = sqlite3.connect("challans.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from amount")
    rows = cur.fetchall()
    return render_template("viewsearch.html", rows=rows)


@app.route("/view")
def view():
    con = sqlite3.connect("vio1.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from culprits")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/viewchallans")
def viewchallans():
    con = sqlite3.connect("challans.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from amount")
    rows = cur.fetchall()
    return render_template("viewchallans.html", rows=rows)

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/deletechallans")
def deletechallans():
    return render_template("deletechallans.html")

@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    with sqlite3.connect("vio1.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from culprits where id = ?", id)
            msg = "Record successfully deleted"
        except:
            msg = "Can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


@app.route("/deleterecord1", methods=["POST"])
def deleterecord1():
    id = request.form["id"]
    with sqlite3.connect("challans.db") as con:
        try:
            cur = con.cursor()
            cur.execute("delete from amount where id = ?", id)
            msg = "Record successfully deleted"
        except:
            msg = "Can't be deleted"
        finally:
            return render_template("delete_record1.html", msg=msg)



@app.route("/register")
def register():
    return render_template("register.html");

@app.route("/picfromcam")
def picfromcam():
    return render_template("picfromcam.html");


@app.route("/add")
def add():
    return render_template("user-add.html")

@app.route("/addchallans")
def addchallans():
    return render_template("addchallans.html")

@app.route("/policeregister")
def policeregister():
    return render_template("policeregister.html");

@app.route("/logout")
def logout():
    return render_template("logout.html")

@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/adminlogin", methods=["POST", "GET"])
def adminlogin():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["username"]
            pwd = request.form["password"]
            with sqlite3.connect("login3.db") as con:
                cur = con.cursor()
                cur.execute("Select username,password from users where username = ? and password = ? ",(name, pwd))
                result = cur.fetchone()
                if result:
                    if (result[0] == name and result[1] == pwd):
                        return render_template("navpolice.html")
                else:
                    return render_template("loginfail.html", msg=msg)

        except:
            msg = "Sorry! Try Again!!"

        finally:
            con.close()

@app.route("/createadmin", methods=["POST", "GET"])
def createadmin():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            uname = request.form["uname"]
            pwd = request.form["password"]
            with sqlite3.connect("login3.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into users (username, password) values (?,?)", (uname, pwd))
                con.commit()
                msg = "Created Sucessfully"
        except:
            con.rollback()
            msg = "Sorry! Try Again!!"
        finally:
            return render_template("multilogin.html", msg=msg)
            con.close()


@app.route("/createuser", methods=["POST", "GET"])
def createuser():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["name"]
            uname = request.form["uname"]
            pwd = request.form["password"]
            vno = request.form["vno"]
            phno = request.form["phno"]
            with sqlite3.connect("users11.db") as con:
                cur = con.cursor()
                cur.execute("INSERT into hello1 (username, password, vno, phno) values (?,?,?,?)", (uname, pwd, vno, phno))
                con.commit()
                msg = "Created Sucessfully"
        except:
            con.rollback()
            msg = "Sorry! Try Again!!"
        finally:
            return render_template("login.html", msg=msg)
            con.close()

@app.route("/login", methods=["POST", "GET"])
def userlogin():
    msg = "msg"
    if request.method == "POST":
        try:
            name = request.form["username"]
            pwd = request.form["password"]
            with sqlite3.connect("users11.db") as con:
                cur = con.cursor()
                cur.execute("Select username,password from hello1 where username = ? and password = ? ",(name, pwd))
                result = cur.fetchone()
                if result:
                    if (result[0] == name and result[1] == pwd):
                        return render_template("navuser.html")
                else:
                    return render_template("loginfail.html", msg=msg)

        except:
            msg = "Sorry! Try Again!!"

        finally:
            con.close()



if __name__ == "__main__":
    app.run(debug=True)


