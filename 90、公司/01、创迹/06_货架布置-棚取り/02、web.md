# 一、项目整理

## 1、首页
## 2、定番

### ①、定番列表

### ②、定番详情

#### Ⅰ、サマリー（概览）

#### Ⅱ、パターン（布局种类）

#### Ⅲ、売場変更

##### （1）、mode 1（改废）

1. 说明：旧商品替换为新商品，商品改变或者废除
2. 创建：定番详情 -> 売場変更 ->  点击 売場変更を作成，选择 商品の改廃を設定する 即可
3. 代码：

| 步骤    | 说明       | 通用性             | 路径                                                                             |
| ----- | -------- | --------------- | ------------------------------------------------------------------------------ |
| 主入口文件 |          | mode 1、2、3、4 通用 | src/views/Standard/StandardChangeDetail/index.vue                              |
| 第 0 步 | 创建时类型选择  | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/Entry.vue                              |
| 第 1 步 | 入口文件     | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/MakeLayout/index.vue                   |
|       | 商品改廃设置   | 仅 mode 1 使用     | src/views/Standard/StandardChangeDetail/MakeLayout/MakeLayoutProductChange.vue |
|       | 商品改廃确认   | 仅 mode 1 使用     | src/views/Standard/StandardChangeDetail/MakeLayout/ProductChangeConfirm.vue    |
| 第 2 步 | 作業日の設定   | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/SendWorkMail.vue                       |
| 第 3 步 | 新规 list  | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/ConfirmNewList.vue                     |
| 第 4 步 | cut list | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/ConfirmCutList.vue                     |
| 第 5 步 | 送信       | mode 1、2、3、4 通用 | src/views/Standard/StandardChangeDetail/SendMail.vue                           |

![|700](attachments/Pasted%20image%2020260212135906.png)

##### （2）、mode 2（直接编辑）

1. 说明：随意替换商品
2. 创建：定番详情 -> 売場変更 ->  点击 売場変更を作成，选择 パターンを直接編集する 即可
3. 代码：

| 步骤    | 说明       | 通用性             | 路径                                                                 |
| ----- | -------- | --------------- | ------------------------------------------------------------------ |
| 主入口文件 |          | mode 1、2、3、4 通用 | src/views/Standard/StandardChangeDetail/index.vue                  |
| 第 0 步 | 创建时类型选择  | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/Entry.vue                  |
| 第 1 步 | 入口文件     | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/MakeLayout/index.vue       |
|       | 直接編集     | mode 2、3 通用     | src/views/Standard/StandardChangeDetail/MakeLayout/PatternEdit.vue |
| 第 2 步 | 作業日の設定   | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/SendWorkMail.vue           |
| 第 3 步 | 新规 list  | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/ConfirmNewList.vue         |
| 第 4 步 | cut list | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/ConfirmCutList.vue         |
| 第 5 步 | 送信       | mode 1、2、3、4 通用 | src/views/Standard/StandardChangeDetail/SendMail.vue               |

![|700](attachments/Pasted%20image%2020260212135939.png)

##### （3）、mode 3（pts 投入）

1. 说明：通过上传 pts 文件进行创建
2. 创建：定番详情 -> 売場変更 ->  点击 売場変更を作成，选择 PTSファイルをインポートする 即可
3. 代码：

| 步骤    | 说明       | 通用性             | 路径                                                                   |
| ----- | -------- | --------------- | -------------------------------------------------------------------- |
| 主入口文件 |          | mode 1、2、3、4 通用 | src/views/Standard/StandardChangeDetail/index.vue                    |
| 第 0 步 | 创建时类型选择  | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/Entry.vue                    |
| 第 1 步 | 入口文件     | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/MakeLayout/index.vue         |
|       | PTS文件上传  | 仅 mode 3 使用     | src/views/Standard/StandardChangeDetail/MakeLayout/ImportPtsFile.vue |
|       | 直接編集     | mode 2、3 通用     | src/views/Standard/StandardChangeDetail/MakeLayout/PatternEdit.vue   |
| 第 2 步 | 作業日の設定   | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/SendWorkMail.vue             |
| 第 3 步 | 新规 list  | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/ConfirmNewList.vue           |
| 第 4 步 | cut list | mode 1、2、3 通用   | src/views/Standard/StandardChangeDetail/ConfirmCutList.vue           |
| 第 5 步 | 送信       | mode 1、2、3、4 通用 | src/views/Standard/StandardChangeDetail/SendMail.vue                 |

![|700](attachments/Pasted%20image%2020260212140133.png)

##### （4）、mode 4（采用パターン变更）

1. 说明，修改パターン，只有 4 步
2. 创建：定番详情 -> パターン -> 点击列表项的採用店舗数 -> 点击抽屉的追加 进行创建
3. 代码：

| 步骤           | 说明       | 通用性             | 路径                                                              |
| ------------ | -------- | --------------- | --------------------------------------------------------------- |
| 主入口文件        |          | mode 1、2、3、4 通用 | src/views/Standard/StandardChangeDetail/index.vue               |
| mode 4 主入口文件 |          | 仅 mode 4 使用     | src/views/Standard/StandardChangeDetail/NewTypeChangeDetail.vue |
| 第 1 步        | 新规 list  | 仅 mode 4 使用     | src/views/Store/StoreSendMail/ConfirmNewLists.vue               |
| 第 2 步        | cut list | 仅 mode 4 使用     | src/views/Standard/StandardChangeDetail/ConfirmCutNewList.vue   |
| 第 3 步        | 採用店舗     | 仅 mode 4 使用     | src/views/Standard/StandardChangeDetail/ShowPatternList.vue     |
| 第 4 步        | 送信       | mode 1、2、3、4 通用 | src/views/Standard/StandardChangeDetail/SendMail.vue            |

![|700](attachments/Pasted%20image%2020260212140421.png)

##### （5）、


#### Ⅳ、

#### Ⅴ、

### ③、

### ④、

## 3、商品改废

## 4、プロモーション

## 5、商品リスト

## 6、店铺

## 7、作業依頼

## 8、


# 二、项目代码


## 1、弹窗

### ①、二次确认弹窗


```js
const changeFlag = await useSecondConfirmation({
	type: 'delete',
	icon: ExclamationIcon,
	width: 490,
	message: [
	'棚の本数やパレットの枚数を減らすなど、什器の数を変える場合、',
	'減らされた場所にあった商品は削除されます。',
	'<div style="padding: 1em;"> (サイズ変更だけの場合は、削除されず保持されます!) </div>',
	'このまま什器を変更してよろしいですか？'
	],
	confirmation: [{ value: 0 }, { value: 1, text: `変更する` }]
});
if (!changeFlag) return;
```


### ②、

### ③、

### ④、
## 2、

## 3、

## 4、


# 三、一些问题

# 四、poc 笔记