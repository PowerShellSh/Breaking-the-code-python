# シーザー暗号
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

# 暗号化・復号する文字列.
#message = 'This is my secret message.'
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
# 暗号化・復号の鍵.
#key = 13
key = input('Enter Number Key?:')
key = int(key)
# プグラムが暗号化するか復号するか.
#mode = 'encrypt' # 'encrypt'あるいは'decrypt'のどちらかを指定する.
mode = 'decrypt'
# 暗号化できるシンボルの全候補.
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# メッセージの暗号化・復号の結果を格納する.
translated = ''

for symbol in message:
    # 注意：文字列SYMBOLSに含まれるシンボルのみを暗号化・復号する.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # 暗号化・復号を実行する.
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # 必要に応じてラップアラウンドを処理する.
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # 暗号化・復号せずにシンボルを追加する.
        translated = translated + symbol

# 変換後の文字列を出力する.
print(translated)
# copy() はpyperclipモジュールの関数。引数に指定した文字列をコピーする。
pyperclip.copy(translated)
