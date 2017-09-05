## Shell操作Tips
1. 命令后加上`2>&1`表示把stderr输出到stdout中，可用于重定向到文件中
```
make > error 2>&1
```
