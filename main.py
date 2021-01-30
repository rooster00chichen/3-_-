import subprocess
import tkinter as tk

import pyautogui as pygui
import pyperclip
import unicodedata
import serial
import os
import shelve


from chechbox import *
from file_open import *

# version 1.1.3

ser = serial.Serial('/dev/cu.usbserial-DN05HZ3P', 19200, timeout=None)

# 繰り返し実行


def count_up():
    global ser
    catch_serial = ser.read_all()
    catch_serial_string = catch_serial.decode()

    #catch_serial_string = "null"

    if 'ok' == catch_serial_string:
        # ここに入れたい処理
        handler(func_list[checkbox1.text_select_list],
                text_list[checkbox1.text_select_list][checkbox1.number_select_list].replace("\n", ""))
    elif 'left' == catch_serial_string:
        # ここに入れたい処理
        handler(func_list[checkbox2.text_select_list],
                text_list[checkbox2.text_select_list][checkbox2.number_select_list].replace("\n", ""))
    elif catch_serial_string == 'right':
        # ここにいれたい処理
        handler(func_list[checkbox3.text_select_list],
                text_list[checkbox3.text_select_list][checkbox3.number_select_list].replace("\n", ""))
    elif catch_serial_string == "end":
        a = subprocess.run(['osascript', '-e', 'display dialog "本当に終了しますか？"'])
        if a.returncode == 0:
            subprocess.run(
                ['osascript', '-e', 'display notification "終了シークエンスを実行" with title "終了シークエンス"'])
            click_btn()

    root.after(100, count_up)


# 関数名前とその関数の引数を引数として関数を実行
def handler(func, args):
    func(args)


# 機能の１つ、.txtファイルから読み取ったurlにApplescriptを用いてアクセス
def open_webpage(webpage: str):
    subprocess.run(
        ['osascript', '-e', 'tell application "safari" to activate'])
    subprocess.run(
        ['osascript', '-e', 'tell application "safari" to open location "'+webpage.replace('\n', '')+'"'])


# 機能の１つ、.txtファイルから読み取ったプリケーション名をApplescriptを用いて開く
def open_app(app: str):
    subprocess.run(
        ['osascript', '-e', 'tell application "' + app.replace('\n', '') + '" to activate'])
    subprocess.run(
        ['osascript', '-e', 'tell application "' + app.replace('\n', '') + '" to reopen'])


# 機能の１つ、.txtファイルから読み取った文章をpyautoguiとpyperclipを用いてペースト
# クリップボード削除　osascript -e "set the clipboard to {}"
def add_string(string):
    temp_string = pyperclip.paste()
    # print(temp_string)
    pyperclip.copy(string.replace('\n', ''))
    pygui.hotkey('command', 'v')
    try:
        pyperclip.copy(temp_string)
    except pyperclip.PyperclipException:
        pyperclip.copy("")


def change_of_nfc(donot_in: str):
    change_string = pyperclip.paste()
    changed_string = unicodedata.normalize('NFC', change_string)
    try:
        pyperclip.copy(changed_string)
    except pyperclip.PyperclipException:
        pyperclip.copy("")


# 終了時の処理
def click_btn():
    # ser.close()
    global prifarence_input, prifarence_mode, prifarence_max_list
    prifarence_mode[0] = [checkbox1.text_select_list,
                          checkbox1.number_select_list]
    prifarence_mode[1] = [checkbox2.text_select_list,
                          checkbox2.number_select_list]
    prifarence_mode[2] = [checkbox3.text_select_list,
                          checkbox3.number_select_list]
    prifarence_max_list = [0, file.string_list_count,
                           file.app_list_count, file.url_list_count]
    prifarence_input["mode"] = prifarence_mode
    prifarence_input["max_list"] = prifarence_max_list
    prifarence_input.close()
    root.destroy()


if __name__ == '__main__':
    # キャッシュのようなものにアクセス
    prifarence_file = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "prifarence")
    prifarence_input = shelve.open(prifarence_file)

    try:
        prifarence_mode = prifarence_input["mode"]
        prifarence_max_list = prifarence_input["max_list"]
    except KeyError:
        # ここの例外処理は、ファイルがなかった時用の初期値の設定
        prifarence_input["mode"] = [[0, 0], [0, 0], [0, 0]]
        prifarence_input["max_list"] = [0, 0, 0, 0]
        prifarence_mode = prifarence_input["mode"]
        prifarence_max_list = prifarence_input["max_list"]

    # urlなどが保存されたファイルにアクセス
    file = File_open(mode=6)

    func_list = [change_of_nfc, add_string, open_app, open_webpage]
    text_list = [["0"]*file.max_list,
                 file.string_list, file.app_list, file.url_list]

    # 枠の生成
    root = tk.Tk()

    canvas = tk.Canvas(root, width=780, height=432)
    canvas.pack()

    # 背景の追加
    image_file = os.path.join(os.path.dirname(
        os.path.abspath(__file__)), "nc123439.png")
    gazou = tk.PhotoImage(file=image_file)
    canvas.create_image(780/2, 432/2, image=gazou)

    # タイトルの挿入
    application_name = tk.Label(
        root, text="超便利‼︎楽々ショートカットボタン", font=("Times New Roman", 25), bg='green')
    application_name.place(x=390-8*25, y=20)

    text_select1 = ["change_of_nfc", "add_string",
                    "open_app", "open_webpage"]

    # checkbox1の生成
    checkbox1 = Checkbox(root)
    checkbox1.creat_checkbox(60, 90,
                             text_select1, text_list, file.max_list, prifarence_mode[0], prifarence_max_list, place_name="left")

    # チェックボックスの１つのサイズが150(px?),(600-150*3)/4で隙間の幅を計算。<-ver なんとか
    # 幅600を４つのエリアに分割。各エリアの境界線上に中央がくるように配置。<-v1.1.1
    # 目視で調整　v1.1.2

    # checkbox2の生成
    checkbox2 = Checkbox(root)
    checkbox2.creat_checkbox(60, 270,
                             text_select1, text_list, file.max_list, prifarence_mode[1], prifarence_max_list, place_name="center")

    # checkbox3の生成
    checkbox3 = Checkbox(root)
    checkbox3.creat_checkbox(405, 90,
                             text_select1, text_list, file.max_list, prifarence_mode[2], prifarence_max_list, place_name="right")

    # 終了用のボタン生成
    button = tk.Button(text="終了する", font=("Times New Roman", 32),
                       bg="green", command=click_btn)
    button.place(x=780/4*3-64, y=340)

    # 繰り返し用の処理
    root.after(100, count_up)

    # 画面の描画
    root.mainloop()
