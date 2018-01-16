# WEEK 003
## Goal
1. Fittingをさっくり理解する
1. Fitting を自作してみる
1. Fitting ライブラリに触れる

## 1. Fittingとは？

> 曲線あてはめ（きょくせんあてはめ）またはカーブフィッティング（英: curve fitting）[1][2][3][4]は、実験的に得られたデータまたは制約条件に最もよく当てはまるような曲線を求めること。最良あてはめ、曲線回帰とも。

ということで、
(実験など)実データから、計算式を類推する手法です。
実データを使う分野ではほぼ必ず使います。

例えば、、、
電気回路の電圧と電流を測定しました。
電気回路の抵抗を求めたいです。しかし、電圧と電流の測定値にはノイズが結構乗っています。
こんな時に使います。

機械学習では、回帰分析とか呼びます。

## [2. Fittingしてみる (1) 自作編](practice/fitting.ipynb)


## [3. Fittingしてみる (2) 実践編](practice/fitting.ipynb)
2章で自作したFittingですが、精度/速度/使い勝手を考えるとライブラリを使います。
今回は1970年代からある老舗"Minuit"のPythonバインディング"iminuit"を使います。科学計算分野でFittingを行う場合によく使用されています。(ROOTなど)

### install
    pip install iminuit

### Reference

    http://nbviewer.jupyter.org/github/iminuit/iminuit/blob/master/tutorial/tutorial.ipynb


