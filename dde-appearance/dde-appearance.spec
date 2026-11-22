Name:           dde-appearance
Version:        6.2.1
Release:        1%{?dist}
Summary:        Appearance service for the Deepin desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-appearance
Source0:        %{url}/archive/%{version}/dde-appearance-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(DDEAPI)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gsettings-qt6)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-cursor)

Requires:       deepin-service-manager
Requires:       gsettings-qt6
Requires:       gtk3
Requires:       fontconfig

%description
dde-appearance provides the DDE appearance service: themes, icons, cursors,
fonts, wallpapers and the fake window manager used by Treeland sessions.

%prep
%autosetup -n dde-appearance-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-fakewm
%{_libdir}/deepin-service-manager/libplugin-dde-appearance.so
%{_datadir}/deepin-service-manager/user/plugin-dde-appearance.json
%{_datadir}/dsg/configs/org.deepin.dde.appearance/
%{_datadir}/dbus-1/services/com.deepin.wm.service
%{_datadir}/dbus-1/services/org.deepin.dde.Appearance1.service
%{_datadir}/dde-appearance/
%{_datadir}/plugin-dde-appearance/translations/
%{_userunitdir}/dde-fakewm.service

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
