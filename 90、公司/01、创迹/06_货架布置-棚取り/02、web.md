# 一、项目整理

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