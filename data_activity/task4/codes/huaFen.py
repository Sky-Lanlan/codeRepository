# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:32:55 2018

@author: Lan
"""

import pandas as pd
from datetime import date
from dateutil import parser


off_raw_data = pd.read_csv('data/ccf_offline_stage1_train.csv')
off_raw_data.columns = ['user_id','merchant_id','coupon_id','discount_rate',
                        'distance','date_received','date']

off_test = pd.read_csv('data/ccf_offline_stage1_test_revised.csv')
off_test.columns = ['user_id','merchant_id','coupon_id','discount_rate',
                    'distance','date_received']


#按照时间划分三个特征集
feature3 = off_raw_data[((off_raw_data.date>=20160315)&(off_raw_data.date<=20160630))
        |((~off_raw_data.date.notnull())&(off_raw_data.date_received>=20160315)&
          (off_raw_data.date_received<=20160630))]
feature2 = off_raw_data[((off_raw_data.date>=20160201)&(off_raw_data.date<=20160514))
        |((~off_raw_data.date.notnull())&(off_raw_data.date_received>=20160201)&
          (off_raw_data.date_received<=20160514))]
feature1 = off_raw_data[((off_raw_data.date>=20160101)&(off_raw_data.date<=20160413))
        |((~off_raw_data.date.notnull())&(off_raw_data.date_received>=20160101)&
          (off_raw_data.date_received<=20160413))]


dataset3 = off_test
dataset2 = off_raw_data[(off_raw_data.date_received>=20160515)&
                        (off_raw_data.date_received<=20160615)]
dataset1 = off_raw_data[(off_raw_data.date_received>=20160414)&
                        (off_raw_data.date_received<=20160514)]


# =============================================================================
# off_test['target'] = off_test.apply(addLable,axis=1)
# =============================================================================
# =============================================================================
# c = OneHotEncoder().fit_transform(raw_data['Coupon_id'].values.reshape(-1,1))
# print(c.toarray())
# =============================================================================
#raw_data.to_csv('first.csv')

# 过滤普通消费数据
# =============================================================================
# raw_data = raw_data[raw_data['Coupon_id'].notnull()]  
# =============================================================================
# =============================================================================
# raw_data = raw_data[~raw_data['Coupon_id'].isin(['fixed'])]
# =============================================================================
# 添加标签列target
def addLable(data):
    if data['date']>0:
        return 1
    else:
        return 0
# =============================================================================
# dataset3['label'] = dataset3.apply(addLable,axis=1)
# =============================================================================
dataset2['label'] = dataset2.apply(addLable,axis=1)
dataset1['label'] = dataset1.apply(addLable,axis=1)


############# user related feature   #############
"""
1.user related: 
      count_merchant. 
      user_avg_distance, user_min_distance,user_max_distance. 
      buy_use_coupon. buy_total. coupon_received.
      buy_use_coupon/coupon_received. 
      buy_use_coupon/buy_total
      user_date_datereceived_gap
      
