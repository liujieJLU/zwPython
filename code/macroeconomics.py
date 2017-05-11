# -*- coding: utf-8 -*-
import tushare as ts
import os
import time
class Macoreconomics(object):
	"""日期格式为YYYY-MM-DD,不要输入2015-2-1(正确输法是2015-02-01)"""
	today_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	index = "..\\file_index\\宏观经济数据\\"
	index_deposit_rate = '存款利率\\'
	index_loan_rate = '贷款利率\\'
	index_rrr ='存款准备金率\\'
	index_money_supply = '货币供应量\\'
	index_money_supply_bal = '货币供应量（年底余额）\\'
	index_gdp_year = '国内生产总值（年度）\\'
	index_gdp_quarter = '国内生产总值（季度）\\'
	index_gdp_for = '三大需求对GDP贡献\\'
	index_gdp_pull = '三大需求对GDP拉动\\'
	index_gdp_contrib = '三大产业贡献率\\'
	index_cpi = '居民消费价格指数\\'
	index_ppi = '工业品出厂价格指数\\'
	father_index = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

	def __init__(self, code, startDate, endDate, kType):
		self.code = code
		self.startDate = startDate
		self.endDate = endDate
		self.kType = kType

    # 存款利率
	def getDepositRate(self):
		file_name = 'deposit_rate.csv'
		path = self.index + self.index_deposit_rate + file_name
		data = ts.get_deposit_rate()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 存款利率
	def getLoanRate(self):
		file_name = 'loan_rate.csv'
		path = self.index + self.index_loan_rate + file_name
		data = ts.get_loan_rate()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 存款准备金率
	def getRRRRate(self):
		file_name = 'rrr_rate.csv'
		path = self.index + self.index_rrr + file_name
		data = ts.get_rrr()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 货币供应量
	def getMoneySupply(self):
		file_name = 'money_supply.csv'
		path = self.index + self.index_money_supply + file_name
		data = ts.get_money_supply()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 货币供应量(年底余额)
	def getMoneySupplyBal(self):
		file_name = 'money_supply_bal.csv'
		path = self.index + self.index_money_supply_bal + file_name
		data = ts.get_money_supply_bal()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 国内生产总值（年度）
	def getGDPYear(self):
		file_name = 'gdp_year.csv'
		path = self.index + self.index_gdp_year + file_name
		data = ts.get_gdp_year()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 国内生产总值（季度）
	def getGDPQuarter(self):
		file_name = 'gdp_quarter.csv'
		path = self.index + self.index_gdp_quarter + file_name
		data = ts.get_gdp_quarter()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 三大需求对GDP的贡献
	def getGDPFor(self):
		file_name = 'gdp_for.csv'
		path = self.index + self.index_gdp_for + file_name
		data = ts.get_gdp_for()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 三大需求对GDP的拉动
	def getGDPPull(self):
		file_name = 'gdp_pull.csv'
		path = self.index + self.index_gdp_pull + file_name
		data = ts.get_gdp_pull()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 三大需产业贡献率
	def getGDPContrib(self):
		file_name = 'gdp_contrib.csv'
		path = self.index + self.index_gdp_contrib + file_name
		data = ts.get_gdp_contrib()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 居民消费价格指数
	def getCPI(self):
		file_name = 'cpi.csv'
		path = self.index + self.index_cpi + file_name
		data = ts.get_cpi()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

	# 居民消费价格指数
	def getPPI(self):
		file_name = 'ppi.csv'
		path = self.index + self.index_ppi+ file_name
		data = ts.get_ppi()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

mc =Macoreconomics('600848', '2017-05-11','2015-03-02', 'D')
# mc.getDepositRate()
# mc.getLoanRate()
# mc.getRRRRate()
# mc.getMoneySupply()
# mc.getMoneySupplyBal()
# mc.getGDPYear()
# mc.getGDPQuarter()
# mc.getGDPFor()
# mc.getGDPPull()
# mc.getGDPContrib()
# mc.getCPI()
mc.getPPI()
