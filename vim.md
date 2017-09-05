
## 设置tags
- `ctags -R --c++-kinds=+p --fields=+iaS --extra=+q <dir>` 生成tags，最好重命名为.tags文件
- 在vim中设置`set tags+=~/.tags;,.tags`
- 使用`<C-w>]`, `<C-w>}`进行跳转

- `"+y`复制到系统粘贴板，`"+p`系统粘贴到vim

| 操作 | 作用 |
| C-v c | 行修改 |
| C-v d | 行删除 |
| C-v S-i | 行插入 |
| C-v S-a | 行增加 |
| S-\* | 查找word在当前buffer所有的引用 |