"""



# =============================================================================
# 
# #for dataset3~1
# def user_feature(off_feature,no):
#     user = off_feature[['user_id','merchant_id','coupon_id','discount_rate',
#                         'distance','date_received','date']]
#     
#     t = user[['user_id']]
#     # 删除重复项
#     t.drop_duplicates(inplace=True)
#     
#     #
#     t1 = user[user.coupon_id.notnull()][['user_id']]
#     t2 =t1.groupby(['user_id']).size()
#     index = pd.Series(t2.index)
#     t3 = pd.DataFrame(t2,columns=['user_coupon_total_received'])
#     t3['user_id'] = index.values
#     t = pd.merge(t,t3,on='user_id',how='left')
#     #
#     t1 = user[(user.date_received.notnull()&~user.date.notnull())][['user_id']]
#     t2 =t1.groupby(['user_id']).size()
#     index = pd.Series(t2.index)
#     t3 = pd.DataFrame(t2,columns=['user_coupon_received_not_use'])
#     t3['user_id'] = index.values
#     t = pd.merge(t,t3,on='user_id',how='left')
#     
#     #
#     t1 = user[(user.coupon_id.notnull()&user.date.notnull())][['user_id']]
#     t2 =t1.groupby(['user_id']).size()
#     index = pd.Series(t2.index)
#     t3 = pd.DataFrame(t2,columns=['user_coupon_received_use'])
#     t3['user_id'] = index.values
#     t = pd.merge(t,t3,on='user_id',how='left')
#     
#     #
#     def use_rate(data):
#         return data['user_coupon_received_use']/data['user_coupon_total_received']
#     t['user_coupon_use_rate'] = t.apply(use_rate,axis=1)
#     
#     
#     #
#     t1 = user[user.date_received.notnull()&user.date.notnull()][['user_id','coupon_id']]
#     t1['count'] = 1
#     t2 = t1.groupby(['user_id','coupon_id']).agg('sum').reset_index()
#     t2 = t2.groupby('user_id').agg('max').reset_index()[['user_id','coupon_id']]
#     t2.rename(columns={'coupon_id':'max_coupon_id_use_user'},inplace=True)
#     t = pd.merge(t,t2,on='user_id',how='left')
#     
#     
#     #
#     t1 = user[user.date_received.notnull()&user.date.notnull()][['user_id','merchant_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['count1'] = 1
#     t2 = t1.groupby('user_id').agg('sum').reset_index()[['user_id','count1']]
#     
#     t1 = user[['user_id','merchant_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['count2'] = 1
#     t3 = t1.groupby('user_id').agg('sum').reset_index()[['user_id','count2']]
#     
#     t4 = pd.merge(t2,t3,on='user_id',how='left')
#     
#     def try_refresh(data):
#         return data['count1']/data['count2']
#     
#     t['try_fresh_merchant'] = t4.apply(try_refresh,axis=1)
#     
#     
#     #
#     t1 = user[(user.date_received.notnull()&user.date.notnull())][['user_id','coupon_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['count1'] = 1
#     t2 = t1.groupby('user_id').agg('sum').reset_index()[['user_id','count1']]
#     
#     t1 = user[['user_id','coupon_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['count2'] = 1
#     t3 = t1.groupby('user_id').agg('sum').reset_index()[['user_id','count2']]
#     
#     t4 = pd.merge(t2,t3,on='user_id',how='left')
#     
#     def try_refresh(data):
#         return data['count1']/data['count2']
#     
#     t['try_fresh_coupon'] = t4.apply(try_refresh,axis=1)
#     
#     
#     #
#     
#     t1 = user[(user.date_received.notnull()&user.date.notnull()&user.distance.notnull())]
#     [['user_id','distance']]
#     t2 = t1.groupby('user_id').agg('min').reset_index()
#     t3 = t1.groupby('user_id').agg('max').reset_index()
#     t4 = t1.groupby('user_id').agg('mean').reset_index()
#     
#     t2.rename(columns={'distance':'min_distance_user'},inplace=True)
#     t3.rename(columns={'distance':'max_distance_user'},inplace=True)
#     t4.rename(columns={'distance':'mean_distance_user'},inplace=True)
#     
#     t = pd.merge(t,t2,on='user_id',how='left')
#     t = pd.merge(t,t3,on='user_id',how='left')
#     t = pd.merge(t,t4,on='user_id',how='left')
#     
#         
#     t.to_csv('data/user'+str(no)+'_feature.csv',index=None)
#     
# user_feature(feature3,3)
# user_feature(feature2,2)
# user_feature(feature1,1)
# 
# """
# 2.merchant related: 
#       coupon_total. 
#       coupon_use, coupon_use_rate,max_coupon_id_use_merchant. 
#       have_fresh_user. use_per_user. use_diff_coupon_num.
#       usr_rate_merchant use_per_coupon. 
#       time_gap_per_coupon 
#       max_distance_merchant/mean_distance_merchant/min_distance_merchant
# 
# """
# def merchant_feature(feature,no):
#     merchant = feature[['user_id','merchant_id','coupon_id','distance',
#                         'date_received','date']]
#     t = merchant[['merchant_id']]
#     t.drop_duplicates(inplace=True)
#         
#     t1 = merchant[merchant.date_received.notnull()][['merchant_id']]
#     t1['coupon_total'] = 1
#     t2 = t1.groupby('merchant_id').agg('sum').reset_index()
#     t = pd.merge(t,t2,on='merchant_id',how='left')
#         
#     t1 = merchant[merchant.date_received.notnull()&merchant.date.notnull()]
#     [['merchant_id']]
#     t1['coupon_use'] = 1
#     t2 = t1.groupby('merchant_id').agg('sum').reset_index()
#     t = pd.merge(t,t2,on='merchant_id',how='left')  
#     
#     def coupon_use_rate(data):
#         return data['coupon_use']/data['coupon_total']
#     
#     t['coupon_use_rate'] = t.apply(coupon_use_rate,axis=1)
#         
#         
#     t1 = merchant[merchant.date_received.notnull()&merchant.date.notnull()]
#     [['merchant_id','coupon_id']]
#     t1['count'] = 1
#     t2 = t1.groupby(['merchant_id','coupon_id']).agg('sum').reset_index()
#     t2 = t2.groupby('merchant_id').agg('max').reset_index()[['merchant_id',
#                    'coupon_id']]
#     t2.rename(columns={'coupon_id':'max_coupon_id_use_merchant'},inplace=True)
#     t = pd.merge(t,t2,on='merchant_id',how='left')
#         
#     
#     
#     #
#     t1 = merchant[merchant.date_received.notnull()&merchant.date.notnull()]
#     [['user_id','merchant_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['count1'] = 1
#     t2 = t1.groupby('merchant_id').agg('sum').reset_index()[['merchant_id','count1']]
#       
#     t1 = merchant[['user_id','merchant_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['count2'] = 1
#     t3 = t1.groupby('merchant_id').agg('sum').reset_index()[['merchant_id','count2']]
#         
#     t4 = pd.merge(t2,t3,on='merchant_id',how='left')
#     
#     def try_refresh(data):
#         return data['count1']/data['count2']
#        
#     t['have_fresh_user'] = t4.apply(try_refresh,axis=1)
#         
#     #  
#     t1 = merchant[merchant.date_received.notnull()][['merchant_id','user_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['user_num'] = 1
#     t2 = t1.groupby('merchant_id').agg('sum').reset_index()[['merchant_id','user_num']]
#     t = pd.merge(t,t2,on='merchant_id',how='left')
#     
#     def use_per_user(data):
#         return data['coupon_use']/data['user_num']
#     
#     t['use_per_user'] = t.apply(use_per_user,axis=1)
#     del t['user_num']
#     
#     
#     #
#     t1 = merchant[merchant.date_received.notnull()&merchant.date.notnull()]
#     [['merchant_id','coupon_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['use_diff_coupon_num'] = 1
#     t2 = t1.groupby('merchant_id').agg('sum').reset_index()[['merchant_id',
#                    'use_diff_coupon_num']]
#     t = pd.merge(t,t2,on='merchant_id',how='left')
#     
#     
#     
#     #
#     t1 = merchant[merchant.date_received.notnull()][['merchant_id','coupon_id']]
#     t1.drop_duplicates(inplace=True)
#     t1['send_diff_coupon_num'] = 1
#     t2 = t1.groupby('merchant_id').agg('sum').reset_index()[['merchant_id',
#                    'send_diff_coupon_num']]
#     t = pd.merge(t,t2,on='merchant_id',how='left')
#     
#     def use_rate_merchant(data):
#         return data['use_diff_coupon_num']/data['send_diff_coupon_num']
#     
#     
#     t['usr_rate_merchant'] = t.apply(use_rate_merchant,axis=1)
#     
#     
#     
#     #
#     
#     t1 = merchant[(merchant.date_received.notnull()&merchant.date.notnull()
#     &merchant.distance.notnull())][['merchant_id','distance']]
#     t2 = t1.groupby('merchant_id').agg('min').reset_index()
#     t3 = t1.groupby('merchant_id').agg('max').reset_index()
#     t4 = t1.groupby('merchant_id').agg('mean').reset_index()
#        
#     t2.rename(columns={'distance':'min_distance_merchant'},inplace=True)
#     t3.rename(columns={'distance':'max_distance_merchant'},inplace=True)
#     t4.rename(columns={'distance':'mean_distance_merchant'},inplace=True)
#         
#     t = pd.merge(t,t2,on='merchant_id',how='left')
#     t = pd.merge(t,t3,on='merchant_id',how='left')
#     t = pd.merge(t,t4,on='merchant_id',how='left')
#     
#     
#     
#     #
#     def use_per_coupon(data):
#         return data['coupon_use']/data['send_diff_coupon_num']
#     
#     t['use_per_coupon'] = t.apply(use_per_coupon,axis=1)
#     del t['send_diff_coupon_num']
#     
#     
#     
#     #
#     t1 = merchant[merchant.date_received.notnull()&merchant.date.notnull()]
#     [['merchant_id','date_received','date']]
#     
#     def get_time_gap(data):
#         get_date = parser.parse(str(data['date_received'])[:-2])
#         use_date = parser.parse(str(data['date'])[:-2])
#         
#         return  (use_date - get_date).days
#     
#     t1['time_gap_total'] = t1.apply(get_time_gap,axis=1)
#     t2 = t1[['merchant_id','time_gap_total']].groupby('merchant_id').agg('sum').reset_index()
#     
#     t = pd.merge(t,t2,on='merchant_id',how='left')
#     
#     def time_gap_per_coupon(data):
#         return data['time_gap_total']/data['coupon_use']
#     
#     t['time_gap_per_coupon'] = t.apply(time_gap_per_coupon,axis=1)
#     t.to_csv('data/merchant'+str(no)+'_feature.csv',index=None)
# 
# 
# 
# merchant_feature(feature3,3)
# merchant_feature(feature2,2)
# merchant_feature(feature1,1)
# 
# 
# """
# 3.user_merchant related: 
#       
# 
# """
# def user_merchant_feature(feature,no):
#     user_merchant = feature[['user_id','merchant_id','coupon_id','distance',
#                              'date_received','date']]
#     t = user_merchant[['user_id','merchant_id']]
#     t.drop_duplicates(inplace=True)
#     
#     #
#     t1 = user_merchant[user_merchant.date_received.notnull()][['user_id','merchant_id']]
#     t1['coupon_receive_times'] = 1
#     t2 = t1.groupby(['user_id','merchant_id']).agg('sum').reset_index()
#     t = pd.merge(t,t2,on=['user_id','merchant_id'],how='left')
#     
#     
#     
#     #
#     t1 = user_merchant[user_merchant.date_received.notnull()&
#                        user_merchant.date.notnull()][['user_id','merchant_id']]
#     t1['coupon_receive_use_user_merchant'] = 1
#     t2 = t1.groupby(['user_id','merchant_id']).agg('sum').reset_index()
#     t = pd.merge(t,t2,on=['user_id','merchant_id'],how='left')
#     
#     
#     #
#     t1 = user_merchant[user_merchant.date_received.notnull()
#         &~user_merchant.date.notnull()][['user_id','merchant_id']]
#     t1['coupon_receive_not_use_user_merchant'] = 1
#     t2 = t1.groupby(['user_id','merchant_id']).agg('sum').reset_index()
#     t = pd.merge(t,t2,on=['user_id','merchant_id'],how='left')
#     
#     def coupon_receive_use_user_merchant_rate(data):
#         return data['coupon_receive_use_user_merchant']/data['coupon_receive_times']
#     
#     
#     t['coupon_receive_use_user_merchant_rate'] =  t.apply(coupon_receive_use_user_merchant_rate,axis=1)
#     
#     #
#     t1 = user_merchant[(user_merchant.date_received.notnull()
#         &~user_merchant.date.notnull())][['user_id']]
#     t2 =t1.groupby(['user_id']).size()
#     index = pd.Series(t2.index)
#     t3 = pd.DataFrame(t2,columns=['user_coupon_received_not_use'])
#     t3['user_id'] = index.values
#     t = pd.merge(t,t3,on='user_id',how='left')
#     
#     
#     t1 = user_merchant[(user_merchant.date_received.notnull()
#         &~user_merchant.date.notnull())][['user_id','merchant_id']]
#     t1['user_coupon_received_not_use_per_merchant'] = 1
#     t2 =t1.groupby(['user_id','merchant_id']).agg('sum').reset_index()
#     
#     t = pd.merge(t,t2,on=['user_id','merchant_id'],how='left')
#     
#     def user_coupon_received_not_use_per_merchant_rate(data):
#         return data['user_coupon_received_not_use_per_merchant']/ data['user_coupon_received_not_use']
#     
#     
#     t['user_coupon_received_not_use_per_merchant_rate'] = t.apply(user_coupon_received_not_use_per_merchant_rate,axis=1)
#     
#     
#     del t['user_coupon_received_not_use']
#     
#     
#     #
#     t1 = user_merchant[(user_merchant.date_received.notnull()
#             &user_merchant.date.notnull())][['user_id']]
#     t2 =t1.groupby(['user_id']).size()
#     index = pd.Series(t2.index)
#     t3 = pd.DataFrame(t2,columns=['user_coupon_received_use'])
#     t3['user_id'] = index.values
#     t = pd.merge(t,t3,on='user_id',how='left')
#     
#     
#     t1 = user_merchant[(user_merchant.date_received.notnull()
#             &user_merchant.date.notnull())][['user_id','merchant_id']]
#     t1['user_coupon_received_use_per_merchant'] = 1
#     t2 =t1.groupby(['user_id','merchant_id']).agg('sum').reset_index()
#     
#     t = pd.merge(t,t2,on=['user_id','merchant_id'],how='left')
#     
#     def user_coupon_received_use_per_merchant_rate(data):
#         return data['user_coupon_received_use_per_merchant']/data['user_coupon_received_use']
#     
#     
#     t['user_coupon_received_use_per_merchant_rate'] =  t.apply(user_coupon_received_use_per_merchant_rate,axis=1)
#     
#     
#     #
#     t1 = user_merchant[(user_merchant.date_received.notnull()
#             &~user_merchant.date.notnull())][['merchant_id']]
#     t1['merchant_coupon_received_not_use'] = 1
#     t2 =t1.groupby(['merchant_id']).agg('sum').reset_index()
#     
#     t = pd.merge(t,t2,on=['merchant_id'],how='left')
#     
#     
#     def merchant_coupon_received_not_use_per_merchant_rate(data):
#         return data['user_coupon_received_not_use_per_merchant']/data['merchant_coupon_received_not_use']
#     
#     
#     t['merchant_coupon_received_not_use_per_merchant_rate'] =  t.apply(merchant_coupon_received_not_use_per_merchant_rate,axis=1)
#     
#     
#     #
#     
#     t1 = user_merchant[(user_merchant.date_received.notnull()
#             &user_merchant.date.notnull())][['merchant_id']]
#     t1['merchant_coupon_received_use'] = 1
#     t2 =t1.groupby(['merchant_id']).agg('sum').reset_index()
#     t = pd.merge(t,t2,on='merchant_id',how='left')
#     
#     def merchant_coupon_received_use_per_merchant_rate(data):
#         return data['user_coupon_received_use_per_merchant']/ data['merchant_coupon_received_use']
#     
#     
#     t['merchant_coupon_received_use_per_merchant_rate'] = t.apply(merchant_coupon_received_use_per_merchant_rate,axis=1)
#     
#     
#     del t['user_coupon_received_use_per_merchant']
#     
#     t.to_csv('data/user_merchant'+str(no)+'_feature.csv',index=None)
# 
# 
# 
# user_merchant_feature(feature3,3)
# user_merchant_feature(feature2,2)
# user_merchant_feature(feature1,1)
# 
# '''
# 4.coupon_feature
# 
# '''
# 
# def coupon_feature(feature,no):
#     coupon = feature[feature.coupon_id.notnull()][['user_id','merchant_id',
#                      'coupon_id','discount_rate','date_received','date']]
#     t = coupon[['coupon_id']]
#     t.drop_duplicates(inplace=True)
#     
#     
#     def calc_discount_rate(s):
#         s =str(s['discount_rate'])
#         s = s.split(':')
#         if len(s)==1:
#             return float(s[0])
#         else:
#             return 1.0-float(s[1])/float(s[0])
#     
#             
#         
#         
#     def is_full_cut(data):
#         if ':' in data['discount_rate']:
#             return 1
#         else:
#             return 0
#         
#     
#     t1 = coupon[coupon.coupon_id.notnull()][['coupon_id','discount_rate']]
#     t1.drop_duplicates(inplace=True)
#     t['is_full_cut'] = t1.apply(is_full_cut,axis=1)
#     
#     
#     t1 = coupon[coupon.coupon_id.notnull()][['coupon_id','discount_rate']]
#     t1.drop_duplicates(inplace=True)
#     t['discount_rate_fair'] = t1.apply(calc_discount_rate,axis=1)
#     
#     
#     t1 = coupon[coupon.coupon_id.notnull()][['coupon_id','discount_rate']]
#     t1['coupon_count'] = 1
#     t2 = t1.groupby('coupon_id').agg('sum').reset_index()[['coupon_id','coupon_count']]
#     t = pd.merge(t,t2,on='coupon_id',how='left')
#     
#     
#     t1 = coupon[coupon.coupon_id.notnull()&coupon.date.notnull()][['coupon_id','discount_rate']]
#     t1['coupon_use_count'] = 1
#     t2 = t1.groupby('coupon_id').agg('sum').reset_index()[['coupon_id','coupon_use_count']]
#     t = pd.merge(t,t2,on='coupon_id',how='left')
#     
#     def coupon_use_rate_coupon(data):
#         return data['coupon_use_count']/data['coupon_count']
#     
#     
#     t['coupon_use_rate_coupon'] = t.apply(coupon_use_rate_coupon,axis=1)
#     
#     
#     
#     
#     #
#     t1 = coupon[coupon.date_received.notnull()&coupon.date.notnull()][['coupon_id','date_received','date']]
#     def get_time_gap(data):
#         get_date = parser.parse(str(data['date_received'])[:-2])
#         use_date = parser.parse(str(data['date'])[:-2])
#            
#         return  (use_date - get_date).days
#          
#     t1['time_gap_total'] = t1.apply(get_time_gap,axis=1)
#     t2 = t1[['coupon_id','time_gap_total']].groupby('coupon_id').agg('sum').reset_index()
#     t = pd.merge(t,t2,on='coupon_id',how='left')
#     def time_gap_per_coupon(data):
#         return data['time_gap_total']/data['coupon_use_count']
#       
#     t['time_gap_per_coupon_coupon'] = t.apply(time_gap_per_coupon,axis=1)
#     
#     #
#     t['day_of_week'] = coupon.date_received.astype('str').apply(lambda x:date(int(x[0:4]),int(x[4:6]),int(x[6:8])).weekday()+1)
#     t['day_of_month'] = coupon.date_received.astype('str').apply(lambda x:int(x[6:8]))
#     
#     #
#     
#     t1 = coupon[(coupon.date_received.notnull())][['coupon_id']]
#     t1['coupon_received'] = 1
#     t2 =t1.groupby(['coupon_id']).agg('sum').reset_index()
#     
#     t = pd.merge(t,t2,on='coupon_id',how='left')
#     t.to_csv('data/coupon'+str(no)+'_feature.csv',index=None)
# 
# coupon_feature(feature3,3)
# coupon_feature(feature2,2)
# coupon_feature(feature1,1)
# 
# 
# 
# def user_coupon_feature(feature,no):
#     coupon = feature[feature.coupon_id.notnull()][['user_id','merchant_id',
#                      'coupon_id','date_received','date']]
#     t = coupon[['user_id','coupon_id']]
#     t.drop_duplicates(inplace=True)
#     
#     #
#     t1 = coupon[(coupon.date_received.notnull())][['user_id','coupon_id']]
#     t1['user_coupon_received'] = 1
#     t2 =t1.groupby(['user_id','coupon_id']).agg('sum').reset_index()
#        
#     t = pd.merge(t,t2,on=['user_id','coupon_id'],how='left')
#     
#     #
#     t1 = coupon[(coupon.date_received.notnull()&coupon.date.notnull())]
#     [['user_id','coupon_id']]
#     t1['user_coupon_use'] = 1
#     t2 =t1.groupby(['user_id','coupon_id']).agg('sum').reset_index()
#        
#     t = pd.merge(t,t2,on=['user_id','coupon_id'],how='left')
#     def user_coupon_use_rate(data):
#         return data['user_coupon_use']/data['user_coupon_received']
#     
#     t['user_coupon_use_rate'] = t.apply(user_coupon_use_rate,axis=1)
# 
#     t.to_csv('data/user_coupon'+str(no)+'_feature.csv',index=None)
# 
# 
# user_coupon_feature(feature3,3)
# user_coupon_feature(feature2,2)
# user_coupon_feature(feature1,1)
# 
# 
# 
# =============================================================================

