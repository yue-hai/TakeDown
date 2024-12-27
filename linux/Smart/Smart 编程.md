# 零、进入练习服务器

## 1、服务器 IP

1. 打开 ttermpro
2. 输入 Ip：172.20.2.55
3. 端口号：22

## 2、服务器用户名密码

1. 账号：creat
2. 密码：creat1234

## 3、进入容器

1. 进入 smartedu-batch_pj 文件夹

```shell
cd workspace/smartedu-batch_pj
```

2. 使用 `make` 命令进入容器

```shell
[creat@BigData01 smartedu-batch_pj]$ make
docker-compose exec  -e COLUMNS="`tput cols`" -e LINES="`tput lines`" myservice bash; 
[trial@smartedu ~]$ 
```

3. 查看容器内是否有新的 smart 指令

```shell
[trial@smartedu ~]$ which lstd
/home/SMART/lstd
```

4. 退出容器

```shell
[trial@smartedu ~]$ exit
exit
[creat@BigData01 smartedu-batch_pj]$ 
```

5. 查看容器外是否有新的 smart 指令

```shell
[creat@BigData01 smartedu-batch_pj]$ which latd
/usr/bin/which: no latd in (/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/root/command:/opt/jdk1.8/bin:/opt/hadoop-2.8.5/bin:/opt/hadoop-2.8.5/sbin:/opt/zookeeper-3.4.6/bin:/opt/apache-hive-1.2.1-bin/bin::/home/creat/.local/bin:/home/creat/bin)
[creat@BigData01 smartedu-batch_pj]$ 
```

# 一、脚本命名

## 1、売上（销售）数据：`CHUPDATE_*`

`CHUPDATE_HIBETU_CHOKUEI.DAYDWH.URE`
`CHUPDATE_这个脚本是做什么处理的.做日别的DWH的数据.数据类型`

1. `URE`：卖上（销售）数据

## 2、予算（预算）数据：

`CHUPDATE_HIBETU_URE.DAYDM.YOSAN`

## 3、自动执行脚本：`DATAMASTER_KYAKUSU_CHOKUEI.DAYDWH.URE`

1. 称为：job
2. 最外层的执行脚本，用来调用其他脚本

# 二、学习课题 1：卖上、予算数据做成

## 1、卖上数据做成

### ①、脚本说明

1. `CHUPDATE_HIBETU_CHOKUEI.DAYDWH.URE`：卖上数据做成的处理脚本
2. `DATAMASTER_KYAKUSU_CHOKUEI.DAYDWH.URE`：用来调用其他脚本的总脚本

### ②、需求

[课题1（DWH数据清洗）.xlsx](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2FSmart%2Fattachments%2F课题1（DWH数据清洗）.xlsx)

### ③、步骤

1. 根据传入的参数在 対象日リスト 中查找以这个参数命名的文件，查看这个文件中有哪些日期，根据文件中的日期遍历 販売明細 文件，做成目标数据
2. 从原数据中抽取出所需列和 10.JAN（用来连接其他表） 后，计算 11.値割金額(税抜き)、13.システムロス金額(税抜き)
3. 根据需求对指定列取整
4. 使用 10.JAN 和 /DWH/TBL/JAN_BUMON rjoin 连接，得到 部門CD
5. 删除掉不需要的列（其实不需要手动删，下一步 sumup 求和时不指定就会自动删除）
6. 使用 sumup 命令以 1.部门CD  2.拠点CD 3.売上日 为主键，求和后面的数据；即每一天的数据总和
7. 插入 4.更新日付
8. 压缩保存
9. --------------------------------
10. 同样方法得到 LINECD 和 DIVCD

### ④、脚本：`CHUPDATE_HIBETU_CHOKUEI.DAYDWH.URE`

[课题1（DWH数据清洗）.zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2FSmart%2Fattachments%2F课题1（DWH数据清洗）.zip)

