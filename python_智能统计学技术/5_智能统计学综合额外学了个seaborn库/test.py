import seaborn as sns
import matplotlib
#应用默认的主题，当然还有其他主题可以自由选择
sns.set_theme()
#载入一个范例数据集，这个数据库默认是没有的，需要自己github到下载
tips = sns.load_dataset("tips")
#创建数据可视化图片
sns.relplot(
    data=tips,
    x="total_bill", y="tip", col="time",
    hue="smoker", style="smoker", size="size",
)
#如果在matplotlib模式下使用Jupyter / IPython接口展示那就不需要这一条
#其他情况都请加上这一句，要不然图片不会在窗口展示，后面会说到原理
matplotlib.pyplot.show()