'''
    other_feature
'''



# =============================================================================
# def other_feature(dataset,no):
#     #
#     t = dataset[['user_id']]
#     t['this_month_user_receive_all_coupon_count'] = 1
#     t = t.groupby('user_id').agg('sum').reset_index()
#     
#     
#     #
#     t1 = dataset[['user_id','coupon_id']]
#     t1['this_month_user_receive_same_coupon_count'] = 1
#     t1 = t1.groupby(['user_id','coupon_id']).agg('sum').reset_index()
#     t = pd.merge(t,t1,on='user_id',how='left')
#     
#     #
#     t2 = dataset[['user_id','coupon_id','date_received']]
#     t2.date_received = t2.date_received.astype('str')
#     t2 = t2.groupby(['user_id','coupon_id'])['date_received'].agg(lambda x:':'.join(x)).reset_index()
#     t2['receive_number'] = t2.date_received.apply(lambda s:len(s.split(':')))
#     t2 = t2[t2.receive_number>1]
#     t2['max_date_received'] = t2.date_received.apply(lambda s:max([float(d) for d in s.split(':')]))
#     t2['min_date_received'] = t2.date_received.apply(lambda s:min([float(d) for d in s.split(':')]))
#     t2 = t2[['user_id','coupon_id','max_date_received','min_date_received']]
#     
#     t3 = dataset[['user_id','coupon_id','date_received']]
#     t3 = pd.merge(t3,t2,on=['user_id','coupon_id'],how='left')
#     t3['this_month_user_receive_same_coupon_lastone'] = t3.max_date_received - t3.date_received
#     t3['this_month_user_receive_same_coupon_firstone'] = t3.date_received - t3.min_date_received
#     def is_firstlastone(x):
#         if x==0:
#             return 1
#         elif x>0:
#             return 0
#         else:
#             return -1 
#             
#     t3.this_month_user_receive_same_coupon_lastone = t3.this_month_user_receive_same_coupon_lastone.apply(is_firstlastone)
#     t3.this_month_user_receive_same_coupon_firstone =t3.this_month_user_receive_same_coupon_firstone.apply(is_firstlastone)
#     t3 = t3[['user_id','coupon_id','date_received',
#              'this_month_user_receive_same_coupon_lastone',
#              'this_month_user_receive_same_coupon_firstone']]
#     t = pd.merge(t,t3,on=['user_id','coupon_id'])
#     t1 = dataset[['user_id','date_received']]
#     t1['this_day_user_receive_all_coupon_count'] = 1
#     t1 = t1.groupby(['user_id','date_received']).agg('sum').reset_index()
#     
#     t = pd.merge(t,t1,on=['user_id','date_received'])
#     
#     t1 = dataset[['user_id','coupon_id','date_received']]
#     t1['this_day_user_receive_same_coupon_count'] = 1
#     t1 = t1.groupby(['user_id','coupon_id','date_received']).agg('sum').reset_index()
#     
#     t = pd.merge(t,t1,on=['user_id','coupon_id','date_received'])
#     
#     
#     
#     
#     t1 = dataset[['user_id','coupon_id','date_received']]
#     t1.date_received = t1.date_received.astype('str')
#     t1 = t1.groupby(['user_id','coupon_id'])['date_received'].agg(lambda x:':'.join(x)).reset_index()
#     t1.rename(columns={'date_received':'dates'},inplace=True)
#     
#     def get_day_gap_before(s):
#         date_received,dates = s.split('-')
#         dates = dates.split(':')
#         gaps = []
#         for d in dates:
#             this_gap = (date(int(date_received[0:4]),int(date_received[4:6]),
#                              int(date_received[6:8]))-date(int(d[0:4]),int(d[4:6]),
#                             int(d[6:8]))).days
#             if this_gap>0:
#                 gaps.append(this_gap)
#         if len(gaps)==0:
#             return -1
#         else:
#             return min(gaps)
#             
#     def get_day_gap_after(s):
#         date_received,dates = s.split('-')
#         dates = dates.split(':')
#         gaps = []
#         for d in dates:
#             this_gap = (date(int(d[0:4]),int(d[4:6]),int(d[6:8]))-date(int(date_received[0:4]),
#                              int(date_received[4:6]),int(date_received[6:8]))).days
#             if this_gap>0:
#                 gaps.append(this_gap)
#         if len(gaps)==0:
#             return -1
#         else:
#             return min(gaps)
#         
#     
#     t2 = dataset[['user_id','coupon_id','date_received']]
#     t2 = pd.merge(t2,t1,on=['user_id','coupon_id'],how='left')
#     t2['date_received_date'] = t2.date_received.astype('str') + '-' + t2.dates
#     t2['day_gap_before'] = t2.date_received_date.apply(get_day_gap_before)
#     t2['day_gap_after'] = t2.date_received_date.apply(get_day_gap_after)
#     t2 = t2[['user_id','coupon_id','date_received','day_gap_before','day_gap_after']]
#     t = pd.merge(t,t2,on=['user_id','coupon_id','date_received'])
#     del t['date_received']
#     t.to_csv('data/other'+str(no)+'_feature.csv',index=None)
# 
# 
# 
# other_feature(dataset3,3)
# other_feature(dataset2,2)
# other_feature(dataset1,1)
# =============================================================================


for i in range(1,4):
    other_features = pd.read_csv('data/other'+str(i)+'_feature.csv') 
    coupon1_feature = pd.read_csv('data/coupon1_feature.csv') 
    merchant1_feature = pd.read_csv('data/merchant1_feature.csv') 
    user_coupon1_feature = pd.read_csv('data/user_coupon1_feature.csv') 
    user_merchant1_feature = pd.read_csv('data/user_merchant1_feature.csv') 
    user1_feature = pd.read_csv('data/user1_feature.csv') 
    result = pd.merge(other_features,dataset1,on=['user_id','coupon_id'],how='right')
    result = pd.merge(result,coupon1_feature,on='coupon_id')
    result = pd.merge(merchant1_feature,result,on=['merchant_id'],how='right')
    result = pd.merge(user_coupon1_feature,result,on=['user_id','coupon_id'],how='right')
    result = pd.merge(user_merchant1_feature,result,on=['user_id','merchant_id'],how='right')
    result = pd.merge(user1_feature,result,on=['user_id'],how='right')
    result.to_csv('data/dataset'+str(i)+'.csv')

   








