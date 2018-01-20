from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "MySessionSecretKey"

mysql = MySQLConnector( app, "email_validation")

@app.route( "/" )
def front_page():
    return render_template( "index.html" )

@app.route( "/process", methods = ["POST"] )
def q():
    query = "SELECT email FROM emails WHERE email = :targetEmail"
    parameters = { "targetEmail": request.form['email'] }
    dbEmail = mysql.query_db ( query, parameters )
    if ( dbEmail ):
        flash ( "<p class='successMessage'>Email " + str(dbEmail[0]["email"]) + " found in the database!</p>" )
    else:
        flash ( "Email not in the database!" )
    return redirect( "/" )
    
app.run ( debug = True )