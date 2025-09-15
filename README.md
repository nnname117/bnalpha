# bnalpha

## 项目简介
本项目为币安现货交易的 alpha 策略板块示例，集成了币安 API。

## 目录结构
```
├── alpha/
│   └── spot_alpha.py   # 现货交易 alpha 策略模块
├── config.py           # API 密钥配置
├── main.py             # 主程序入口
├── requirements.txt    # 依赖包
└── README.md           # 项目说明
```

## 使用方法
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
2. 配置 API 密钥：
   编辑 `config.py`，填入你的币安 API KEY 和 SECRET。
3. 运行主程序：
   ```bash
   python main.py
   ```

## 示例功能
- 获取账户信息
- 获取 BTCUSDT 当前价格
- 可扩展更多交易逻辑

## 依赖
- python-binance

---
如需扩展更多 alpha 策略或交易功能，请在 `alpha/spot_alpha.py` 中添加相关代码。