```shell
#!/bin/bash -xv
#
# CHUPDATE_HIBETU_CHOKUEI.DAYDWH.URE >>> 日別商品階層別店別売上
#
# Usage : CHUPDATE_HIBETU_CHOKUEI.DAYDWH.URE <YYYYMMDD>
#
# Written by Jiang baidong
# Date : 2022/08/24

# 引き数の確認
if [ $# -eq 0 ] ; then
    # 更新日付
    sday=$(date +%Y%m%d)
else
    # 復旧日付
    sday=$1
fi

HOME=/home/trial
# 走行ログの記録
echo   "${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}" &> /dev/null
exec 2> ${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}

#/////////////////////////////////////////////////////////////////////////
# 初期設定
#/////////////////////////////////////////////////////////////////////////
# パスの定義
export PATH=/home/SMART:/home/SMART_TRIAL:/usr/local/bin:${PATH}
export LANG=ja_JP.UTF-8

# 変数の定義
# 一時ファイルパス
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d%H%M%S)
# ログパス
logd=${HOME}/LOG
# セマフォパス
semd=${HOME}/SEMAPHORE
# 共通テーブルディレクトリ
tbld=/DWH/TBL
# Level3ディレクトリ
lv3d=/DWH/LV3/URE

# 簡易YYYYMMDD日付チェック
date +%Y%m%d -d "${sday}" >/dev/null
[ $? -ne 0 ] && { echo "Parameter DATE error:[${sday}]" ; exit 1 ; }

# エラー時の終了処理定義
ERROR_EXIT(){
    touch ${semd}/$(basename $0).${HOSTNAME}.ERROR.${sday}
    rm -rf ${tmp}-* 2>/dev/null
    exit 1
}

# 開始時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} START $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.START.${sday}

#/////////////////////////////////////////////////////////////////////////
# 処理部
#/////////////////////////////////////////////////////////////////////////

# ----判断目录是否存在，不存在就创建该目录
mkdir -p "${lv3d}"/10222148/HIBETU_BUMON_CHOKUEI
mkdir -p "${lv3d}"/10222148/HIBETU_LINE_CHOKUEI
mkdir -p "${lv3d}"/10222148/HIBETU_DIV_CHOKUEI

# ---- 根据传入的参数读取当日更新了哪几天
zcat "${lv3d}"/HANBAI_DAYLIST/"${sday}".gz                      |
# ---- 去重
kuniq -k1                                                       |
# ---- 遍历
while read day ; do
    # ---- 判断文件是否存在，不存在就跳过本次循环
    [ -e "${lv3d}"/HANBAI_MEISAI/"${day}".gz ]                  || continue

    # ---- 每天各个部门的销售数据
    # 日別部門別売上
    zcat "${lv3d}"/HANBAI_MEISAI/"${day}".gz                    |
    # 1.売上日 2.拠点CD 3.レジ番号 4.取引番号 5.営業日 6.取引明細番号
    # 7.更新日付 8.売上日時 9.顧客CD 10.JAN 11.計上会社CD 12.固定部門
    # 13.原単額 14.売単価 15.原価額 16.売上数量 17.売上金額 18.売上金額（税抜き）
    # 19.値割数量 20.値割金額 21.システムロス金額

    # ---- 筛选第 11 列 等于 0001 的数据
    selrow -e '$11==0001'                                           |
    
    # ---- 抽取指定的列
    selcol -c10 -c12 -c2 -c1 -c15,21                                 |
    # 1.JAN 2.固定部門 3.拠点CD 4.売上日 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額

    # ---- 税率=(売上金額 - 売上金額（税抜き）) / 売上金額（税抜き）=($7-$8)/$8
    # ---- 计算税率，放到最后一行（第12行）
    awk '{print $0,$8==0?0:sprintf("%.8f",($7-$8)/$8)}'             |
    # 1.JAN 2.固定部門 3.拠点CD 4.売上日 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11システムロス金額 12.税率

    # ---- 计算 値割金額(税抜き)，放到最后一行（第13行），値割金額(税抜き)=値割金額 / 税率
    awk '{print $0,(1+$12)==0?0:sprintf("%.8f",$10/(1+$12))0}'      |
    # 1.JAN 2.固定部門 3.拠点CD 4.売上日 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額 12.税率
    # 13.値割金額(税抜き) 

    # ---- 计算 システムロス金額(税抜き) ，放到最后一行（第14行），システムロス金額(税抜き) = システムロス金額 / 税率
    awk '{print $0,(1+$12)==0?0:sprintf("%.8f",$11/(1+$12))}'       |
    # 1.JAN 2.固定部門 3.拠点CD 4.売上日 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額 12.税率
    # 13.値割金額(税抜き)  14.システムロス金額(税抜き)

    # ---- 四舍五入取整：
    round -tA -c6.0 -c7.0 -c8.0 -c9.0 -c10.0 -c11.0                 |
    # ---- 向上取整：
    round -tB -c13.0 -c14.0                                         |

    # ----删掉税率的那一列
    delcol -c12                                                     |
    # 1.JAN 2.固定部門 3.拠点CD 4.売上日 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額
    # 12.値割金額(税抜き)  13.システムロス金額(税抜き)

    # ----排序
    ssort -k1                                                       |

    # ----rjoin 连接 JAN_BUMON 表
    hrjoin_default -k1 -M2 -i"****" -c2 "${tbld}"/JAN_BUMON -       |
    # 1.JAN 2.部门CD 3.固定部門 4.拠点CD 5.売上日 6.原価額 7.売上数量 8.売上金額
    # 9.売上金額（税抜き）10.値割数量 11.値割金額 12.システムロス金額 
    # 13.値割金額(税抜き)  14.システムロス金額(税抜き)

    # ----删掉第 1 列和第 3 列
    delcol -c1 -c3                                                  |
    # 1.部门CD  2.拠点CD 3.売上日 4.原価額 5.売上数量 6.売上金額
    # 7.売上金額（税抜き）8.値割数量 9.値割金額 10.システムロス金額 
    # 11.値割金額(税抜き)  12.システムロス金額(税抜き)

    # ----排序
    ssort -k1,3                                                     |   

    # ----以 1、2、3 列为主键求和
    sumup -k1,3 -c4,12                                              |

    # ---- 插入更新时间
    insstr -i"${sday}" -c4                                          |
    # 1.部门CD  2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額 
    # 12.値割金額(税抜き)  13.システムロス金額(税抜き)

    # ----压缩
    gzip -f                                                         >"${lv3d}"/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz
    # ----抓错
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    # ---- 每天各个ライン的销售数据；在上面的基础上进行
    # 日別ライン別売上
    zcat "${lv3d}"/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz         |
    # 1.部门CD  2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額 
    # 12.値割金額(税抜き)  13.システムロス金額(税抜き)

    # ----rjoin 连接 BUMON_LINE 表
    hrjoin_default -k1 -M2 -i"9999" "${tbld}"/BUMON_LINE -           |
    # 1.部门CD 2.ラインCD 3.拠点CD 4.売上日 5.更新日付 6.原価額 7.売上数量 8.売上金額
    # 9.売上金額（税抜き）10.値割数量 11.値割金額 12.システムロス金額 
    # 13.値割金額(税抜き)  14.システムロス金額(税抜き)

    # ----排序
    ssort -k2,5                                                      |

    # ----以 2、3、4、5 列为主键求和
    sumup -k2,5 -c6,14                                               |
    # 1.ラインCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額 
    # 12.値割金額(税抜き)  13.システムロス金額(税抜き)

    # ----压缩
    gzip -f                                                         >"${lv3d}"/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz
    # ----抓错
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    # ---- 每天各个ディビジョンCD的销售数据；在上面的基础上进行
    # 日別ディビジョンCD別売上
    zcat "${lv3d}"/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz         |
    # 1.ラインCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額 
    # 12.値割金額(税抜き)  13.システムロス金額(税抜き)

    # rjoin 连接 LINE_DIV 表
    hrjoin_default -k1 -M2 -i"9999" "${tbld}"/LINE_DIV -           |
    # 1.ラインCD 2.ディビジョンCD 3.拠点CD 4.売上日 5.更新日付 6.原価額 7.売上数量 8.売上金額
    # 9.売上金額（税抜き）10.値割数量 11.値割金額 12.システムロス金額 
    # 13.値割金額(税抜き)  14.システムロス金額(税抜き)

    # ----排序
    ssort -k2,5                                                      |

    # ----以 2、3、4、5 列为主键求和
    sumup -k2,5 -c6,14                                               |
    # 1.ディビジョンCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.システムロス金額 
    # 12.値割金額(税抜き)  13.システムロス金額(税抜き)

    # ----压缩
    gzip -f                                                         >"${lv3d}"/10222148/HIBETU_DIV_CHOKUEI/"${day}".gz
    # ----抓错
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    exit 0
:;done

# 抓错
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} END $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.END.${sday}

# 終了
rm -rf ${tmp}-* 2>/dev/null

exit 0

```

