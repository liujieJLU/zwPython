# -*- coding: utf-8 -*-
import tushare as ts
import os
import time
class Macoreconomics(object):
	"""日期格式为YYYY-MM-DD,不要输入2015-2-1(正确输法是2015-02-01)"""
	today_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	index = "..\\file_index\\投资参考数据\\"
	index_profit = '分配预案\\'
	index_forecast_data = '业绩预告\\'
	index_xsg_data ='限售股解禁\\'
	index_fund_holdings = '基金持股\\'
	index_new_stocks = '新股数据\\'
	index_sh_margins = '融资融券（沪市）\\'
	index_sh_margins_details = '融资融券明细数据（沪市）\\'
	index_sz_margins = '融资融券（深市）\\'
	index_sz_margins_details = '融资融券明细数据（深市）\\'
	father_index = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

	def __init__(self, code, startDate, endDate, kType,date, quarter):
		self.code = code
		self.startDate = startDate
		self.endDate = endDate
		self.quarter = quarter
		self.date = date

    # 分配预案（参数：year默认为2014，top默认为25）
	def getProfit(self, number):
		file_name = str(self.date)+'.csv'
		path = self.index + self.index_profit + file_name
		data = ts.profit_data(year = self.date, top=number)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 业绩预告
	def getForecast(self):
		file_name = str(self.date)+'_'+str(self.quarter)+'.csv'
		path = self.index + self.index_forecast_data + file_name
		data = ts.forecast_data(year = self.date, quarter=self.quarter)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 限售股解禁(年月默认为当前年当前月)
	def getXSGData(self,m):
		file_name = str(self.date)+'_'+str(m)+'xsg.csv'
		path = self.index + self.index_xsg_data + file_name
		data = ts.xsg_data(year=self.date, month=m)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 基金持股(年月默认为当前年当前月)
	def getFundHold(self):
		file_name = str(self.date)+'_'+str(self.quarter)+'.csv'
		path = self.index + self.index_fund_holdings + file_name
		data = ts.fund_holdings(year= self.date, quarter= self.quarter)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 新股数据
	def getNewStocks(self):
		file_name = 'new_stocks.csv'
		path = self.index + self.index_new_stocks + file_name
		data = ts.new_stocks()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 沪市融资融券
	def getShMargins(self):
		file_name = self.startDate+'_'+self.endDate+'_sh_margins.csv'
		path = self.index + self.index_sh_margins + file_name
		data = ts.sh_margins(start = self.startDate, end = self.endDate)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 沪市融资融券明细数据(symbol：标的代码，6位数字e.g.600848，默认为空’‘)
	def getShMarginsDetails(self,code):
		file_name = self.startDate+'_'+self.endDate+'_sh_margins_details.csv'
		path = self.index + self.index_sh_margins_details + file_name
		data = ts.sh_margin_details(start = self.startDate, end = self.endDate, symbol=code)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 深市融资融券
	def getSzMargins(self):
		file_name = self.startDate+'_'+self.endDate+'_sz_margins.csv'
		path = self.index + self.index_sz_margins + file_name
		data = ts.sz_margins(start = self.startDate, end = self.endDate)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 沪市融资融券明细数据(symbol：标的代码，6位数字e.g.600848，默认为空’‘)
	def getSzMarginsDetails(self):
		file_name = self.startDate+'_'+self.endDate+'_sz_margins_details.csv'
		path = self.index + self.index_sz_margins_details + file_name
		data = ts.sz_margin_details(date = self.startDate)
		data.to_csv(path, encoding='utf-8')
		print(file_name)


me =Macoreconomics('600848', '2017-01-03', '2017-5-12', 'D',2016, 1)
# me.getProfit(60)
# me.getForecast()
# me.getXSGData(3)
# me.getFundHold()
# me.getNewStocks()
# me.getShMargins()
# me.getShMarginsDetails('601989')
# me.getSzMargins()
# me.getSzMarginsDetails()

