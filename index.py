import openpyxl #ライブラリの読み込み

wb = openpyxl.load_workbook('/content/drive/MyDrive/apapa.xlsx') #ファイルパス
ws = wb['Sheet1'] #シート名
ws.protection.disable() #そのファイルを解除
