# Docker上でのML環境構築

1. Dockerfileを作成
2. $Docker build .
3. docker run -p 8888:8888 -v ~/{作業ディレクトリ}:/work --name my-lab {buildで出てきたコード}
4. ブラウザ上でlocalhost:8888にアクセス