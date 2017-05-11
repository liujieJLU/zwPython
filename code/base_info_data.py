# -*- coding: utf-8 -*-
import tushare as ts
import os
import time
class BascisInfoData(object):
	"""日期格式为YYYY-MM-DD,不要输入2015-2-1(正确输法是2015-02-01)"""
	today_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	index = "..\\file_index\\基本面数据\\"
	index_stock_basic = '股票列表\\'
	index_report_data = '业绩报告\\'
	index_profit_data ='盈利能力\\'
	index_operation_data = '营运能力\\'
	index_growth_data = '成长能力\\'
	index_debtpaying_index = '偿债能力\\'
	index_cashflow_index = '现金流量\\'
	father_index = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

	def __init__(self, code, startDate, endDate, kType):
		self.code = code
		self.startDate = startDate
		self.endDate = endDate
		self.kType = kType


    # 获取沪深上市公司基本情况
	def getStockBasics(self):
		file_name = 'stock_basic.csv'
		path = self.index + self.index_stock_basic + file_name
		data = ts.get_stock_basics()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 业绩报告（参数为XX年第几季度1,2,3,4）
	def getReportData(self, year, quarter):
		file_name = str(year)+'_'+str(quarter)+'.csv'
		path = self.index + self.index_report_data + file_name
		data = ts.get_report_data(year, quarter)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 盈利能力（参数为XX年第几季度1,2,3,4）
	def getProfitData(self, year, quarter):
		file_name = str(year)+'_'+str(quarter)+'.csv'
		path = self.index + self.index_profit_data + file_name
		data = ts.get_profit_data(year, quarter)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 营运能力（参数为XX年第几季度1,2,3,4）
	def getOperationData(self, year, quarter):
		file_name = str(year)+'_'+str(quarter)+'.csv'
		path = self.index + self.index_operation_data + file_name
		data = ts.get_operation_data(year, quarter)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 成长能力（参数为XX年第几季度1,2,3,4）
	def getGrowthData(self, year, quarter):
		file_name = str(year)+'_'+str(quarter)+'.csv'
		path = self.index + self.index_growth_data + file_name
		data = ts.get_growth_data(year, quarter)
		data.to_csv(path, encoding='utf-8')
		print(file_name)


	# 偿债能力（参数为XX年第几季度1,2,3,4）
	def getdebtPayData(self, year, quarter):
		file_name = str(year)+'_'+str(quarter)+'.csv'
		path = self.index + self.index_debtpaying_index + file_name
		data = ts.get_debtpaying_data(year, quarter)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 现金流量（参数为XX年第几季度1,2,3,4）
	def getCashflowData(self, year, quarter):
		file_name = str(year)+'_'+str(quarter)+'.csv'
		path = self.index + self.index_cashflow_index + file_name
		data = ts.get_cashflow_data(year, quarter)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

hs =  BascisInfoData('600848', '2017-05-04','2015-03-02', 'D')
# hs.getStockBasics()
# hs.getReportData(2017, 1)
# hs.getProfitData(2017, 1)
# hs.getOperationData(2017, 1)
# hs.getGrowthData(2017, 1)
# hs.getdebtPayData(2017, 1)
# hs.getCashflowData(2017, 1)