import pandas as pd
import matplotlib.pyplot as plt



def read_excel_and_plot_dual_axis(file_path , material):
    df = pd.read_excel(file_path)
    if material == 'XJ':

        times = df.iloc[:,0] #df.iloc用于根据列索引获取数据
        delta_temp = df.iloc [:,3]
        temp = df.iloc[:,4]

        fig,ax1 = plt.subplots(figsize = (10,5)) #subplots创建图表
        
        ax1.grid(True)#网格线
        
        ax1.plot(times, delta_temp, 'g-',label='delta_temp')
        ax1.set_xlabel('Time')#仅为标签
        ax1.set_ylabel('Delta_Temp', color='g')
        ax1.tick_params('y', colors='g')#设置y轴刻度颜色

        ax2 = ax1.twinx()#建立共享x轴，具有独立y轴的轴系
        ax2.plot(times, temp, 'b-',label='temp')
        ax2.set_ylabel('Temp', color='b')
        ax2.tick_params('y', colors='b')
        plt.show()

    elif material == 'YJBL':

        times = df.iloc[:,0] # 
        delta_temp = df.iloc[:,7]
        temp = df.iloc[:,8]

        fig,ax1 = plt.subplots(figsize = (10,5)) 

        ax1.grid(True)

        ax1.plot(times, delta_temp, 'g-',label='delta_temp')
        ax1.set_xlabel('Time')#仅为标签
        ax1.set_ylabel('Delta_Temp', color='g')
        ax1.tick_params('y', colors='g')

        ax2 = ax1.twinx()#建立共享x轴，具有独立y轴的轴系
        ax2.plot(times, temp, 'b-',label='temp')
        ax2.set_ylabel('Temp', color='b')
        ax2.tick_params('y', colors='b')
        plt.show()


read_excel_and_plot_dual_axis('D:\e\exp1.xlsx' , 'XJ')
read_excel_and_plot_dual_axis('D:\e\exp1.xlsx' , 'YJBL')