## 2、予算数据做成

### ①、脚本说明

1. `CHUPDATE_HIBETU_URE.DAYDM.YOSAN`：卖上数据做成的处理脚本

### ②、需求

[课题2_(DWH_LV4)数据做成.xlsx](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2FSmart%2Fattachments%2F课题2_(DWH_LV4)数据做成.xlsx)

### ③、步骤

1. 根据传入的日期（年月）在查找 `"${lv3d}"/URE_YOSAN_EIGYO_MONTHLIST/` 目录下以这个日期（年月）命名的文件，查看这个文件中有哪些日期，根据文件中的日期遍历 `"${lv3d}"/URE_YOSAN_EIGYO/` 下的文件，做成目标数据
2. 读取 `"${lv3d}"/URE_YOSAN_EIGYO` 下以指定日期命名的文件，排序，与 `"${lv3d}"/URE_YOSAN_SIKO/` 下以指定日期命名的文件 `ojoin_default` 连接：1:部門CD 2:店舗CD 3:売上日 4:更新日付 5:当日営業予算 6:更新日付 7:当日執行予算
3. 删除两个更新日付列：1:部門CD 2:店舗CD 3:売上日 4:当日営業予算 5:当日執行予算
4. 计算一个月每天的累积和：1:部門CD 2:店舗CD 3:売上日 4:当日営業予算 5.累計営業予算 6:当日執行予算 7.累計執行予算
5. 

6. 1
7. 1
8. 1
9. 1
10. 

11. 压缩保存
12. --------------------------------
13. 同样方法得到 LINECD 和 DIVCD

### ④、脚本：`CHUPDATE_HIBETU_URE.DAYDM.YOSAN`

[课题2_(DWH_LV4%20数据做成).zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2FSmart%2Fattachments%2F课题2_(DWH_LV4%20数据做成).zip)

