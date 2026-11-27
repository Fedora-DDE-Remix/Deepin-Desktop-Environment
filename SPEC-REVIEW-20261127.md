# DDE 桌面 SPEC 审查与修复记录

本轮以维护提交 `adcd681b0b9e68cacbf9daa33bede62a253a3315` 为基线，对仓库现有
80 份 SPEC 做静态清点，重点核对桌面、登录、会话、schemas、默认资源及明确覆盖
Fedora 编译参数的包。修复仅进入独立分支供审阅与自测，没有调用 COPR 构建。
这不是所有包均完成重新编译、所有桌面功能均通过测试的声明。

## 已确认并提交的修复

| 包 | 问题 | 修复 |
| --- | --- | --- |
| dde-file-manager | 嵌套 Qt 插件加载时 DPF 事件转换回调在不同共享库中形成不同实例，内层回调为空，与桌面 WindowFrame 空屏幕对象崩溃链吻合 | Release 10，新增 Patch2，将可变回调定义集中到 framework；完整重建同一 SRPM 的运行包，保留原编译参数 |
| deepin-desktop-schemas | mediakey 的 away 键有重复 summary/description，真实严格编译失败；默认背景指向缺失文件，安装脚本静默忽略错误 | Release 2，最小两行删除补丁、真实 buildroot 的严格 %check、Fedora glib2 文件触发器、现存 JPEG 路径及其资源依赖 |
| deepin-default-settings | 普通桌面安装没有提供 Treeland/appearance 默认路径对应的背景资源 | Release 3，声明 desktop-backgrounds-basic，安装两份桌面 DConfig 默认值；不重置已有用户选择 |
| deepin-desktop-base | 硬性依赖主 Fedora 标识包，阻止 Remix 选择通用系统图形资源 | Release 2，改为虚拟依赖 system-logos，保留源码及安装文件不变 |
| ddm | 服务需要 dde-seatd，但 RPM 未声明；仅处理传统 getty 与初始 VT 的竞争 | Release 9，增加运行依赖，按 DDM_INITIAL_VT 对应的 kmscon 单元增加 After/Conflicts；PAM 和 SELinux 配置保持原样 |
| treeland | 缺少服务所需 dde-seatd 及外部执行 Xwayland 的运行依赖；默认 Logo URL scheme 和 qrc 资源路径错误 | Release 11，增加实际运行依赖，保留原 Patch0/1 并增加 Patch2，将回退值改为 qrc:/dsg/icons/logo.svg |
| dde-api | 将 Debian sudo 组的附加授权规则打包到 Fedora Polkit 默认不读取的 /var/lib 目录 | Release 9，剔除这一无效规则及其空目录，保留现有管理员认证策略与调用流程 |
| dde-shell | 手写 CMAKE_CXX_FLAGS 覆盖 Fedora 参数并对全部 C++ 目标强制 -fPIE | Release 5，保留 build_cxxflags 与原 deprecation suppression，由 CMake/Fedora 处理 PIC/PIE |
| 10 个 SeetaFace 源码包 | 强制包含标准库头文件时覆盖了 Fedora C++ 参数 | 保留所有原 include/选项，追加到 build_cxxflags；各包递增既有 Release 序号 |

10 个 SeetaFace 包为：anti-spoofing-x、authorize、boxes、landmarker、open-role-zoo、
pose-estimation、quality-assessor、recognizer、tennis、tracker。模型数据包没有改动。
各自原日期、Git 源码版本和架构/授权/加密选项均保留。

## 验证证据与边界

### DPF 崩溃

固定上游 DFM 提交为 `bdd0f409316054d136eeb8eb7a132a977e4915f7`。
原 Fedora 包的真实嵌套 Qt 探针可复现内层事件名转换为 -1、回调无效；集中定义后
事件编号、同址回调、整数与列表通道返回值均正确。完整临时 RPM 已在独立 Fedora
容器通过安装、ELF、重定位及实际嵌套 Qt 探针：

