# -*- coding: utf-8 -*-
import tushare as ts
import os
import time
class SharesClassData(object):
	"""日期格式为YYYY-MM-DD,不要输入2015-2-1(正确输法是2015-02-01)"""
	today_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	index = "..\\file_index\\股票分类数据\\"
	index_industry_class = '行业分类\\'
	index_concept_calss = '概念分类\\'
	index_area_class ='地域分类\\'
	index_sme_class = '中小板分类\\'
	index_gem_class = '创业板分类\\'
	index_st_class = '风险警示板分类\\'
	index_hs300_class = '沪深300成份\\'
	index_sz50_class = '上证50成份\\'
	index_zz500_class = '中证500成份\\'
	index_terminated_class = '终止上市股票列表\\'
	index_suspended_class = '暂停上市股票列表\\'
	father_index = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

	def __init__(self, code, startDate, endDate, kType):
		self.code = code
		self.startDate = startDate
		self.endDate = endDate
		self.kType = kType

    # 行业分类
	def getIndustryClass(self):
		file_name = 'industry_class.csv'
		path = self.index + self.index_industry_class + file_name
		data = ts.get_industry_classified()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 概念分类
	def getConceptClass(self):
		file_name = 'concept_class.csv'
		path = self.index + self.index_concept_calss + file_name
		data = ts.get_concept_classified()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 地域分类
	def getAreaClass(self):
		file_name = 'area_class.csv'
		path = self.index + self.index_area_class + file_name
		data = ts.get_area_classified()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 中小板分类
	def getSMEClass(self):
		file_name = 'ame_class.csv'
		path = self.index + self.index_sme_class + file_name
		data = ts.get_sme_classified()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 创业板分类
	def getGEMClass(self):
		file_name = 'gem_class.csv'
		path = self.index + self.index_gem_class + file_name
		data = ts.get_gem_classified()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 风险警告板分类
	def getSTClass(self):
		file_name = 'st_class.csv'
		path = self.index + self.index_st_class + file_name
		data = ts.get_st_classified()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 沪深300成份
	def getHS300(self):
		file_name = 'hs300.csv'
		path = self.index + self.index_hs300_class + file_name
		data = ts.get_hs300s()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 上证50成份
	def getSZ50(self):
		file_name = 'sz50.csv'
		path = self.index + self.index_sz50_class + file_name
		data = ts.get_sz50s()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 上证50成份
	def getZZ500(self):
		file_name = 'zz500.csv'
		path = self.index + self.index_zz500_class + file_name
		data = ts.get_zz500s()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 终止上市股票列表
	def getTerminated(self):
		file_name = 'terminated.csv'
		path = self.index + self.index_terminated_class + file_name
		data = ts.get_terminated()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 暂停上市股票列表
	def getSuspended(self):
		file_name = 'suspended.csv'
		path = self.index + self.index_suspended_class + file_name
		data = ts.get_suspended()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

sc =SharesClassData('600848', '2017-05-11','2015-03-02', 'D')
# sc.getIndustryClass()
# sc.getConceptClass()
# sc.getAreaClass()
# sc.getSMEClass()
# sc.getGEMClass()
# sc.getSTClass()
# sc.getHS300()
# sc.getSZ50()
# sc.getZZ500()
# sc.getTerminated()
# sc.getSuspended()