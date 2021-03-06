# WEEK 005
今回は座学が多いです。
## Goal
1. 回帰分析モデルを評価してみる
1. 以前ざっくりやったFittingについて少し踏み込む
1. 評価手法とは


## [1. 回帰分析モデルを評価してみる ](practice/regression.ipynb)

## [2. Fitting についてもう少し](practice/fitting.ipynb)

[OverView](../overview/readme.md)

## 3. 評価手法とは
予測問題に応じて、適切は評価方法(評価関数)を使用して評価を行う。
<br> 今回の需要予測の場合は、誤差を使用する。
<br> 今回の需要予測の様に線形回帰を行った場合、N次元座標空間に写像されるため、距離が強力な指標となるため。

Root Mean Squared Error (RMSE) = sqrt( 1/N * sigma (x  -  p)\*\*2 )
x : 実測値、p : 予測値

他にはこんな評価関数がある。

### 主な評価関数

 + AUC
   + 分類精度を測る
   + 0~1 (値が大きいほど良い)
 + LogLoss
   + 分類精度を測る
   + 0~ (値が小さいほど良い)
 + Accuracy
   + 分類精度を測る
   + 0~1 (値が大きいほど良い)
 + Precision
   + 正確性を測る
   + 0~1 (値が大きいほど良い)
 + Recall
   + カバー率を測る
   + 0~1 (値が大きいほど良い)
 + RMSE (Root Mean Squared Error, 重み付き平均二乗誤差)
   + 誤差を測る
   + 0~ (値が小さいほど良い)
 + MSE (Mean Squared Error, 平均二乗誤差)
   + 誤差を測る
   + 0~ (値が小さいほど良い)
 + MAE (Mean Absolute Error, 平均絶対誤差)
   + 誤差を測る
   + 0~ (値が小さいほど良い)
   + RMSEなどより誤差を大きく見積もる際に使用する
 + MAP@N
   + 検出精度を測る
   + 0~1 (値が大きいほど良い)
 + nDCG
   + ランキング精度を測る
   + 0~1 (値が大きいほど良い)