- [原包/候选 A/B](https://github.com/Fedora-DDE-Remix/ISO-Build/actions/runs/45948782959)
- [完整 RPM 独立复验](https://github.com/Fedora-DDE-Remix/ISO-Build/actions/runs/45956698212)
- [详细分析与原始失败记录](https://github.com/Fedora-DDE-Remix/ISO-Build/blob/2d1ed2ce6dcb34bb2d3df56903b5de077cd83357/DDE-HOTFIX-20261127.md)

补丁 SHA-256 为 `40b726528a34f41cdcbba4a538e5fc9b08fb3b354f8c340f905ead2c0d3d0381`。
这些构建验证的是同一补丁的临时 `9.1.remix1` 包，不是声称此分支的 `10` 已在
COPR 构建。当前子包已有 exact EVR 约束；不因本次修复修改 SONAME、关闭 LTO，
也不把 dde-shell 的独立 flags 错误当作 DPF 根因。

### schemas 与背景默认值

固定上游 schemas 提交为 `00a92111f8f0cc7bcba8af9ae2a9950c7f02ae4e`。
[ISO compose 45974028174](https://github.com/Fedora-DDE-Remix/ISO-Build/actions/runs/45974028174)
在安装完全部 69 个 mandatory 包后，实际报 `Only one <summary> element allowed inside <key>`。
本机 GLib 2.84.4 对原文件复现相同 319:23 错误；只删除重复的空元素后，全部
79 个 XML 通过严格编译。x86 base、四种 edition 与 Remix override 的检查也通过。

没有加入 ISO override 时，按新 SPEC 的路径映射读取真实编译缓存，两项背景默认值
均为 `file:///usr/share/backgrounds/images/earth_from_space.jpg`。
本机没有 Go 编译器；上述 override 合并由独立脚本按固定上游生成器语义重现。
新增 RPM `%check` 会验证 Fedora 构建中真正由 Go 生成并安装到 buildroot 的内容。

后续 [ISO compose 45981240945](https://github.com/Fedora-DDE-Remix/ISO-Build/actions/runs/45981240945/job/140445377978)
已完成真实 `go1.27.4-X:nodwarf5 linux/amd64` / GLib `2.90.1` 构建，
原生 override 工具、RPM buildroot 的严格 `%check`、最终镜像中编译后的
`away=['XF86Away']` 与背景默认值均通过。实际 binary RPM SHA-256 为
`4a292037c9cf2d0a742da489d1f40d06d855f176c399c67d1a1185fe67f27f20`。
本次原生验证使用临时 `6.0.13-1.1.remix1.fc45`，与维护者 `6.0.13-2` 使用同一
XML 补丁和严格检查；没有声称维护者版本已在 COPR 构建，也没有用 compose 成功
代替桌面登录或安装验收。

### 登录、依赖与 Logo

DDM 补丁已实际应用到固定 0.5.0 源文件，并检查初始 VT 为 1 和 7 的配置结果。
Treeland 的 Xwayland helper 直接执行 `Xwayland`，构建启用该功能；这类外部执行
不会自动形成 ELF 库依赖，因此声明 `/usr/bin/Xwayland`。

Treeland 固定上游 `859a8c314f00947bc98168f46631ba10f9c7e6fa` 的资源构建使用
`/dsg/icons` 前缀。实际旧 VM 的 `file::/dsg/logo.svg` 错误，与错误 fallback 及
QUrl 转换一致；DTK 对缺失的 LogoTransparent 返回第三参数，新的 qrc URL 同时
修正 scheme 和资源路径。配置中已有的发行版 Logo 不受影响。
补丁适用性和配置路径已核对，尚未把这些源检查表述成重新编译或图形登录通过。

### dde-api 的无效附加规则

固定上游提交 `217260df489497007a52f5ca08fd1975256e468f` 的
[Makefile](https://github.com/linuxdeepin/dde-api/blob/217260df489497007a52f5ca08fd1975256e468f/Makefile)
把唯一的 `org.deepin.dde.device.rules` 安装到 `/var/lib/polkit-1/rules.d`。
该规则为活动会话的 Debian `sudo` 组自动授权蓝牙解锁，原 SPEC 直接收录整个目录。
实际 `.2` payload 为 `polkit-127-5.fc45`；对应固定版本的
[authority 源码](https://github.com/polkit-org/polkit/blob/9e4894c969eecf26a3ba762f4f7a268aa0fb3e51/src/polkitbackend/polkitbackendduktapeauthority.c)
默认读取 `/etc`、`/run`、`/usr/local/share`、`/usr/share` 下的 `polkit-1/rules.d`，
没有这个 `/var/lib` 位置。

同一上游的
[action policy](https://github.com/linuxdeepin/dde-api/blob/217260df489497007a52f5ca08fd1975256e468f/misc/polkit-action/org.deepin.dde.device.unblock-bluetooth-devices.policy.in)
对活动会话要求 `auth_admin_keep`，对其他会话为 `no`；
[device 调用](https://github.com/linuxdeepin/dde-api/blob/217260df489497007a52f5ca08fd1975256e468f/device/device.go)
允许交互认证，并在授权成功后才执行 `rfkill unblock bluetooth`。
RPM 已声明 `rfkill` 运行依赖。

本次只在 buildroot 清理该无效规则和空目录，去掉对应 `%files` 条目；保留 action
policy、程序和服务。没有将规则移入有效目录或扩大无密码授权。本项是打包清理，
不是已确认的黑屏原因，也没有进行真实蓝牙硬件或交互认证测试。

### 编译参数

实际 Fedora 45 RPM 宏将 build_cxxflags 传给 CXXFLAGS；显式 CMAKE_CXX_FLAGS 会
覆盖这条路径。dde-shell 上游还启用了 -Werror，因此保留原 deprecation suppression。
11 个 SPEC 的变更均限于 Release、flags 行和 changelog；没有关闭 LTO 或放宽全局警告。
**这 11 个包尚未重新编译，需要按维护者的 COPR 自测结果继续确认。**

## 尚未确认的故障

旧 VM 的剪贴板 GUI 服务约 45 秒超时，但程序、unit 与三个 D-Bus activation 名称
匹配。初始化发生在 GUI 注册 BusName 之前；旧日志没有给出具体阻塞点，暂不改包。
可选 reportlog 库加载告警及设置分组占位告警，也没有被当作已证明的桌面崩溃原因。

## 后续构建与测试重点

DFM 需完整重建所有同源运行包，不能只替换 framework。随后优先检查 schemas 的
RPM `%check`、普通桌面组安装后的背景、DDM/Treeland 登录和 Xwayland 应用。
compiler flags 提交可独立自测；若恢复 Fedora 参数暴露新的真实编译错误，应按
具体报错修正源码，保留发行版参数。

SELinux 保持 Enforcing。新的 ISO 桌面与加密安装结果由 ISO-Build 的真实 VM 报告
另行记录，不以静态 SPEC 审查或容器探针代替。
