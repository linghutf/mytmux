# Golang问题汇总

## 第三方包问题
1. 遇到x/net包无法下载
  - 进入`$GOPATH/src/golang.org/x/`
  - 运行`git clone https:/github.com/golang/net.git net`
  - 安装`go install net`
