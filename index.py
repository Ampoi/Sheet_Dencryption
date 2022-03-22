import openpyxl #ライブラリの読み込み

wb = openpyxl.load_workbook('hoge.xlsx') #ファイルパス
ws = wb['Sheet1'] #シート名
ws.protection.disable() #そのファイルを解除
