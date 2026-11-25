# indentcheck

`indentcheck` は、PythonのソースコードのインデントをチェックするLinuxコマンドです。

標準入力から受け取ったPythonコードを調べ、インデントに関する問題を検出します。

## 機能

- インデントが4の倍数になっているか確認
- 行頭にタブ文字が含まれていないか確認
- エラーが発生した行番号と内容を表示
- 検出したエラーの合計数を表示
- 標準入力に対応しており、パイプで他のコマンドと連携可能

## 使用方法

### 実行権限の設定

```bash
chmod +x indentcheck
```


### パイプを利用する

```bash
cat sample.py | ./indentcheck
```

```bash
printf 'def hello():\n  print("Hello")\n' | ./indentcheck
```

## 実行結果

### 正常な場合

入力：

```python
def hello():
    print("Hello")
```

出力：

```text
No indentation errors found.
```

### インデントに問題がある場合

入力：

```python
def hello():
  print("Hello")
```

出力：

```text
Line 2: Indentation is not a multiple of 4.
1 indentation error(s) found.
```

## 使用技術

- Python 3
- 標準ライブラリ（追加ライブラリ不要）

## License

BSD 3-Clause License
