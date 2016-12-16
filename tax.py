#!/usr/bin/env python
# encoding: utf-8

# 各项保险费，公积金统一计算可能还有问题
# 北京市公积金租房应该也算一项福利
import sys

# 分档计税
def calc_base(base,t,idx):
    s=0
    for i in xrange(idx):
        s+=base[i]*t[i]
    return s

# 每月所得税
def calc_tax_month(num):
    num-=3500
    # 剔除上一档的扣税基准
    base= [1500,3000,4500,26000,20000,25000]
    t   = [0.03, 0.1, 0.2, 0.25, 0.3,0.35,0.45]
    tax = 0
    if num <=0:
        tax = 0
    elif num <= 1500:
        tax=num*0.03
    elif num>1500 and num<=4500:
        tax=(num-1500)*t[1]+calc_base(base,t,1)
    elif num>4500 and num<=9000:
        tax=(num-4500)*t[2]+calc_base(base,t,2)
    elif num>9000 and num<=35000:
        tax=(num-9000)*t[3]+calc_base(base,t,3)
    elif num>35000 and num<=55000:
        tax=(num-35000)*t[4]+calc_base(base,t,4)
    elif num>55000 and num<80000:
        tax=(num-55000)*t[5]+calc_base(base,t,5)
    else:
        tax=(num-8000)+t[6]+calc_base(base,t,6)
    return tax

# 年终奖所得税
# 单独作为一个月工资
# base 月薪
# m_num 奖金月数
# mons 分为年中，年终对应的月份
def calc_tax_year_std(base, m_num, mons):
    # 速算扣除数，可能按照税率变化
    susuan = [0,105,555,1005,2755,5505,13505]
    # 现行税率
    t = [0.03,0.1,0.2,0.25,0.3,0.35,0.45]
    # 缴税基准
    std = [1500,4500,9000,35000,55000,80000]

    base_mon = base * m_num
    calc_type = -1
    if base>3500:
        base_mon /= (mons*1.0)
        calc_type = 0
    else:
        base_mon = (base_mon-3500.0+base)/mons
        calc_type = 1

    # 确定缴税区间
    idx = 0
    for i in std:
        if base_mon<i:
            break
        idx+=1

    tax = 0
    # 平均每月奖金高于3500
    if calc_type == 0:
        tax = base * m_num * t[idx] - susuan[idx]
    elif calc_type == 1:
        tax = (base * m_num - 3500.0 + base) * m_num * t[idx] -susuan[idx]
    return tax

# 计算公积金,需要按照本市平均工资核算
def calc_common(base,v):
    return base * v

# 计算每月的薪资情况
# 扣除各项保险金额
def profit(num,secure):
    total = num
    #comm = calc_common(num,v)
    #num -= comm
    tax = calc_tax_month(num-secure)
    real = num - tax
    print "税前工资:%f\n缴税总额:%f\n税后工资:%f\n" %(round(total,2),round(tax,2),round(real,2),)

# 计算实际年薪、总缴税额
# secure 每月保险公积金总额
# mid_mons 年中奖月份
# final_mons 年终奖月份
def benifit_year(base,secure,mid_mons,final_mons):
    tax = 0
    mons = mid_mons+final_mons
    tot = base * (mons+12)

    if mid_mons<1e-5: # 奖金一次性发放
        tax = calc_tax_month(base-secure)*12 + calc_tax_year_std(base,mons,12)
    else: #奖金分为年中、年终两次发放
        tax = calc_tax_month(base-secure)*12 + calc_tax_year_std(base,mid_mons,6) + calc_tax_year_std(base,final_mons,12)
    return tax,tot - tax

if __name__ == '__main__':
    if len(sys.argv)<5:
        print "usage:%s 月薪B 每月扣除费f 年中奖月份m 年终奖月份M" %(sys.argv[0],)
        sys.exit(1)

    base = float(sys.argv[1])
    sec = float(sys.argv[2])
    mon = float(sys.argv[3])
    year = float(sys.argv[4])
    print '*'*6,"每月情况",'*'*6
    profit(base,sec)
    print '*'*6,"年终情况",'*'*6
    tax,real = benifit_year(base,sec,mon,year)
    print "个人所得税:%f\n实际收入:%f\n" %(tax,real,)
