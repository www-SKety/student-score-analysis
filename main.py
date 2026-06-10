# 导入所需库
import pandas as pd
import matplotlib.pyplot as plt
import pymysql
from pymysql import Error

# ===================== 配置区=====================
# MySQL 连接信息
MYSQL_HOST = "localhost"
MYSQL_USER = "root"       # 你的MySQL用户名
MYSQL_PWD = "123456"     # 你的MySQL密码
MYSQL_DB = "student_score"
# Excel 文件路径
EXCEL_PATH = "./score_data.xlsx"
# 设置中文显示（解决matplotlib绘图乱码）
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
# =================================================================

def read_excel_data():
    """1. 读取Excel成绩数据"""
    try:
        df = pd.read_excel(EXCEL_PATH)
        print("✅ Excel数据读取成功！")
        print("原始数据：")
        print(df)
        return df
    except Exception as e:
        print(f"❌ 读取Excel失败：{e}")
        return None

def data_clean(df):
    """2. 数据清洗：处理缺失值、异常分数"""
    # 删除存在空值的行
    df = df.dropna()
    # 过滤分数 0~100 之外的异常数据
    score_cols = ["语文", "数学", "英语"]
    for col in score_cols:
        df = df[(df[col] >= 0) & (df[col] <= 100)]
    print("\n✅ 数据清洗完成！")
    print("清洗后数据：")
    print(df)
    return df

def insert_to_mysql(df):
    """3. 将清洗后的数据存入MySQL数据库"""
    try:
        # 连接数据库
        conn = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset="utf8mb4"
        )
        cursor = conn.cursor()

        # 遍历数据逐行插入
        for index, row in df.iterrows():
            sql = """
            INSERT INTO score (name, class, chinese, math, english)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (row["姓名"], row["班级"], row["语文"], row["数学"], row["英语"]))
        conn.commit()
        print("\n✅ 数据成功存入MySQL数据库！")
    except Error as e:
        print(f"\n❌ 数据库操作失败：{e}")
        conn.rollback()
    finally:
        if conn:
            cursor.close()
            conn.close()

def data_statistics(df):
    """4. 数据统计分析：平均分、最高分、不及格人数"""
    print("\n========== 成绩统计分析 ==========")
    score_cols = ["语文", "数学", "英语"]

    # 各科平均分
    avg_score = df[score_cols].mean()
    print("📊 各科平均分：")
    print(avg_score)

    # 各科最高分
    max_score = df[score_cols].max()
    print("\n📊 各科最高分：")
    print(max_score)

    # 统计不及格人数（<60分）
    print("\n📊 各科不及格人数：")
    for col in score_cols:
        fail_num = df[df[col] < 60].shape[0]
        print(f"{col} 不及格人数：{fail_num}")

def draw_chart(df):
    """5. 数据可视化：绘制班级平均分柱状图"""
    # 按班级分组，计算各科平均分
    class_avg = df.groupby("班级")[["语文", "数学", "英语"]].mean()
    print("\n✅ 开始生成可视化图表...")

    # 绘制柱状图
    class_avg.plot(kind="bar", figsize=(10, 6))
    plt.title("各班各科平均分对比")
    plt.xlabel("班级")
    plt.ylabel("平均分")
    plt.legend(loc="upper right")
    plt.tight_layout()
    # 保存图片到本地
    plt.savefig("./score_chart.png")
    print("✅ 图表已保存为 score_chart.png")
    # 弹出图表窗口
    plt.show()

def main():
    # 执行完整流程
    df = read_excel_data()
    if df is None:
        return
    df_clean = data_clean(df)
    insert_to_mysql(df_clean)
    data_statistics(df_clean)
    draw_chart(df_clean)
    print("\n🎉 学生成绩分析系统 全部功能执行完毕！")

if __name__ == "__main__":
    main()