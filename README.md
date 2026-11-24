# pairwise-vector-path-fill

## 领域

游戏、图形与多媒体

## 主题

矢量路径填充与抗锯齿

## 说明

保留环绕方向、自适应细分与解析覆盖。

初始状态下 `graphics/vector_path_fill.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
