#!/bin/sh
set -e

# 初始化 Go 模块（如果还没有的话）
if [ ! -f "go.mod" ]; then
    go mod init temp_proto_module
fi

# 使用 go install 安装工具
go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway@latest
go install github.com/grpc-ecosystem/grpc-gateway/protoc-gen-swagger@latest
go install github.com/golang/protobuf/protoc-gen-go@latest

# 下载并解压 Google API
wget https://repo1.maven.org/maven2/com/google/api/grpc/googleapis-common-protos/0.0.3/googleapis-common-protos-0.0.3.jar
jar xvf googleapis-common-protos-0.0.3.jar

# 创建目标目录（如果不存在）
mkdir -p $HOME/protobuf/include/

# 复制文件
cp -r google/ $HOME/protobuf/include/
ls -l

# 可选：清理临时文件
rm googleapis-common-protos-0.0.3.jar