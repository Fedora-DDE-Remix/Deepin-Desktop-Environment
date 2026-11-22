%global srcname dde-qtintegration

Name:           deepin-qt6integration
Version:        6.7.54
Release:        1%{?dist}
Summary:        Qt 6 platform integration plugins for the Deepin desktop
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-qtintegration
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  cmake(DtkBuildHelper)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

Requires:       dtk6widget
Requires:       qt6-qtbase-gui

%description
Deepin Qt 6 integration provides the Deepin platform theme, icon engine,
image format plugins and the Chameleon widget style.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%cmake -GNinja -DDTK5=OFF -DENABLE_QT_XDG_ICON_LOADER=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_qt6_plugindir}/iconengines/libdicon.so
%{_qt6_plugindir}/iconengines/libdsvgicon.so
%{_qt6_plugindir}/imageformats/libdci.so
%{_qt6_plugindir}/imageformats/libdsvg.so
%{_qt6_plugindir}/platformthemes/libqdeepin.so
%{_qt6_plugindir}/styles/libchameleon.so

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.7.54-1
- Initial Fedora package (Qt 6 only).