```shell
#!/bin/bash -xv
#
# CHUPDATE_HIBETU_URE.DAYDM.YOSAN  >>> 日別商品階層別売上予算
# 
# Usage : CHUPDATE_HIBETU_URE.DAYDM.YOSAN <YYYYMMDD>
#
# Written by Cui changjian
# Date : 2022/08/31

if [ $# -eq 0 ] ; then
    # 更新日付
    sday=$(date +%Y%m%d)
else
    # 復旧日付
    sday=$1
fi

HOME=/home/trial
# 走行ログの記録
echo   "${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}" &> /dev/null
exec 2> ${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}

#/////////////////////////////////////////////////////////////////////////
# 初期設定
#/////////////////////////////////////////////////////////////////////////
# パスの定義
export PATH=/home/SMART:/home/SMART_TRIAL:/usr/local/bin:${PATH}
export LANG=ja_JP.UTF-8

# 変数の定義
# 一時ファイルパス
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d%H%M%S)
# ログパス
logd=${HOME}/LOG
# セマフォパス
semd=${HOME}/SEMAPHORE
# 共通テーブルディレクトリ
tbld=/DWH/TBL
# Level3ディレクトリ
lv3d=/DWH/LV3/YOSAN

# 簡易YYYYMMDD日付チェック
date +%Y%m%d -d "${sday}" >/dev/null
[ $? -ne 0 ] && { echo "Parameter DATE error:[${sday}]" ; exit 1 ; }

# エラー時の終了処理定義
ERROR_EXIT(){
    touch ${semd}/$(basename $0).${HOSTNAME}.ERROR.${sday}
    rm -rf ${tmp}-* 2>/dev/null
    exit 1
}

# 開始時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} START $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.START.${sday}

#/////////////////////////////////////////////////////////////////////////
# 処理部
#/////////////////////////////////////////////////////////////////////////

# ----判断目录是否存在，不存在就创建该目录
mkdir -p "${lv3d}"/10222148/HIBETU_BUMON_URE_YOSAN
mkdir -p "${lv3d}"/10222148/HIBETU_LINE_URE_YOSAN
mkdir -p "${lv3d}"/10222148/HIBETU_DIV_URE_YOSAN
mkdir -p "${lv3d}"/10222148/URE_YOSAN_EIGYO_DAYLIST

# 将存放 売上日 数据的表清空，以免数据出错
:>"${tmp}"-day_list

# ---- 根据传入的参数读取当日更新了哪几个月
# 予算MONTHリストから対象データ取得
zcat "${lv3d}"/URE_YOSAN_EIGYO_MONTHLIST/"${sday}".gz           |
# 1.年月

# 行变列
tov                                                             |
# 1.年月

# 去重
kuniq -k1                                                       |

# 根据读取的月份进行循环；做每天的数据
while read month ; do

    # ---- 判断文件是否存在，不存在就跳过本次循环
    # 日別売上営業予算
    [ -e "${lv3d}"/URE_YOSAN_EIGYO/"${month}".gz ]              || continue
    # 日別売上執行予算
    [ -e "${lv3d}"/URE_YOSAN_SIKO/"${month}".gz ]               || continue

    # ---- 读取每月的各个店每天的营业数据；求 累計営業予算、累計執行予算
    # 日別部門別売上
    zcat "${lv3d}"/URE_YOSAN_EIGYO/"${month}".gz                  |
    # 1:部門CD 2:店舗CD 3:売上日 4:更新日付 5:当日営業予算

    # ---- 排序
    ssort -k1,3                                                   |

    # ----rjoin 连接两个表；URE_YOSAN_EIGYO、URE_YOSAN_SIKO
    ojoin_default -k1,3 -M5 -M5 -i"0" - <(zcat "${lv3d}"/URE_YOSAN_SIKO/"${month}".gz | ssort -k1,3)    |
    # 1:部門CD 2:店舗CD 3:売上日 4:更新日付 5:当日営業予算 6:更新日付 7:当日執行予算

    # 删除两个 更新日付 列
    delcol -c4 -c6                                                |
    # 1:部門CD 2:店舗CD 3:売上日 4:当日営業予算 5:当日執行予算

    # 计算一个月每天的累积和
    # 计算 累計営業予算、累計執行予算
    addup -c1,2 -c4,5                                             >"${tmp}"-HIBETU_BUMON_URE_YOSAN-6-9
    # 1:部門CD 2:店舗CD 3:売上日 4:当日営業予算 5.累計営業予算 6:当日執行予算 7.累計執行予算

    # ----抓错
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    # ---- 读取刚才创建的临时表的文件，求 当月営業予算、当月執行予算
    ojoin_default -k1,3 -M7 -M5 -i"0" "${tmp}"-HIBETU_BUMON_URE_YOSAN-6-9 <(selcol -c1,3 -c4 -c6 "${tmp}"-HIBETU_BUMON_URE_YOSAN-6-9 | sumup -k1,3 -c4,5) |
    # 1:部門CD 2:店舗CD 3:売上日 4:当日営業予算 5.累計営業予算 6:当日執行予算 7.累計執行予算 8.当月営業予算 9.当月執行予算

    # 更改列顺序
    selcol -c1,5 -c8 -c6,7 -c9                                     |
    # 1:部門CD 2:店舗CD 3:売上日 4:当日営業予算 5.累計営業予算 6.当月営業予算 7:当日執行予算 8.累計執行予算 9.当月執行予算

    # ----插入更新时间
    # 4:更新日付 
    insstr -i"${sday}" -c3                                         |
    # 1:部門CD 2:店舗CD 3:売上日 4:更新日付 5:当日営業予算 6.累計営業予算 7.当月営業予算 8:当日執行予算 9.累計執行予算 10.当月執行予算

    # 排序；根据 3.売上日、1.部門CD、2.店舗CD，因为要根据第 3 列分割
    ssort -k3@1@2                                                  |

    # 将排序后的数据放到一个临时表中，用以做 売上日 的数据；不会影响后面命令的运行
    tee "${tmp}"-bumon_yosan                                       |

    # ----压缩，根据第 3 列分割；做每天的数据
    fsplit -z                                                       "${lv3d}"/10222148/HIBETU_BUMON_URE_YOSAN/%3.gz
    # ----抓错
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    # 将本次循环中创建的 売上日 的临时表的数据，追加到总 売上日 的临时表中，用以做总 売上日 的数据；只要第 3 列 売上日 
    kuniq -k3 "${tmp}"-bumon_yosan                                  >>"${tmp}"-day_list
    # 1.売上日

    # ----抓错
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT

:;done
# ----抓错
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT



# 将总 売上日 临时表的数据去重、压缩；这个文件代表：文件名的日期这一天更新了那些天的数据
kuniq -k1 "${tmp}"-day_list                                         |
# 1.売上日

# ----压缩
gzip -f                                                             >"${lv3d}"/10222148/URE_YOSAN_EIGYO_DAYLIST/"${sday}".gz
# ----抓错
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


# 读取总 売上日 的数据
zcat "${lv3d}"/10222148/URE_YOSAN_EIGYO_DAYLIST/"${sday}".gz        |
# 1.売上日

# 根据总 売上日 的数据进行循环
while read day ; do

    # 根据读取的每天的日期，读取刚才做的每天的数据
    zcat "${lv3d}"/10222148/HIBETU_BUMON_URE_YOSAN/"${day}".gz      |
    # 1:部門CD 2:店舗CD 3:売上日 4:更新日付 5:当日営業予算 6.累計営業予算 7.当月営業予算 8:当日執行予算 9.累計執行予算 10.当月執行予算

    # ----rjoin 连接 BUMON_LINE 表；获取 ラインCD
    hrjoin_default -k1 -M2 -i"0031" "${tbld}"/BUMON_LINE -          |
    # 1:部門CD 2.ラインCD 3:店舗CD 4:売上日 5:更新日付 6:当日営業予算 7.累計営業予算 8.当月営業予算 9:当日執行予算 10.累計執行予算 11.当月執行予算
    
    # 删掉第 1 列、求和避免 hrjoin 连接后有重复
    sumup -k2,4 -c5,10                                              |
    # 1.ラインCD 2:店舗CD 3:売上日 4:更新日付 5:当日営業予算 6.累計営業予算 7.当月営業予算 8:当日執行予算 9.累計執行予算 10.当月執行予算
    
    # ----压缩
    gzip -f                                                         >"${lv3d}"/10222148/HIBETU_LINE_URE_YOSAN/"${day}".gz
    # ----抓错
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    # 根据读取的每天的日期，读取刚才做的 ラインCD 的每天的数据
    zcat "${lv3d}"/10222148/HIBETU_LINE_URE_YOSAN/"${day}".gz      |
    # 1.ラインCD 2:店舗CD 3:売上日 4:更新日付 5:当日営業予算 6.累計営業予算 7.当月営業予算 8:当日執行予算 9.累計執行予算 10.当月執行予算
    
    # ----rjoin 连接 BUMON_LINE 表；获取 ディビジョンCD
    hrjoin_default -k1 -M2 -i"0016" "${tbld}"/LINE_DIV -            |
    # 1.ラインCD 2.ディビジョンCD 3:店舗CD 4:売上日 5:更新日付 6:当日営業予算 7.累計営業予算 8.当月営業予算 9:当日執行予算 10.累計執行予算 11.当月執行予算
    
    # 删掉第 1 列、求和避免 hrjoin 连接后有重复
    sumup -k2,4 -c5,10                                              |
    # 1.ラインCD 2:店舗CD 3:売上日 4:更新日付 5:当日営業予算 6.累計営業予算 7.当月営業予算 8:当日執行予算 9.累計執行予算 10.当月執行予算
    
    # ----压缩
    gzip -f                                                             >"${lv3d}"/10222148/HIBETU_DIV_URE_YOSAN/"${day}".gz
    # ----抓错
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT

    
:;done
# ----抓错
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} END $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.END.${sday}

# 終了
rm -rf ${tmp}-* 2>/dev/null
exit 0

```

