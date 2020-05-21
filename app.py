import requests
from flask import Flask, render_template,request

app = Flask(__name__) # __name__ 為 python 內建的變數，他會儲存目前程式在哪個模組下執行，如果為__main__代表主程式



@app.route("/") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def home():

    return render_template("index.html", title="五官大於三觀")

#@app.route("/It/100") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

#def IT100():

#    return render_template("IT100.html", title="五官大於三觀")

@app.route("/It/200") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def IT200():

    return render_template("IT200.html", title="五官大於三觀")

@app.route("/It/300") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def IT300():

    return render_template("IT300.html", title="五官大於三觀")

@app.route("/JPN/100") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def JPn100():

   return render_template("JPn100.html", title="五官大於三觀")

@app.route("/JPN/200") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def JPn200():

   return render_template("JPn200.html", title="五官大於三觀")

@app.route("/JPN/300") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def JPn300():

   return render_template("JPn300.html", title="五官大於三觀")

@app.route("/BD/100") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def BD100():

   return render_template("BD100.html", title="五官大於三觀")

@app.route("/CUR/200") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def CUR200():

   return render_template("CUR200.html", title="五官大於三觀")

@app.route("/CUR/300") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def CUR300():

   return render_template("CUR300.html", title="五官大於三觀")

@app.route("/KOR/200") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def KOR200():

   return render_template("KOR200.html", title="五官大於三觀")

@app.route("/KOR/300") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def KOR300():

   return render_template("KOR300.html", title="五官大於三觀")

@app.route("/ND/100") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def ND100():

   return render_template("ND100.html", title="五官大於三觀")

@app.route("/SA/200") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def SA200():

   return render_template("SA200.html", title="五官大於三觀")

@app.route("/TW/100") #函式的裝飾 Decorator，以底下函式為基礎，提供附加的功能，這邊 "/" 代表根目錄

def TW100():

   return render_template("TW100.html", title="五官大於三觀")

if __name__ == "__main__": #如果以主程式運行

    app.run(debug=True)  #啟動伺服器 debug=True 修改內容將立即反應在網頁