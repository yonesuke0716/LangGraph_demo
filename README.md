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
docker container run --rm -it -v $(pwd):/app lang-graph bash
```