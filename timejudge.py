# -*- coding: utf-8 -*-
import time
import calendar
class TimeJudge():
    #判断是否为周一
    def isMonday():
        if (0 == time.localtime(time.time()).tm_wday):
            return True
        else:
            return False

	    #判断是否为周二
    def isTuesday():
        if (1 == time.localtime(time.time()).tm_wday):
            return True
        else:
            return False
			
	    #判断是否为周三
    def isWednesday():
        if (2 == time.localtime(time.time()).tm_wday):
            return True
        else:
            return False
			
	    #判断是否为周四
    def isThursday():
        if (3 == time.localtime(time.time()).tm_wday):
            return True
        else:
            return False
			
	    #判断是否为周五
    def isFriday():
        if (4 == time.localtime(time.time()).tm_wday):
            return True
        else:
            return False
			
		    #判断是否为周六
    def isSaturday():
        if (5 == time.localtime(time.time()).tm_wday):
            return True
        else:
            return False
    #判断是否为周日
    def isSunday():
        if (6 == time.localtime(time.time()).tm_wday):
            return True
        else:
            return False

    #判断是否为本月最后一天
    def isEndOfMonth():
        monthRange = calendar.monthrange(time.localtime(time.time()).tm_year, time.localtime(time.time()).tm_mon )[1]
        if (monthRange == time.localtime(time.time()).tm_mday):
            return True
        else:
            return False

    #计算两个时间区间间隔天数，weekend_flag：true表示自然日，false表示工作日（不含除周六日外的节假日）
    #输入日期格式:%Y-%m-%d
    def IntervalDay(start_date, end_date, weekend_flag):
        if (start_date == end_date):
            return True
        start_struct = time.strptime(start_date, "%Y-%m-%d")
        start_ms = time.mktime(start_struct)
        end_struct = time.strptime(end_date, "%Y-%m-%d")
        end_ms =  time.mktime(end_struct)
        if (end_ms < start_ms):
            print("起始日期大于截止日期，输入不符合规则")
            return -1
        else:
            delta_ms = end_ms - start_ms
            delta_day = int(delta_ms / 3600 / 24)
            if weekend_flag:
                return  delta_day
            else:
                delta_week = int(delta_day / 7)
                mod_day = delta_day % 7
                getridday = 0
                #计算非整周部分处于周末的天数
                for i in range(mod_day):
                    if (((time.localtime(start_ms + i * 3600 * 24).tm_wday) == 5) or ((time.localtime(start_ms + i * 3600 * 24).tm_wday) == 6)):
                        getridday += 1
                #整周部分，加非整周部分
                delta_weekday = delta_week * 5 + (mod_day -getridday)
                return delta_weekday

    #获取当前月的自然天数
    def getDayNumOfMonthNow():
        struct_time = time.localtime()
        year = struct_time.tm_year
        month = struct_time.tm_mon
        if (month in [1,3,5,7,8,10,12]):
            return 31
        elif (month in [4,6,9,11]):
            return 30
        else:
            if (calendar.isleap):
                return 29
            else:return 28





