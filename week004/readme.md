# WEEK 004
## Goal
1. 回帰分析をざっくり理解する
1. 回帰分析をやってみる

## 1. 回帰分析とは？

前回でやったFittingのようなデータの傾向を分析し、数式化、未知データを予測する手法。
<br>数値を予測するために使用する。

回帰分析は単回帰分析/重回帰分析と大きく分類される。
 + 単回帰は1つのパラメータ(説明変数, 特徴量)から、1つのパラメータ(目的変数)を求めること
   + パラメータとパラメータの関係がシンプルな時に効力がある
 + 重回帰は複数のパラメータ(説明変数, 特徴量)から、1つのパラメータ(目的変数)を求めること
   + パラメータとパラメータの関係が複雑な時に効力がある
   + パラメータを一杯使用すればいい訳ではない


[OverView](../overview/readme.md)

## 2. 回帰分析をやってみる
### 分析の流れ
1. 説明変数を決め、データを準備
   + データ収集
   + 前処理
     + 欠損値
     + 名寄せ
     + など
   + 学習データとテストデータにデータを分割
     + データを全て使用してモデルを作成すると、過学習が発生していることを知ることが出来ない
     + そのために、データを学習データとテストデータに分ける
     + 学習データでモデルを作成
     + テストデータでモデルの評価を実施
       + テストデータを使用して予測を実施。予測結果と実測値を使用してモデルの評価を実施。
       + 通例、7:3 程度で学習データとテストデータを分けます。
1. 使用するモデル/アルゴリズムを選択
   + 今回は最もシンプルな線形回帰モデルを使用する
1. モデルを作成
1. モデルを使い予測
1. モデルの評価
1. 上記を繰り返し

### 線形回帰 (Linear Regression)

データが
<br>y = a\*x + b, y = a\*x_1 + b\*x_2 + c の様な直線(線形)的な関係
<br> であると仮定して行う、データの関係性分析方法

### 準備
#### Install Library

    pip install scikit- learn # Higher 0.19.1

## [3. 回帰分析してみる ](practice/regression.ipynb)

今回は最も簡単な線形回帰モデルを使用
