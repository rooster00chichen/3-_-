import tkinter as tk

# チェックボックス生成用のクラス。tk.Frameはおそらく不要。


class Checkbox(tk.Frame):

    def __init__(self, master):
        # 初期の設定。今回の場合は、おそらく不要
        super().__init__(master)
        self.master = master
        self.pack()

    # 単語設定のチェックボックスに付与する関数。一つしか選択されないようにするのと、現在の選択部分を保存するのと、
    # モード変更時に単語リストをモードに合わせたものにするための設定
    def text_one_select(self):
        # チェックボックス選択前の選択項目を所得
        a = self.text_select_list

        # チェックボックス選択前の単語リストを抹消
        for i in range(len(self.text_list[self.text_select_list])):
            self.number_cbtn[i].destroy()

        # 現在選択されているチェックボックスを線形探索。
        for i in range(len(self.text_select1)):
            if self.text_bvar[i].get():
                if self.text_select_list != i:
                    # 違う部分が選択されていたら変数に追加。
                    a = i

        # GUIと内部間で差異が生じないように、モード選択が１つしか選択されていない状態にGUIを設定
        if self.text_select_list != a:
            for i in range(len(self.text_select1)):
                if a != i:
                    self.text_bvar[i].set(False)
                elif a == i:
                    self.text_bvar[i].set(True)
        elif self.text_select_list == a:
            # １つは選択されていることを示す用
            self.text_bvar[a].set(True)

        # チェックボックス洗濯後の選択項目を設定
        self.text_select_list = a

        # 選択されたモードに対応した単語リストを新たに描画する
        for i in range(len(self.text_list[self.text_select_list])):
            self.number_bvar[i] = tk.BooleanVar()
            if i == 0:
                self.number_select_list = 0
                self.number_bvar[i].set(True)
            else:
                self.number_bvar[i].set(False)
            self.number_cbtn[i] = tk.Checkbutton(self.master, text=self.text_list[self.text_select_list][i].replace("\n", ""), font=(
                "Times New Roman", 15), variable=self.number_bvar[i], bg="#dfe", command=self.number_one_select)
            self.number_cbtn[i].place(
                x=135+self.place_x, y=self.place_y+25*i)

    # 単語設定のチェックボックスに付与する関数。一つしか選択されないようにするのと、現在の選択部分を保存する。
    def number_one_select(self):
        # チェックボックス選択前の選択項目を所得
        a = self.number_select_list

        # 現在選択されているチェックボックスを線形探索。
        for i in range(len(self.text_list[self.text_select_list])):
            if self.number_bvar[i].get():
                if self.number_select_list != i:
                    # 違う部分が選択されていたら変数に追加。
                    a = i

        # GUIと内部間で差異が生じないように１つしか選択されていない状態にGUIを設定
        if self.number_select_list != a:
            for i in range(len(self.text_list[self.text_select_list])):
                if a != i:
                    self.number_bvar[i].set(False)
                elif a == i:
                    self.number_bvar[i].set(True)
        elif self.number_select_list == a:
            # １つは選択されていることを示す用
            self.number_bvar[a].set(True)

        # チェックボックス洗濯後の選択項目を設定
        self.number_select_list = a

    # チェックボックスの作成
    def creat_checkbox(self, place_x, place_y, text_select1, text_list, max_list, prifarence, prifarence_list, place_name=""):

        # 場所の設定
        self.place_x = place_x
        self.place_y = place_y

        # 何のボタンが対応しているか示すためのラベル設置
        mode_left_text = tk.Label(self.master, font=(
            "Times New Roman", 15), text=place_name+"_button", width=15, height=1, bg="#dfe")
        mode_left_text.place(x=place_x+15, y=place_y-20)

        # チェックボックスの作成＿モード選択
        self.text_bvar = [None]*max_list
        self.text_cbtn = [None]*max_list
        self.text_select_list = prifarence[0]
        self.text_select1 = text_select1
        self.text_list = text_list
        for i in range(len(text_select1)):
            self.text_bvar[i] = tk.BooleanVar()
            if i == self.text_select_list:
                self.text_bvar[i].set(True)
            else:
                self.text_bvar[i].set(False)
            self.text_cbtn[i] = tk.Checkbutton(self.master, text=text_select1[i], font=(
                "Times New Roman", 15), variable=self.text_bvar[i], bg="#dfe", command=self.text_one_select)
            self.text_cbtn[i].place(x=place_x, y=place_y+25*i)

        # チェックボックスの作成＿単語設定
        self.number_bvar = [None]*max_list
        self.number_cbtn = [None]*max_list
        if len(self.text_list[self.text_select_list]) != prifarence_list[self.text_select_list]:
            self.number_select_list = 0
        else:
            self.number_select_list = prifarence[1]

        for i in range(len(text_list[self.text_select_list])):
            self.number_bvar[i] = tk.BooleanVar()
            if i == self.number_select_list:
                self.number_bvar[i].set(True)
            else:
                self.number_bvar[i].set(False)
            self.number_cbtn[i] = tk.Checkbutton(self.master, text=text_list[self.text_select_list][i].replace("\n", ""), font=(
                "Times New Roman", 15), variable=self.number_bvar[i], bg="#dfe", command=self.number_one_select)
            self.number_cbtn[i].place(x=135+place_x, y=place_y+25*i)
