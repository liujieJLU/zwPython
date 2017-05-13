# -*- coding: utf-8 -*-
import tushare as ts
import os
import time
class ShiBor(object):
	"""日期格式为YYYY-MM-DD,不要输入2015-2-1(正确输法是2015-02-01)"""
	today_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	index = "..\\file_index\\银行间同业拆放率\\"
	index_shibor_data = 'Shibor拆放利率\\'
	index_shibor_quote_data = '银行报价数据\\'
	index_shibor_ma_data ='Shibor均值数据\\'
	index_lpr_data = '贷款基础利率\\'
	index_lpr_ma_data = 'LPR均值数据\\'
	father_index = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

	def __init__(self, code, startDate, endDate, kType, date):
		self.code = code
		self.startDate = startDate
		self.endDate = endDate
		self.kType = kType
		self.date = date

    # Shibor拆放利率
	def getShiborDate(self):
		file_name = str(self.date)+'_shibor'+'.csv'
		path = self.index + self.index_shibor_data + file_name
		data = ts.shibor_data(year = self.date)
		data.sort('date', ascending=False).head(10)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 银行报价数据
	def getShiborQuoteDate(self):
		file_name = str(self.date)+'_shibor_quote'+'.csv'
		path = self.index + self.index_shibor_quote_data + file_name
		data = ts.shibor_quote_data(year = self.date)
		data.sort('date', ascending=False).head(10)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# Shibor均值数据
	def getShiborMaDate(self):
		file_name = str(self.date)+'_shibor_ma'+'.csv'
		path = self.index + self.index_shibor_ma_data + file_name
		data = ts.shibor_ma_data(year = self.date)
		data.sort('date', ascending=False).head(10)
		data.to_csv(path, encoding='utf-8')
		print(file_name)
	# 基础贷款利率
	def getLPRDate(self):
		file_name = str(self.date)+'_lpr'+'.csv'
		path = self.index + self.index_lpr_data + file_name
		data = ts.lpr_data(year = self.date)
		data.sort('date', ascending=False).head(10)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# LPR均值数据
	def getLPRMaDate(self):
		file_name = str(self.date)+'_lpr_ma'+'.csv'
		path = self.index + self.index_lpr_ma_data + file_name
		data = ts.lpr_ma_data(year = self.date)
		data.sort('date', ascending=False).head(10)
		data.to_csv(path, encoding='utf-8')
		print(file_name)
sb =ShiBor('600848', '2017-01-03', '2017-5-12', 'D',2017)
# sb.getShiborDate()
# sb.getShiborQuoteDate()
# sb.getShiborMaDate()
# sb.getLPRDate()
# sb.getLPRMaDate()