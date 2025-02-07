# 部首タイピングゲーム (Busu Typing Game)

部首やつくりに分解された熟語からもとの熟語を当てる、クイズ形式のタイピングゲームです。

* 小1から漢検1級までのレベルを指定できます。
* ただし、頻出の漢字の並びを熟語としているので、必ずしも辞書に載っている熟語とは限りません。

## 構成

```
/
├── busutyping.py   # ゲームスクリプト
└── data/           # データディレクトリ
    ├── kanji2radical_left_right.json # 漢字-部首対応データ (左右)
    ├── kanji2radical_top_bottom.json # 漢字-部首対応データ (上下)
    ├── 小1/         # 小学校1年生レベルの単語データ
    ├── 小2/         # 小学校2年生レベルの単語データ
    ├──...
    ├── 高校/        # 高校レベルの単語データ
    ├── 準一級/      # 準一級レベルの単語データ
    └── 一級/        # 一級レベルの単語データ
```

## 始め方

リポジトリをクローンまたはダウンロードしてください。

ゲームスクリプトを実行

```bash
python busutyping.py [レベル]
```

例：

```bash
python busutyping.py s3  # 小3レベル
python busutyping.py j1k # 準一級レベル
python busutyping.py      # デフォルト: 小3レベル
```

## 操作方法

* 部首が表示されたら、元の熟語を入力してください。
* 3回間違えるとゲームオーバーです。
* 空文字列を入力するとその問題はギブアップとなり、答えが表示されます。

## オプション

* `s1`, `s2`,..., `s6`: 小学校1年生～6年生
* `j2`, `j3`: 中学校2年、3年生
* `h`: 高校
* `j1k`: 準一級
* `1k`: 一級

## ライセンス

* MIT License (Pythonスクリプト)
* Creative Commons Attribution-Share Alike 4.0 International (データ: `data/kanji2radical_*.json`, 提供元: https://github.com/yagays/kanjivg-radical/
* CC BY 4.0 (データ: `data/小1/`, `data/高校/` など, 提供元: https://github.com/marmooo/graded-idioms-ja/

