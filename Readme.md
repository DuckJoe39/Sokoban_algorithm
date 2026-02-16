Sokoban AI Solver
Pythonを用いて、古典的なパズルゲーム「倉庫番（Sokoban）」を最適に解くAIソルバーです。A*探索（A-Star Search）および均一コスト探索（Uniform Cost Search）アルゴリズムを実装し、最小の手数でゴールに到達する経路を計算します。
search.py	A*探索およびUCSのコアアルゴリズム。
sokoban.py	倉庫番のルール、状態遷移、ヒューリスティック関数の定義。
solver.py	コマンドラインからパズルを解くためのメインエントリーポイント。
utils.py	メモ化（memoize）や、探索用の高速な PriorityQueue の実装。

使い方
clickをインストール
pip install click

solver.pyを実行
# A*探索で実行
python src/solver.py --input boards/＜txtファイル名＞ --output solution_astar.txt --mode astar

# 均一コスト探索で実行
python src/solver.py --input boards/＜txtファイル名＞ --output solution_ucs.txt --mode ucs

これで solution_astar.txt と solution_ucs.txt が生成

boardsフォルダにはテストに使用した.txt 形式のステージデータが同梱