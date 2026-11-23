Name:           deepin-fcitx5configtool-plugin
Version:        6.0.41
Release:        2%{?dist}
Summary:        Fcitx5 input method configuration plugin for DDE Control Center
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/deepin-fcitx5configtool-plugin
Source0:        %{url}/archive/%{version}/deepin-fcitx5configtool-plugin-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-fcitx5configtool-plugin/01-fedora-cxx20.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(DdeControlCenter)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Fcitx5Core)
BuildRequires:  cmake(Fcitx5Config)
BuildRequires:  cmake(Fcitx5Utils)
BuildRequires:  cmake(Fcitx5Qt6DBusAddons)
BuildRequires:  cmake(Fcitx5Qt6WidgetsAddons)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  xkeyboard-config-devel
BuildRequires:  iso-codes-devel

Requires:       dde-control-center
Requires:       fcitx5
Requires:       fcitx5-qt

%description
This package adds the Fcitx5 input method configuration page to the Deepin
Control Center.

%prep
%autosetup -n deepin-fcitx5configtool-plugin-%{version} -p1

%build
%cmake -GNinja \
  -DBUILD_UOS=OFF \
  -DENABLE_KCM=OFF \
  -DENABLE_CONFIG_QT=OFF \
  -DENABLE_TEST=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSES/
%doc README.md
%{_libdir}/dde-control-center/plugins_v1.1/fcitx5configtool/
%{_libexecdir}/dcc-fcitx5configtool-exec
%{_bindir}/fcitx5-helper
%{_bindir}/kbd-layout-viewer6
%config(noreplace) %{_sysconfdir}/xdg/autostart/fcitx5-helper.desktop
%{_datadir}/dde-control-center/translations/v1.1/fcitx5configtool_*.qm
%{_datadir}/applications/kbd-layout-viewer6.desktop
%{_datadir}/locale/*/LC_MESSAGES/deepin-fcitx5-configtool.mo

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.0.41-1
- Initial Fedora package; build against Fedora fcitx5 5.1.23.
