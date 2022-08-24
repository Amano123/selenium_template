# selenium template

スクレイピングをするときに使用する。
**python/src**にプログラムを置くとコンテナ内で実行できる。

## Apple Silicon(M1 チップ：arm64)について

Apple Silicon(M1 チップ：arm64)では、chromedriverのエラーが発生する問題がある。  
対策として、Chromeのarm64（M1 CPU）版がないのでChromiumを使用している。  
M1 Mac & Docker Desktop for Mac以外の環境であれば、Chrome、Firefox、 Edgeのドライバーで実行できる。

## 実行コマンド

```shell
docker-compose build --no-cache
docker-compose up -d
```

## サンプルプログラムの実行

``` shell
docker exec -it selenium-python-1 python sample.py
```