# 三、学习课题 2：DWH_LV4 数据做成

[课题2_(DWH_LV4)数据做成.xlsx](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2FSmart%2Fattachments%2F课题2_(DWH_LV4)数据做成.xlsx)

[课题2_(DWH_LV4%20数据做成).zip](https://tool.yuehai.fun:63/file/downloadPublicFile?basePathType=takeDown&subPath=%2Flinux%2FSmart%2Fattachments%2F课题2_(DWH_LV4%20数据做成).zip)

## 1、日别

### ①、脚本说明

1. 根据拠点CD和部門CD（LINECD、DIVCD）求出每天的営業予算：当日営業予算
2. 分别需要：部門CD、LINECD、DIVCD

### ②、步骤

1. 根据传入的日期求出是哪个月，然后输出这个月的全部天数，以这些天数进行遍历
2. 读取 `"${lv3d}"/URE/10222148/HIBETU_BUMON_CHOKUEI/` 目录下以本次遍历的天数为名的文件，获取：1.部门CD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
3. 排序
4. `ojoin_default` 连接 `"${lv3d}"/YOSAN/10222148/HIBETU_BUMON_URE_YOSAN` 目录下以本次遍历的天数为名的文件，得到：1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
5. 使用 `sumup` 去重、求和，防止`ojoin_default` 连接后有重复的主键
6. 插入本次遍历的天数
7. 调整列顺序
8. --------------------------------
9. 同样方法得到 LINECD 和 DIVCD

### ③、脚本
`POMPAMAKE_HIBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN`
```shell
#!/bin/bash -xv
#
# POMPAMAKE_HIBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN >>> 日別拠点別階層別
#
# Usage : POMPAMAKE_HIBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN <YYYYMMDD>
#
# Written by cuichangjian
# Date : 2022/09/06

# 引き数の確認
if [ $# -eq 0 ] ; then
    # 更新日付
    sday=$(date +%Y%m%d)
else
    # 復旧日付
    sday=$1
fi

HOME=/home/trial
# 走行ログの記録
echo   "${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}" &> /dev/null
exec 2> ${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}

#/////////////////////////////////////////////////////////////////////////
# 初期設定
#/////////////////////////////////////////////////////////////////////////
# パスの定義
export PATH=/home/SMART:/home/SMART_TRIAL:/usr/local/bin:${PATH}
export LANG=ja_JP.UTF-8

# 変数の定義
# 一時ファイルパス
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d%H%M%S)
# ログパス
logd=${HOME}/LOG
# セマフォパス
semd=${HOME}/SEMAPHORE
# 共通テーブルディレクトリ
tbld=/DWH/TBL
# Level3ディレクトリ
lv3d=/DWH/LV3
# Level4ディレクトリ
lv4d=/home/trial/APDATA/URE_YOSAN

# 簡易YYYYMMDD日付チェック
date +%Y%m%d -d "${sday}" >/dev/null
[ $? -ne 0 ] && { echo "Parameter DATE error:[${sday}]" ; exit 1 ; }

# エラー時の終了処理定義
ERROR_EXIT(){
    touch ${semd}/$(basename $0).${HOSTNAME}.ERROR.${sday}
    rm -rf ${tmp}-* 2>/dev/null
    exit 1
}

# 開始時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} START $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.START.${sday}

#/////////////////////////////////////////////////////////////////////////
# 処理部
#/////////////////////////////////////////////////////////////////////////

mkdir -p "${lv4d}"/10222148/HIBETU_BUMON_CHOKUEI
mkdir -p "${lv4d}"/10222148/HIBETU_LINE_CHOKUEI
mkdir -p "${lv4d}"/10222148/HIBETU_DIV_CHOKUEI

# 当月
smonth=$(sdate -m "${sday}")

sdate -d "${smonth}"m                                               |
tov                                                                 |
# 1.日付
while read day ; do

    [ -e "${lv3d}"/URE/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz ]  || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_BUMON_URE_YOSAN/"${day}".gz ]|| continue
    # 日別拠点別部門別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz    |
    # 1.部门CD  2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き) 
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.部门CD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_BUMON_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               |
    insstr -i"${day}" -c5                                           |
    # 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算 6.日付
    selcol -c6 -c2 -c1 -c3,5                                        |
    # 1.日付 2.拠点CD 3.部門CD 4.売上数量 5.売上金額（税抜き） 6.当日営業予算
    gzip -f                                                         >"${lv4d}"/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    [ -e "${lv3d}"/URE/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz ]   || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_LINE_URE_YOSAN/"${day}".gz ]|| continue
    # 日別拠点別LINECD別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz     |
    # 1.ラインCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き)
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.ラインCD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_LINE_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.ラインCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               |
    insstr -i"${day}" -c5                                           |
    # 1.ラインCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算 6.日付
    selcol -c6 -c2 -c1 -c3,5                                        |
    # 1.日付 2.拠点CD 3.LINECD 4.売上数量 5.売上金額（税抜き） 6.当日営業予算
    gzip -f                                                         >"${lv4d}"/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    [ -e "${lv3d}"/URE/10222148/HIBETU_DIV_CHOKUEI/"${day}".gz ]    || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_DIV_URE_YOSAN/"${day}".gz ]|| continue
    # 日別拠点別DIVCD別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_DIV_CHOKUEI/"${day}".gz      |
    # 1.ラインCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き)
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.ラインCD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_DIV_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.ラインCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               |
    insstr -i"${day}" -c5                                           |
    # 1.ラインCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算 6.日付
    selcol -c6 -c2 -c1 -c3,5                                        |
    # 1.日付 2.拠点CD 3.LINECD 4.売上数量 5.売上金額（税抜き） 6.当日営業予算
    gzip -f                                                         >"${lv4d}"/10222148/HIBETU_DIV_CHOKUEI/"${day}".gz
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT

:;done
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} END $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.END.${sday}

# 終了
rm -rf ${tmp}-* 2>/dev/null

exit 0

```
## 2、月别
### ①、脚本说明

1. 根据拠点CD和部門CD（LINECD、DIVCD）求出每月的営業予算：当月営業予算
2. 分别需要：部門CD、LINECD、DIVCD
### ②、步骤

1. 根据传入的日期求出是哪个月，然后输出这个月的全部天数，以这些天数进行遍历
2. 读取 `"${lv3d}"/URE/10222148/HIBETU_BUMON_CHOKUEI/` 目录下以本次遍历的天数为名的文件，获取：1.部门CD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
3. 排序
4. `ojoin_default` 连接 `"${lv3d}"/YOSAN/10222148/HIBETU_BUMON_URE_YOSAN` 目录下以本次遍历的天数为名的文件，得到：1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
5. 使用 `sumup` 去重、求和，防止`ojoin_default` 连接后有重复的主键
6. 将本次循环的数据追加入一个临时表：`"${tmp}"-tukibetu_bumon_data`
7. --------------------------------
8. 同样方法得到 LINECD 和 DIVCD 的临时表 `"${tmp}"-tukibetu_line_data`、`"${tmp}"-tukibetu_div_data`
9. ----在循环后----------------------------
10. 读取临时表：`"${tmp}"-tukibetu_bumon_data`
11. 排序
12. 使用 `sumup` 去重、求和，防被追加后有重复的主键
13. 插入月份
14. 调整列顺序
15. --------------------------------
16. 同样方法得到 LINECD 和 DIVCD
### ③、脚本
`POMPAMAKE_TUKIBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN`
```shell
#!/bin/bash -xv
#
# POMPAMAKE_TUKIBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN >>> 月別拠点別階層別
#
# Usage : POMPAMAKE_TUKIBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN <YYYYMMDD>
#
# Written by cuichangjian
# Date : 2022/09/06

# 引き数の確認
if [ $# -eq 0 ] ; then
    # 更新日付
    sday=$(date +%Y%m%d)
else
    # 復旧日付
    sday=$1
fi

HOME=/home/trial
# 走行ログの記録
echo   "${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}" &> /dev/null
exec 2> ${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}

#/////////////////////////////////////////////////////////////////////////
# 初期設定
#/////////////////////////////////////////////////////////////////////////
# パスの定義
export PATH=/home/SMART:/home/SMART_TRIAL:/usr/local/bin:${PATH}
export LANG=ja_JP.UTF-8

# 変数の定義
# 一時ファイルパス
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d%H%M%S)
# ログパス
logd=${HOME}/LOG
# セマフォパス
semd=${HOME}/SEMAPHORE
# 共通テーブルディレクトリ
tbld=/DWH/TBL
# Level3ディレクトリ
lv3d=/DWH/LV3
# Level4ディレクトリ
lv4d=/home/trial/APDATA/URE_YOSAN

# 簡易YYYYMMDD日付チェック
date +%Y%m%d -d "${sday}" >/dev/null
[ $? -ne 0 ] && { echo "Parameter DATE error:[${sday}]" ; exit 1 ; }

# エラー時の終了処理定義
ERROR_EXIT(){
    touch ${semd}/$(basename $0).${HOSTNAME}.ERROR.${sday}
    rm -rf ${tmp}-* 2>/dev/null
    exit 1
}

# 開始時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} START $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.START.${sday}

#/////////////////////////////////////////////////////////////////////////
# 処理部
#/////////////////////////////////////////////////////////////////////////

mkdir -p "${lv4d}"/10222148/TUKIBETU_BUMON_CHOKUEI
mkdir -p "${lv4d}"/10222148/TUKIBETU_LINE_CHOKUEI
mkdir -p "${lv4d}"/10222148/TUKIBETU_DIV_CHOKUEI

:>"${tmp}"-tukibetu_bumon_data
:>"${tmp}"-tukibetu_line_data
:>"${tmp}"-tukibetu_div_data

# 当月
smonth=$(sdate -m "${sday}")

sdate -d "${smonth}"m                                               |
tov                                                                 |
# 1.日付
while read day ; do

    [ -e "${lv3d}"/URE/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz ]  || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_BUMON_URE_YOSAN/"${day}".gz ]|| continue
    # 月別拠点別部門別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz    |
    # 1.部门CD  2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き) 
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.部门CD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_BUMON_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               >>"${tmp}"-tukibetu_bumon_data
    # 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    [ -e "${lv3d}"/URE/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz ]   || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_LINE_URE_YOSAN/"${day}".gz ]|| continue
    # 月別拠点別LINECD別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz     |
    # 1.ラインCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き)
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.ラインCD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_LINE_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.LINECD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               >>"${tmp}"-tukibetu_line_data
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    [ -e "${lv3d}"/URE/10222148/HIBETU_DIV_CHOKUEI/"${day}".gz ]    || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_DIV_URE_YOSAN/"${day}".gz ]|| continue
    # 月別拠点別DIVCD別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_DIV_CHOKUEI/"${day}".gz      |
    # 1.ディビジョンCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き)
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.ディビジョンCD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_DIV_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.DIVCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               >>"${tmp}"-tukibetu_div_data
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT

:;done
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


cat "${tmp}"-tukibetu_bumon_data|
# 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
ssort -k1,2                     |
sumup -k1,2 -c3,5               |
# 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.月别営業予算合计
insstr -i"${smonth}" -c5        |
# 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.月别営業予算合计 6.年月
selcol -c6 -c2 -c1 -c3,5        |
# 1.年月 2.拠点CD 3.部門CD 4.売上数量 5.売上金額（税抜き） 6.月别営業予算合计
gzip -f                         >"${lv4d}"/10222148/TUKIBETU_BUMON_CHOKUEI/"${smonth}".gz
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


cat "${tmp}"-tukibetu_line_data |
# 1.LINECD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
ssort -k1,2                     |
sumup -k1,2 -c3,5               |
# 1.LINECD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.月别営業予算合计
insstr -i"${smonth}" -c5        |
# 1.LINECD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.月别営業予算合计 6.年月
selcol -c6 -c2 -c1 -c3,5        |
# 1.年月 2.拠点CD 3.LINECD 4.売上数量 5.売上金額（税抜き） 6.月别営業予算合计
gzip -f                         >"${lv4d}"/10222148/TUKIBETU_LINE_CHOKUEI/"${smonth}".gz
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


cat "${tmp}"-tukibetu_div_data  |
# 1.DIVCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
ssort -k1,2                     |
sumup -k1,2 -c3,5               |
# 1.DIVCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.月别営業予算合计
insstr -i"${smonth}" -c5        |
# 1.DIVCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.月别営業予算合计 6.年月
selcol -c6 -c2 -c1 -c3,5        |
# 1.年月 2.拠点CD 3.DIVCD 4.売上数量 5.売上金額（税抜き） 6.月别営業予算合计
gzip -f                         >"${lv4d}"/10222148/TUKIBETU_DIV_CHOKUEI/"${smonth}".gz
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} END $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.END.${sday}

# 終了
rm -rf ${tmp}-* 2>/dev/null

exit 0

```
## 3、周别
### ①、脚本说明

1. 根据拠点CD和部門CD（LINECD、DIVCD）求出每周的営業予算：当週営業予算
2. 分别需要：部門CD、LINECD、DIVCD
### ②、步骤

1. 根据传入的日期求出是哪个周，然后输出这个周的全部天数，以这些天数进行遍历
2. 下面的步骤和月别相同
### ③、脚本
`POMPAMAKE_SYUBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN`
```shell
#!/bin/bash -xv
#
# POMPAMAKE_SYUBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN >>> 週別拠点別階層別
#
# Usage : POMPAMAKE_SYUBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN <YYYYMMDD>
#
# Written by cuichangjian
# Date : 2022/09/06

# 引き数の確認
if [ $# -eq 0 ] ; then
    # 更新日付
    sday=$(date +%Y%m%d)
else
    # 復旧日付
    sday=$1
fi

HOME=/home/trial
# 走行ログの記録
echo   "${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}" &> /dev/null
exec 2> ${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}

#/////////////////////////////////////////////////////////////////////////
# 初期設定
#/////////////////////////////////////////////////////////////////////////
# パスの定義
export PATH=/home/SMART:/home/SMART_TRIAL:/usr/local/bin:${PATH}
export LANG=ja_JP.UTF-8

# 変数の定義
# 一時ファイルパス
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d%H%M%S)
# ログパス
logd=${HOME}/LOG
# セマフォパス
semd=${HOME}/SEMAPHORE
# 共通テーブルディレクトリ
tbld=/DWH/TBL
# Level3ディレクトリ
lv3d=/DWH/LV3
# Level4ディレクトリ
lv4d=/home/trial/APDATA/URE_YOSAN

# 簡易YYYYMMDD日付チェック
date +%Y%m%d -d "${sday}" >/dev/null
[ $? -ne 0 ] && { echo "Parameter DATE error:[${sday}]" ; exit 1 ; }

# エラー時の終了処理定義
ERROR_EXIT(){
    touch ${semd}/$(basename $0).${HOSTNAME}.ERROR.${sday}
    rm -rf ${tmp}-* 2>/dev/null
    exit 1
}

# 開始時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} START $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.START.${sday}

#/////////////////////////////////////////////////////////////////////////
# 処理部
#/////////////////////////////////////////////////////////////////////////

mkdir -p "${lv4d}"/10222148/SYUBETU_BUMON_CHOKUEI
mkdir -p "${lv4d}"/10222148/SYUBETU_LINE_CHOKUEI
mkdir -p "${lv4d}"/10222148/SYUBETU_DIV_CHOKUEI

:>"${tmp}"-syubetu_bumon_data
:>"${tmp}"-syubetu_line_data
:>"${tmp}"-syubetu_div_data

# 当週
sweek=$(sdate -w "${sday}")

sdate -d "${sweek}"w                                               |
tov                                                                |
# 1.日付
while read day ; do

    [ -e "${lv3d}"/URE/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz ]  || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_BUMON_URE_YOSAN/"${day}".gz ]|| continue
    # 週別拠点別部門別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_BUMON_CHOKUEI/"${day}".gz    |
    # 1.部门CD  2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き) 
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.部门CD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_BUMON_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               >>"${tmp}"-syubetu_bumon_data
    # 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    [ -e "${lv3d}"/URE/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz ]   || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_LINE_URE_YOSAN/"${day}".gz ]|| continue
    # 週別拠点別LINECD別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_LINE_CHOKUEI/"${day}".gz     |
    # 1.ラインCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き)
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.ラインCD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_LINE_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.LINECD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               >>"${tmp}"-syubetu_line_data
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


    [ -e "${lv3d}"/URE/10222148/HIBETU_DIV_CHOKUEI/"${day}".gz ]    || continue
    [ -e "${lv3d}"/YOSAN/10222148/HIBETU_DIV_URE_YOSAN/"${day}".gz ]|| continue
    # 週別拠点別DIVCD別売上
    zcat "${lv3d}"/URE/10222148/HIBETU_DIV_CHOKUEI/"${day}".gz      |
    # 1.ディビジョンCD 2.拠点CD 3.売上日 4.更新日付 5.原価額 6.売上数量 7.売上金額
    # 8.売上金額（税抜き）9.値割数量 10.値割金額 11.値割金額(税抜き)
    # 12.システムロス金額  13.システムロス金額(税抜き)
    selcol -c1,2 -c6 -c8                                            |
    # 1.ディビジョンCD 2.拠点CD 3.売上数量 4.売上金額（税抜き）
    ssort -k1,2                                                     |
    ojoin_default -k1,2 -M4 -M3 -i"0" - <(zcat "${lv3d}"/YOSAN/10222148/HIBETU_DIV_URE_YOSAN/"${day}".gz | selcol -c1,2 -c5 | ssort -k1,2) |
    # 1.DIVCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
    sumup -k1,2 -c3,5                                               >>"${tmp}"-syubetu_div_data
    [ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT

:;done
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


cat "${tmp}"-syubetu_bumon_data |
# 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
ssort -k1,2                     |
sumup -k1,2 -c3,5               |
# 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.週别営業予算合计
insstr -i"${sweek}" -c5         |
# 1.部門CD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.週别営業予算合计 6.年週
selcol -c6 -c2 -c1 -c3,5        |
# 1.年月 2.拠点CD 3.部門CD 4.売上数量 5.売上金額（税抜き） 6.週别営業予算合计
gzip -f                         >"${lv4d}"/10222148/SYUBETU_BUMON_CHOKUEI/"${sweek}".gz
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


cat "${tmp}"-syubetu_line_data  |
# 1.LINECD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
ssort -k1,2                     |
sumup -k1,2 -c3,5               |
# 1.LINECD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.週别営業予算合计
insstr -i"${sweek}" -c5         |
# 1.LINECD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.週别営業予算合计 6.年週
selcol -c6 -c2 -c1 -c3,5        |
# 1.年月 2.拠点CD 3.LINECD 4.売上数量 5.売上金額（税抜き） 6.週别営業予算合计
gzip -f                         >"${lv4d}"/10222148/SYUBETU_LINE_CHOKUEI/"${sweek}".gz
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


cat "${tmp}"-syubetu_div_data   |
# 1.DIVCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.当日営業予算
ssort -k1,2                     |
sumup -k1,2 -c3,5               |
# 1.DIVCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.週别営業予算合计
insstr -i"${sweek}" -c5         |
# 1.DIVCD 2.拠点CD 3.売上数量 4.売上金額（税抜き） 5.週别営業予算合计 6.年週
selcol -c6 -c2 -c1 -c3,5        |
# 1.年月 2.拠点CD 3.DIVCD 4.売上数量 5.売上金額（税抜き） 6.週别営業予算合计
gzip -f                         >"${lv4d}"/10222148/SYUBETU_DIV_CHOKUEI/"${sweek}".gz
[ $(errchk  ${PIPESTATUS[@]}) -eq 0 ] || ERROR_EXIT


#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} END $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.END.${sday}

# 終了
rm -rf ${tmp}-* 2>/dev/null

exit 0

```
## 4、job
`APMASTER_URE_YOSAN_CHOKUEI.DAYDWH.URE`
```shell
#!/bin/bash -xv
#
# APMASTER_URE_YOSAN_CHOKUEI.DAYDWH.URE >>> 月別部門、ライン別ディビジョン別売上と予算作成
# Usage : APMASTER_URE_YOSAN_CHOKUEI.DAYDWH.URE <YYYYMMDD>
#
# Written by cuichangjian 
# Date : 2022/09/06

if [ $# -eq 0 ] ; then
    # 更新日付
    sday=$(date +%Y%m%d)
else
    # 復旧日付
    sday=$1
fi

HOME=/home/trial/AP
# 走行ログの記録
echo   "${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}" &> /dev/null
exec 2> ${HOME}/LOG/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$.${sday}

#/////////////////////////////////////////////////////////////////////////
# 初期設定
#/////////////////////////////////////////////////////////////////////////
# パスの定義
export PATH=/home/SMART:/home/SMART_TRIAL:/usr/local/bin:${PATH}
export LANG=ja_JP.UTF-8

# 変数の定義
# 一時ファイルパス
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d%H%M%S)
# ログパス
logd=${HOME}/LOG
# セマフォパス
semd=${HOME}/SEMAPHORE
# シェルパス
shld=${HOME}/SHELL

# 簡易YYYYMMDD日付チェック
date +%Y%m%d -d "${sday}" >/dev/null
[ $? -ne 0 ] && { echo "Parameter DATE error:[${sday}]" ; exit 1 ; }

# エラー時の終了処理定義
ERROR_EXIT(){
    unlock -f /tmp/$(basename $0)_${sday}.${HOSTNAME}.LOCK
    touch ${semd}/$(basename $0).${HOSTNAME}.ERROR.${sday}
    rm -rf ${tmp}-* 2>/dev/null
    exit 1
}

# 起動時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} START $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.START.${sday}

#/////////////////////////////////////////////////////////////////////////
# 処理の起動
#/////////////////////////////////////////////////////////////////////////

#　日別拠点別階層別
${shld}/10222148/POMPAMAKE_HIBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN "${sday}"
[ $? -eq 0 ] || ERROR_EXIT

#　月別拠点別階層別
${shld}/10222148/POMPAMAKE_TUKIBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN "${sday}"
[ $? -eq 0 ] || ERROR_EXIT

#　週別拠点別階層別
${shld}/10222148/POMPAMAKE_SYUBETU_DIV_LINE_BUMON_CHOKUEI.DAYDWH.UREYOSAN "${sday}"
[ $? -eq 0 ] || ERROR_EXIT


#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了時刻の記録
echo "${HOSTNAME} $(basename $0) ${sday} END $(date +%Y%m%d%H%M%S)" >> ${logd}/UPCNT.${sday}
touch ${semd}/$(basename $0).${HOSTNAME}.END.${sday}

# 終了
rm -rf ${tmp}-* 2>/dev/null
exit 0

```

# 四、

# 五、
---

## 1、
## 2、
## 3、
## 4、
## 5、
## 6、
## 7、
## 8、
## 9、
### ①、
### ②、
### ③、
### ④、
### ⑤、
### ⑥、
### ⑦、
### ⑧、
### ⑨、
### ⑩、
#### Ⅰ、
#### Ⅱ、
#### Ⅲ、
#### Ⅳ、
#### Ⅴ、
#### Ⅵ、
#### Ⅶ、
#### Ⅷ、
#### Ⅸ、
#### Ⅹ、
