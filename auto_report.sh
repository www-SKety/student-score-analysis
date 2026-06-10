#!/bin/bash
# 学生成绩报表自动导出脚本

# 替换成你本地项目文件夹的绝对路径
cd D:/code/student-score-analysis

# 执行Python分析程序
python3 main.py

# 备份图表文件
cp score_chart.png ./backup/$(date +%Y%m%d)_score_chart.png
echo "报表生成并备份完成"