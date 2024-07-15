# LangGraph_demo
LangGraphのデモ

## 準備
### API keyの取得

必要なAPI Key

- OpenAI

取得したAPIキーはDockerfileのENVに追記する。

## 実行方法
```
docker image build -t lang-graph .
docker container run --rm -it -v $(pwd):/app -p 8080:8080 lang-graph bash
```

### Streamsync
編集
```
streamsync edit chatbot --port 8080 --host 0.0.0.0 --enable-remote-edit
```
実行
```
streamsync run chatbot --port 8080 --host 0.0.0.0
```
以下にアクセス。

http://0.0.0.0:8080