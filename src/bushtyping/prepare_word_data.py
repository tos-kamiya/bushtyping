import os
import re
from bs4 import BeautifulSoup

def generate_script_for_word_data(subdirectory, output_script_filename):
    """
    指定されたサブディレクトリにあるHTMLファイルから熟語を読み取り、
    リスト形式で記述したPythonスクリプトを生成します。

    Args:
        subdirectory (str): サブディレクトリの名前（例: "小1", "小2"）。
    """

    words = []
    for filename in os.listdir(subdirectory):
        if filename.endswith(".html"):
            filepath = os.path.join(subdirectory, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    html = f.read()

                    #Beautiful SoupでHTMLを解析
                    soup = BeautifulSoup(html, 'html.parser')

                    # aタグから熟語を抽出
                    for a_tag in soup.find_all('a'):
                        word = a_tag.text
                        words.append(word)

            except Exception as e:
                print(f"エラー: {filepath} を読み込めませんでした。 {e}")

    # Pythonスクリプトの生成
    script_content = f"""words = [
    {', '.join(f'"{word}"' for word in words)}
]
"""

    # スクリプトをファイルに書き出す
    output_path = os.path.join("data", output_script_filename) # dataディレクトリに保存
    with open(output_path, "w", encoding="utf-8") as outfile:
        outfile.write(script_content)

    print(f"スクリプト '{output_script_filename}' を生成しました。")


# 例: "data/小1" ディレクトリのHTMLファイルからスクリプトを生成する場合
# generate_script_for_word_data("data/小1")

# すべてのディレクトリに対してスクリプトを生成する場合 (例)
# base_dir = "data"
# for subdir in os.listdir(base_dir):
#      full_path = os.path.join(base_dir, subdir)
#      if os.path.isdir(full_path):
#          generate_script_for_word_data(full_path)

generate_script_for_word_data("data/小1", "words_s1.py")
generate_script_for_word_data("data/小2", "words_s2.py")
generate_script_for_word_data("data/小3", "words_s3.py")
generate_script_for_word_data("data/小4", "words_s4.py")
generate_script_for_word_data("data/小5", "words_s5.py")
generate_script_for_word_data("data/小6", "words_s6.py")
generate_script_for_word_data("data/中2", "words_c2.py")
generate_script_for_word_data("data/中3", "words_c3.py")
generate_script_for_word_data("data/常用", "words_j.py")
generate_script_for_word_data("data/準1級", "words_j1k.py")
generate_script_for_word_data("data/1級", "words_1k.py")
