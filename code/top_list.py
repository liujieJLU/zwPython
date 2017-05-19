# -*- coding: utf-8 -*-
import tushare as ts
import os
import time
class TopListData(object):
	"""日期格式为YYYY-MM-DD,不要输入2015-2-1(正确输法是2015-02-01)"""
	today_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	index = "..\\file_index\\龙虎榜数据\\"
	index_top_list = '每日龙虎榜列表\\'
	index_cap_tops_data = '个股上榜统计\\'
	index_broker_tops ='营业部上榜统计\\'
	index_inst_tops = '机构席位追踪\\'
	index_inst_detail = '机构成交明细\\'
	father_index = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

	def __init__(self, code, startDate, endDate, kType):
		self.code = code
		self.startDate = startDate
		self.endDate = endDate
		self.kType = kType

    # 每日龙虎榜列表
	def getTopList(self):
		file_name = self.startDate+'_top_list.csv'
		path = self.index + self.index_top_list + file_name
		data = ts.top_list(date=self.startDate)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 个股上榜统计
	def getCapTops(self):
		file_name = 'cap_tops.csv'
		path = self.index + self.index_cap_tops_data + file_name
		data = ts.cap_tops()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 营业部上榜统计获取最近5、10、30、60日累计买卖次数和金额，参数days,默认day=5）
	def getBrokerTops(self):
		file_name = 'broker_tops.csv'
		path = self.index + self.index_broker_tops + file_name
		data = ts.broker_tops()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 机构席位追踪（获取最近5、10、30、60日累计买卖次数和金额，参数days,默认day=5）
	def getInstTops(self):
		file_name = 'inst_tops.csv'
		path = self.index + self.index_inst_tops + file_name
		data = ts.inst_tops()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 机构成交明细(仅可获取最近一个交易机构)
	def getInstDetail(self):
		file_name = 'inst_detail.csv'
		path = self.index + self.index_inst_detail + file_name
		data = ts.inst_detail()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

tl=  TopListData('600848', '2017-04-11','2015-03-02', 'D')
# tl.getTopList()
# tl.getCapTops()
# tl.getBrokerTops()
# tl.getInstTops()
# tl.getInstDetail()
