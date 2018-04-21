# lcd_imog
Raspberry PiでAQM0802Aを使って文字を表示するのを簡潔にやるPythonモジュールです。

## Description
半角文字のみ対応、スパゲッティコード、ゴミコード。
i2csetコマンドを使って無理やり制御しています。
Raspberry Piでしか動きません。
Raspberry Pi3 Model Bのみ動作確認。

## Usage
### Install
```sh
git clone https://github.com/GomiPrograms/lcd_imog.git
cd lcd_imog
```
・Raspberry Pi
・AQM0802A(バックライト付き)
※事前にI2C通信を有効化、i2csetコマンドが使用できる環境を作っておいてください。

## Hints
### Options
```Python
printLCD(input1, input2)
```
input1 -> 1行目
input2 -> 2行目
に表示するstr型のオブジェクトを渡してください。

```Python
clearAll()
```
LCDを初期化します。プログラムの終わりには必ず実行してください。

### Examples Of Command
```Python
import time 
printLCD('Hello', 'ｺﾝﾊﾞﾝﾊ!') # 1行目に'Hello'、2行目に'ｺﾝﾊﾞﾝﾊ!'を表示
time.sleep(5) # 5秒待機
clearAll() # LCDを初期化
```

## Future Releases
・LCDのGPIOピンを設定できるようにする
・データシートに乗ってる文字全てに対応する
・いろいろやる

## Contribution
1. Fork it  
2. Create your feature branch  
3. Commit your changes  
4. Push to the branch  
5. Create new Pull Request

## License
[MIT](LICENSE)