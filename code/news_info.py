# -*- coding: utf-8 -*-
import tushare as ts
import os
import time
class NewsInfo(object):
	"""日期格式为YYYY-MM-DD,不要输入2015-2-1(正确输法是2015-02-01)"""
	today_time = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime(time.time()))
	today_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	index = "..\\file_index\\新闻事件数据\\"
	index_latest_news = '即时新闻\\'
	index_notice = '信息地雷\\'
	index_guba_sina ='新浪股吧\\'
	index_lpr_data = '贷款基础利率\\'
	index_lpr_ma_data = 'LPR均值数据\\'
	father_index = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
	# top 最新消息条数，show_content 是否显示新闻内容
	def __init__(self, code, startDate, endDate, date, top, show_content):
		self.code = code
		self.startDate = startDate
		self.endDate = endDate
		self.date = date
		self.top = top
		self.bool = show_content

    # 即时新闻()
	def getLatestNews(self):
		file_name = 'news_top'+str(self.top)+'.csv'
		path = self.index + self.index_latest_news + file_name
		data = ts.get_latest_news(top = self.top, show_content=self.bool)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 信息地雷
	def getNotice(self):
		file_name = self.code + '_'+ self.startDate +'.csv'
		path = self.index + self.index_notice + file_name
		data = ts.get_notices(code = self.code, date = self.startDate)
		data.to_csv(path, encoding='utf-8')
		print(file_name)

    # 新浪股吧(此方法未成功)
	def getGubaSina(self):
		file_name = 'guba_sina.csv'
		path = self.index + self.index_guba_sina + file_name
		data = ts.guba_sina()
		data.to_csv(path, encoding='utf-8')
		print(file_name)

ni = NewsInfo('000898', '2017-02-08', '2017-5-12', '2017', 80, True)
# ni.getLatestNews()
# ni.getNotice()
ni.getGubaSina()