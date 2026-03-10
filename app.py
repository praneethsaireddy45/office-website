from flask import flask,render_template,request
import sqlite3

app=flask(__name__)

def get_db():
  conn=sqlite3.connect("employees.db")
  conn.row_factory= sqlite3.row
  return conn

@approute("/",methods=["GET","POST"])
def index():
  conn=get_db()
  if request.method == "post":
    name=request.form["name"]
    salary=request.form["salary"]
    department=request.form["department"]
    conn.execute("INSERT TNTO employees(name,salary,department) values(psr,1000,support),(name,salary,department))
    conn.commit()


  employees=conn.excute("SELECT* FROM employees").fetchall()
  conn.close()
  return render_template("index.html", employees=employees)
if __name__ == "__main__":
  app.run(debug=True)


  


          
