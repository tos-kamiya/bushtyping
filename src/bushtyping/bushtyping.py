import argparse
import os
import random
import re
import sys
import time

if sys.platform != "win32":
    import readline  # for proper handling [BS] key

from .data_loader.kanji2radical_left_right import left_right_data
from .data_loader.kanji2radical_top_bottom import top_bottom_data

word_data = {}
from .data_loader.words_1k import words
word_data["1k"] = words
from .data_loader.words_j import words
word_data["j"] = words
from .data_loader.words_j1k import words
word_data["j1k"] = words
from .data_loader.words_c2 import words
word_data["c2"] = words
from .data_loader.words_c3 import words
word_data["c3"] = words
from .data_loader.words_s1 import words
word_data["s1"] = words
from .data_loader.words_s2 import words
word_data["s2"] = words
from .data_loader.words_s3 import words
word_data["s3"] = words
from .data_loader.words_s4 import words
word_data["s4"] = words
from .data_loader.words_s5 import words
word_data["s5"] = words
from .data_loader.words_s6 import words
word_data["s6"] = words


RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


def decompose_kanji(kanji):
    if kanji in left_right_data:
        return left_right_data[kanji]
    elif kanji in top_bottom_data:
        return top_bottom_data[kanji]
    else:
        return [kanji]  # 分解できない場合はそのまま返す


def decompose_word(word):
    parts = []
    for char in word:
        parts.extend(decompose_kanji(char))
    return parts


def get_words_from_html(subdirectory):
    """
    指定されたサブディレクトリにあるHTMLファイルから熟語を読み取り、リストとして返します。
    正規表現を使って<a>タグから熟語を抽出します。

    Args:
        subdirectory (str): サブディレクトリの名前（例: "小1", "小2"）。

    Returns:
        list: 熟語のリスト。
    """

    words = []
    for filename in os.listdir(subdirectory):
        if filename.endswith(".html"):
            filepath = os.path.join(subdirectory, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    html = f.read()
                    # 正規表現で<a>タグから熟語を抽出
                    pattern = r'<a href="https://www.google.com/search\?q=.*?>(.*?)</a>'
                    matches = re.findall(pattern, html)
                    for word in matches:
                        words.append(word)
            except Exception as e:
                print(f"エラー: {filepath} を読み込めませんでした。 {e}")
    return words


# def main():
#     words_list = get_words_from_html("小1")
#     word = words_list[0]
#     print(decompose_word(word))


def main():
    choices = {
        "s1": "小1",
        "s2": "小2",
        "s3": "小3",
        "s4": "小4",
        "s5": "小5",
        "s6": "小6",
        "c2": "中2",
        "c3": "中3",
        "k": "高校",
        "j1k": "準1級",
        "1k": "1級",
        "j": "常用",
    }
    parser = argparse.ArgumentParser(description="漢字部首分解クイズ")
    parser.add_argument(
        "grade",
        type=str,
        default="s3",
        nargs="?",
        help=f"出題範囲 (例: {', '.join(choices.keys())})",
    )
    args = parser.parse_args()

    if args.grade not in choices:
        print(f"error: 出題範囲は次のいずれかです: {', '.join(choices.keys())}")
    words_list = word_data.get(args.grade, None)
    assert words_list is not None
    num_questions = 10
    correct_count = 0
    start_time = time.time()

    for i in range(num_questions):
        while True:
            word = random.choice(words_list)
            parts = decompose_word(word)

            if len(parts) <= len(word):
                continue
            break

        random.shuffle(parts)

        attempts = 3
        while attempts > 0:
            print(f"{YELLOW}第{i+1}問: {RESET}パーツ:", "".join(parts))
            answer = input("元の熟語を入力してください (ギブアップ: 空白): ")

            if not answer:  # 空文字列の場合
                print(f"{RED}ギブアップ！答えは「{word}」でした。{RESET}")
                attempts = 0
            elif answer == word:
                print(f"{GREEN}正解！{RESET}")
                correct_count += 1
                break
            else:
                print(f"{RED}不正解...{RESET}")
                attempts -= 1

        if attempts == 0 and answer != word:
            print(f"答えは「{word}」でした。")

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"\n{YELLOW}クイズ終了！{RESET}")
    print(f"正答率: {correct_count / num_questions * 100:.1f}%")
    print(f"経過時間: {elapsed_time:.1f}秒")


if __name__ == "__main__":
    main()
