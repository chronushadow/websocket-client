# websocket-client

Python で WebSocket クライアントを実装する。

## Usage

### Requirement

### Install

### Run

第1引数に接続先 WebSocket サーバーの URLを指定して実行する。

```
python websocket-client.py wss://hoge.hoge
```

## Architecture

### フレームワーク／ライブラリ

[websocket-client](https://github.com/websocket-client/websocket-client) を利用する。

新しいスレッドを開始して、何らかのインプットがあるまで待機。インプットされたら、WebSocket サーバーへ送信する。