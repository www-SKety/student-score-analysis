# student-score-analysis
学生成绩数据分析系统，基于Python+Pandas+MySQL实现数据读取、清洗、入库、统计与可视化
# 学生成绩数据分析系统

## 项目简介
本项目基于 **Python + Pandas + Matplotlib + MySQL** 实现，完成从原始成绩数据读取、清洗、入库、统计分析到可视化的全流程自动化处理，是一套面向学生成绩管理的数据分析工具。

## 技术栈
- 编程语言：Python 3
- 数据处理：Pandas
- 数据可视化：Matplotlib
- 数据库：MySQL
- 自动化脚本：Shell
- 开发环境：VS Code + Git
- 运行环境：Windows / Linux

## 项目功能
1.  **数据读取**：支持读取 Excel 格式的学生成绩原始数据
2.  **数据清洗**：自动处理空值、过滤异常分数，保证数据质量
3.  **数据入库**：将清洗后的数据持久化存入 MySQL 数据库
4.  **多维度统计**：计算各科平均分、最高分、不及格人数等核心指标
5.  **可视化展示**：生成班级各科平均分对比柱状图，直观呈现成绩分布
6.  **自动化备份**：Shell 脚本实现程序自动运行与报表备份

## 项目目录结构
student-score-analysis/
├── main.py               # 主程序（数据处理+统计+可视化）
├── score_data.xlsx       # 原始成绩数据文件
├── score_chart.png       # 生成的可视化图表
├── auto_report.sh        # Linux自动化运行脚本
├── backup/               # 报表备份文件夹
└── README.md             # 项目说明文档
## 运行步骤
### 1. 安装依赖库
```bash
pip install pandas matplotlib pymysql openpyxl
2. 数据库准备

在 MySQL 中创建数据库和数据表：
CREATE DATABASE IF NOT EXISTS student_score DEFAULT CHARACTER SET utf8mb4;
USE student_score;

CREATE TABLE IF NOT EXISTS score (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    class VARCHAR(20) NOT NULL,
    chinese INT,
    math INT,
    english INT
);
3. 修改配置信息

在 main.py 中修改 MySQL 连接信息：
MYSQL_HOST = "localhost"
MYSQL_USER = "你的MySQL用户名"
MYSQL_PWD = "你的MySQL密码"
MYSQL_DB = "student_score"
4. 运行主程序
python main.py
5. Linux 环境自动化运行
chmod +x auto_report.sh
./auto_report.sh
运行效果

• 控制台打印原始数据、清洗后数据及统计结果

• 自动生成 score_chart.png 柱状图，展示各班各科平均分对比

• 数据自动存入 MySQL 的 score 表中

项目总结

本项目模拟了企业数据分析师的日常工作流程，熟练掌握了数据预处理、数据库交互、数据可视化及 Linux 脚本自动化开发，具备基础的数据分析与运维能力，可作为数据科学专业的入门实战项目。
