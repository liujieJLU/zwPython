# -*- coding: utf-8 -*-
import tushare as ts
import os
import time
class HistoryData(object):
	"""日期格式为YYYY-MM-DD,不要输入2015-2-1(正确输法是2015-02-01)"""
	today_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	index = "..\\file_index\\交易数据\\"
	index_hist_data = '历史行情\\'
	index_h_data = '复权数据\\'
	index_today_data ='实时行情\\'
	index_tick_data ='历史分笔\\'
	index_time_data = '实时分笔\\'
	index_today_tick_data = '当日历史分笔\\'
	index_get_index = '大盘指数行情列表\\'
	index_get_sina_dd = '大单交易数据\\'
	father_index = os.path.abspath(os.path.join(os.getcwd(), os.pardir))



	def __init__(self, code, startDate, endDate, kType):
		self.code = code
		self.startDate = startDate
		self.endDate = endDate
		self.kType = kType

    # 获取历史行情数据（get_hist_data的数据从2014年12月8号开始至今）
	def getHistoryData(self):
		file_name = self.code + '_' + self.startDate + '_' + self.endDate + '.csv'
		path = self.index + self.index_hist_data + file_name
		data = ts.get_hist_data(code=self.code, start=self.startDate, end=self.endDate, ktype=self.kType)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 获取复权数据
	def getHData(self):
		file_name = self.code + '_' + self.startDate + '_' + self.endDate + '.csv'
		path = self.index + self.index_h_data + file_name
		data = ts.get_h_data(code=self.code, start=self.startDate, end=self.endDate)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 获取实时行情
	def getTodayData(self):
		file_name = self.today_time + '.csv'
		path = self.index + self.index_today_data + file_name
		data = ts.get_today_all()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 获取某个股票历史分笔信息
	def getTickData(self):
		file_name = self.code + '_' + self.startDate + '.csv'
		path = self.index + self.index_tick_data + file_name
		data = ts.get_tick_data(code=self.code, date=self.startDate)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 获取某个股票实时分笔信息
	def getRealtimeData(self):
		file_name = self.code + '_' + self.startDate + '.csv'
		path = self.index + self.index_time_data + file_name
		data = ts.get_realtime_quotes(self.code)
		data[['code','name','price','bid','ask','volume','amount','time']]
		data.to_csv(path, encoding='utf-8')
		print (file_name)
	
	# 获取当日产生的分笔明细数据
	def getToadyStickData(self):
		file_name = self.code + '_' + self.today_date + '.csv'
		path = self.index + self.index_today_tick_data + file_name
		data = ts.get_today_ticks(code=self.code)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 大盘指数行情表(此方法未测试)
	def getGetIndexData(self):
		file_name = self.today_date + '.csv'
		path = self.index + self.index_get_index + file_name
		data = ts.get_index()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 大单交易数据(默认400手，vol=400)
	def getSinaDdData(self):
		file_name = self.code + '_' + self.startDate + '.csv'
		path = self.index + self.index_get_sina_dd + file_name
		data = ts.get_sina_dd(code = self.code, date = self.startDate)
		data.to_csv(path, encoding='utf-8')
		print(file_name)



hs =  HistoryData('600848', '2017-01-19','2017-05-02', 'D')
# hs.getHistoryData()
# hs.getHData()
# hs.getTodayData()
# hs.getTickData()
# hs.getRealtimeData()
# hs.getToadyStickData()
# hs.getGetIndexData()
# hs.getSinaDdData()