# 一、nodejs

# 二、nvm

## 1、介绍

## 2、目录规划

1. 没有的目录提前创建

```shell
D:\IDE\Web\
├── nodejs\              ← 全局 Node 22（永久使用，PATH 指向这里）
├── nvm-noinstall\       ← nvm 本体 + 各版本 Node 存放处
│   ├── nvm.exe
│   ├── settings.txt
│   └── v14.17.0\        ← nvm install 后生成
└── nvm-nodejs\          ← nvm 软链接目录（执行 nvm use 才用到，平时可为空）
```

## 3、nvm 安装与配置

### ①、下载解压 nvm

1. nvm 下载：https://github.com/coreybutler/nvm-windows/releases/tag/1.1.12
	1. 1.1.12 本地下载：[nvm-noinstall-1.1.12.zip](attachments/nvm-noinstall-1.1.12.zip)
2. 解压到 `D:\IDE\Web\nvm-noinstall` 目录

### ②、创建 settings.txt

> 需要使用 VS Code 保存为 UTF-8；记事本默认 Unicode(UTF-16) 会导致 nvm 读不到配置，导致 nvm root 为空

1. 在 `D:\IDE\Web\nvm-noinstall` 目录下创建 `settings.txt`，必须是 UTF-8，输入以下内容：

```shell
root: D:\IDE\Web\nvm-noinstall
path: D:\IDE\Web\nvm-nodejs
arch: 64
proxy: none
```

### ③、配置系统环境变量

1. 添加系统变量：

| 变量名         | 值                        |
| ----------- | ------------------------ |
| NVM_HOME    | D:\IDE\Web\nvm-noinstall |
| NVM_SYMLINK | D:\IDE\Web\nvm-nodejs    |

2. 添加PATH 配置：
	1. `%NVM_HOME%`，用于 nvm 命令
3. 不要把 `%NVM_SYMLINK%` 或 `D:\IDE\Web\nvm-nodejs` 目录加入 PATH

### ④、验证配置

1. 打开 CMD：

```shell
nvm version    # 期望输出：1.1.12
nvm root       # 期望输出：D:\IDE\Web\nvm-noinstall
node -v        # 期望输出：v22.7.0（全局不变）
```

## 4、安装 Node 14.17.0

1. 安装 Node 14.17.0：

```shell
# 安装 Node 14.17.0
nvm install 14.17.0

# 查看 Node 列表
nvm list
```

1. 安装位置：`D:\IDE\Web\nvm-noinstall\v14.17.0\`
2. 不要执行 `nvm use 14.17.0`，会改 nvm 软链接，不符合全局不变方案
3. `D:\IDE\Web\nvm-nodejs` 目录为空是正常的
4. nvm 安装的是 `node64.exe`，没有 node.exe，需手动复制一次：

```shell
copy D:\IDE\Web\nvm-noinstall\v14.17.0\node64.exe D:\IDE\Web\nvm-noinstall\v14.17.0\node.exe
```

## 5、项目开发打包流程

1. 进入项目目录，如：

```shell
cd D:\Idea\save\Company\09_support_YuanXIangCong_10218858\06_hbs-newkintai-kintai\hbs-newkintai-kintai-web
```

2. 将当前终端临时切换到 Node 14

```shell
$env:PATH = "D:\IDE\Web\nvm-noinstall\v14.17.0;$env:PATH"
```

3. 查看是否切换成功

```shell
node -v
```

4. 清掉旧依赖

```shell
Remove-Item -Recurse -Force node_modules -ErrorAction SilentlyContinue
```

5. 安装依赖

```shell
npm install
```

6. 安装依赖（可选）：临时指定镜像地址

```shell
npm install --sass_binary_site=https://npmmirror.com/mirrors/node-sass/
```

7. 启动项目

```shell
npm run dev
```

8. 打包

```shell
# 测试
npm run build:test

# 生产
npm run build
```

## 6、可复用脚本

1. 在项目根目录保存 `use-node14.ps1`：

```shell
# 将当前终端临时切换到 Node 14
$env:PATH = "D:\IDE\Web\nvm-noinstall\v14.17.0;$env:PATH"
Write-Host "当前 Node: $(node -v)"
Write-Host "当前 npm:  $(npm -v)"
```

2. 使用：

```shell
.\use-node14.ps1
npm install
npm run build
```

## 7、

## 8、

## 9、


# 三、

# 四、

# 五、

# 六、

# 七、

# 八、

# 九、

# 十、
