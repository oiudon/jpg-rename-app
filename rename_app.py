import tkinter
import os
import glob
from tkinter import filedialog

# フレーム作成
class Application(tkinter.Frame):
    # イニシャライズ
    def __init__(self, root=None):
        super().__init__(root, width=280, height=180,
                         borderwidth=1, relief='groove')
        self.root = root
        self.pack()
        self.pack_propagate(0)
        self.create_widgets()
        

    # ウィジェット作成メソッド
    def create_widgets(self):
        # 閉じるボタン
        quit_btn = tkinter.Button(self)
        quit_btn['text'] = '閉じる'
        quit_btn['command'] = self.root.destroy
        quit_btn.place(x=170, y=120)

        # フォルダ参照ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = 'フォルダ参照'
        submit_btn['command'] = self.dir_handler
        submit_btn.place(x=30, y=20)

        # ラベル
        digit_lbl = tkinter.Label(self, text='桁数：')
        digit_lbl.place(x=30, y=70)

        # スピンボックスウィジェットの作成と配置
        self.spinbox = tkinter.Spinbox(self, from_=1, to=20, increment=1)
        self.spinbox['width'] = 5
        self.spinbox.place(x=70, y=70)

        # 実行ボタン
        submit_btn = tkinter.Button(self)
        submit_btn['text'] = '実行'
        submit_btn['command'] = self.do_handler
        submit_btn.place(x=70, y=120)

        # メッセージ出力
        self.message = tkinter.Message(self)
        self.message['width'] = 150
        self.message.place(x=100, y=20)


    # フォルダ指定処理
    def dir_handler(self):
        self.dirPath = ""
        dir = os.path.abspath(os.path.dirname(__file__))
        self.dirPath = filedialog.askdirectory(initialdir = dir)

        # フォルダパスが指定されているか確認
        if not self.dirPath:
            self.message['text'] = 'フォルダを指定してください'
            return

        self.message['text'] = 'フォルダ指定完了'


    # 実行時処理
    def do_handler(self):
        # フォルダパスが指定されているか確認
        if not self.dirPath:
            self.message['text'] = 'フォルダを指定してください'
            return

        # 桁数を読み込み
        digits = self.spinbox.get()

        # 連番で一括リネームしたい画像があるフォルダを指定し、変数へ代入
        filenames = glob.glob(self.dirPath + '/*.jpg')

        # 連番でリネーム
        for i, old_filename in enumerate(filenames):
            # 連番を指定桁数に変換
            num = str(i).zfill(int(digits))
            # 新しいファイル名
            new_filename = self.dirPath + '/' + num + '.jpg'
    
            # 既に同じ連番のファイル名があればスキップ
            if old_filename == new_filename :
                continue
    
            # リネーム実行
            os.rename(old_filename, new_filename)

        self.message['text'] = '完了'


root = tkinter.Tk()
root.title('jpg連番リネームアプリ')
root.geometry('300x200')
app = Application(root=root)
app.mainloop()