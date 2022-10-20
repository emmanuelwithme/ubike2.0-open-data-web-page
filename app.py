from encodings.utf_8 import encode
import json
from urllib import request
from flask import Flask, render_template


print("__name__: ", __name__)
app_f = Flask("__name__")
# Python 直譯器執行程式碼時，有一些內建、隱含的變數，__name__就是其中之一，其意義是「模組名稱!!」。
# 如果該檔案是被引用，其值會是模組名稱；但若該檔案是(透過命令列)直接執行，其值會是 __main__；。
# 如果傳遞__name__，會是該程式檔名。


@app_f.route("/")
def hello():
    return render_template("base.html")


@app_f.route("/ubike2.0")
def ubike20():
    data_name_dict = {"ar": "站點位置", "sarea": "行政區域", "sno": "站號", "sna": "站名", "tot": "總停車格",
                      "sbi": "目前車輛數量", "bemp": "空位數量", "act": "全站禁用狀態(0:禁用、1:啟用)", "infoTime": "各站資料更新時間"}
    opendata_url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    # re = request.urlopen(opendata_url)
    with request.urlopen(opendata_url) as response:
        # data = response.read().decode(encoding='utf-8')
        # print(data)
        data = json.load(response)
        print(data)
        for station in data:
            for key, value in data_name_dict.items():
                print(value, ": ", station[key])
            print("-------------------------------------")
    return render_template("bike_list.html", data=data, data_name_dict=data_name_dict.items())


if __name__ == "__main__":
    app_f.run()
