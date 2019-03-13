# Quick Start

## 环境安装说明

凡是安装开发环境，都需要注意以下几点，防止意外错误的发生：

- 安装的软件目录中不要出现**中文**与**特殊字符**，尤其是**空格**
- 计算机名称`(控制面板\所有控制面板项\系统中设置)`不要**中文**，改成**英文**，也不要**特殊字符**

- - - - - - - - - - - - - - - - - - - - - - - -

## Node环境

如果已经安装过Node并且是使用安装包单独安装，那么先卸载掉，然后使用nvm进行安装，好处是可以动态切换Node版本以适应不同环境的需求，目前ReactNative需要至少8.0以上的Node版本。<br />

卸载Node的时候最好把npm缓存也一起清掉，清除缓存运行`npm cache clean --force`命令就可以，Windows用户也可以在用户目录下手动删除缓存文件夹`C:\Users\UserName\AppData\Roaming\npm-cache`。<br />

大多数情况下，如果遇到`Unexpected end of JSON input while parsing near`错误，都是因为安装的包与本地Node版本不符导致的，这时候清除缓存就可解决。<br />

### **nvm**

nvm是NodeJS的版本管理工具，使用它可以在本地安装多个不同版本的NodeJS，并根据需要动态切换。安装nvm之前，需要先卸载之前单独安装过的NodeJS，在控制面板中进行卸载即可。

下载

- [mac下载]<https://github.com/creationix/nvm/releases>
- [windows下载]<https://github.com/coreybutler/nvm-windows/releases>

安装说明

windows用户下载一键安装版本`nvm-setup.zip`, 解压后傻瓜式安装即可。<br />
安装过后，在命令行窗口运行`nvm version`命令进行检测，如果显示安装的版本号，即成功。<br />

- [参考文档]<https://www.jianshu.com/p/1d80cf35abd2>

配置淘宝镜像

为了提高nvm在国内的下载速度，最好修改源镜像下载地址。首先找到nvm的安装目录，编辑settings.txt文件，添加如下配置，含义是使用淘宝镜像下载64位的node或npm，如果是32位操作系统，那么arch设为32。<br />

- [参考文档]<https://www.jianshu.com/p/253cb9003411>

```txt
arch: 64
node_mirror: http://npm.taobao.org/mirrors/node/
npm_mirror: https://npm.taobao.org/mirrors/npm/
```

nvm常用命令

- nvm install      # 安装指定版本
- nvm uninstall    # 卸载指定版本
- nvm list         # 列出已安装的版本
- nvm use          # 版本切换
- nvm on           # 启用nvm
- nvm off          # 关闭nvm
- nvm root         # nvm安装路径

### **node**

nvm安装配置成功后，接下来安装node只需一条命令即可。安装完毕后，通过use命令切换到指定版本的node，最好是官方推荐的稳定版本。然后运行`node -v`命令进行检测，只要显示出你刚刚切换的node版本，就大功告成了。<br />

安装Node的时候，如果是开发使用，建议安装稳定版本，如果是为了尝试新特性无所谓，目前Node有个规范，奇数版本为实验版本，偶数版本为稳定版本，很多开源项目在版本号制定时都会参照这种方式，需要留意一下。<br />

- [nvm安装参考文档]<https://www.jianshu.com/p/28bca6529150>
- [node官方版本查阅]<https://nodejs.org/zh-cn/>

安装

```shell
# 安装官方推荐的稳定版本
nvm install 8.11.3
nvm use 8.11.3

# 安装最新的稳定版本，体验新特性
nvm install stable
nvm list
nvm use xxx
```

npm淘宝镜像配置

node安装后，npm就跟着一起被安装了，为了提供国内的下载速度，同样把npm的源镜像地址改为淘宝的，在命令行窗口中运行如下命令进行配置。<br />

- [参考文档]<https://www.jianshu.com/p/253cb9003411>

```shell
# 配置
npm config set registry https://registry.npm.taobao.org
npm config set disturl https://npm.taobao.org/dist

# 检测
npm config get registry
npm config get disturl
```

- - - - - - - - - - - - - - - - - - - - - - - -

## React-Native快速开发环境

学习使用React-Native最令人头疼的就是环境问题，因为大多数web开发者，并不熟悉Android与IOS的开发环境，配置起来也比较繁琐，同时Android程序员也不熟悉IOS环境，IOS程序员也不熟悉Android环境，导致了很多人因为环境而放弃学习，为了解决这个问题，所以产生了所谓的快速开发环境。

### **create-react-native-app**

这是目前官网推荐的React-Native开发工具，特点是无需配置繁杂的Android或IOS开发环境便可进行RN原生应用的开发，简化了环境搭建与配置，非常方便，很适合新人和拥有多台办公设备的程序员使用。

- [参考文档]<https://facebook.github.io/react-native/docs/getting-started.html>

安装

```shell
# 安装
npm install -g create-react-native-app

# 检测
create-react-native-app --version
```

### **模拟器**

有了开发环还需要一款手机作为运行环境，除了使用真机外，还可以使用模拟器软件进行替代。Window平台下官方推荐使用一款叫Genymotion的Android模拟器，该模拟器依赖VirtualBox虚拟机，需要创建账号登陆后才能使用，除此以外也可以使用国内模拟器，国内模拟器比较多，有夜神、雷电、MuMu等。<br />

- [Genymotion]<https://www.genymotion.com/>
- [夜神]<https://www.yeshen.com/>
- [雷电]<https://www.yeshen.com/>
- [MuMu]<http://mumu.163.com/baidu/>

### adb工具

adb安装在Android-sdk路径下的platform-tools目录，这个工具是电脑与Android设备进行通信的通用命令行工具，同时可以检测或连接Android设备，所有有几个常用命令需要了解。<br />
将来使用的时候需要保证本机的adb版本需要与Android设备内的adb版本一致，否则可能无法正常通信，解决办法是我们可以复制本机的adb.exe程序，然后覆盖掉模拟器中的版本。<br />

- adb version        # 版本
- adb devices        # 列出连接到本机的Android设备与状态
- adb connect        # 手动连接Android设备
- adb start-server   # 启动adb服务
- adb kill-server    # 关闭adb服务

```shell
adb version
// 第一行显示的信息：Android Debug Bridge version 1.0.40
// 其中40就代表adb的版本，将来可能把copy这个版本的adb工具覆盖掉模拟器版本
```

- - - - - - - - - - - - - - - - - - - - - - - -

## 开发方式

### **模拟器开发调试**

开发环境`create-react-native-app`与运行环境`模拟器`准备好之后，就可以开始RN开发了。<br />

**启动模拟器**

- 首先启动模拟器，运行adb devices命令，查看设备是否正常连接，
- 如果提示adb版本不符合，那么就需要把本地Android-sdk目录下的adb.ext复制到模拟器目录下的bin中，进行覆盖。然后重启模拟器进行尝试。

```shell
// 连接正常的话会显示设备信息或地址信息，如：127.0.0.1:62001 device
adb devices

// 如果没有发现设备，那么需要手动进行连接，夜神模拟器端口62001，MUMU模拟器端口7555
adb connect 127.0.0.1:7555
```

**项目创建与运行**

然后通过下面的命令创建并运行项目，CRNA会自动在模拟器中安装Expo软件，并在此APP中运行我们的项目，这种方式有点类似与微信小程序，即我们的项目最终是运行在一个叫Expo的App当中。<br />

```shell
# 项目创建
create-react-native-app projectName

# 运行
cd projectName
yarn start
```
