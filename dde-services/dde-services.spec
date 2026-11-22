Name:           dde-services
Version:        6.2.1
Release:        1%{?dist}
Summary:        DDE system and session service plugins
License:        GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT
URL:            https://github.com/linuxdeepin/dde-services
Source0:        %{url}/archive/%{version}/dde-services-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6DConfig)
BuildRequires:  cmake(TreelandProtocols) >= 0.6.0
BuildRequires:  cmake(deepin-qdbus-service)
BuildRequires:  pkgconfig(libpcap)
BuildRequires:  pkgconfig(polkit-qt6-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wlr-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-xinput)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  libpcap-devel
BuildRequires:  polkit-devel

Requires:       deepin-service-manager
Requires:       dde-daemon

%description
dde-services contains the DDE service-manager plugins and helper tools for
shortcuts, power, XSettings, ambient brightness, wallpaper caching and
desktop integration.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the DdeShortcutI18n CMake module.

%prep
%autosetup -n dde-services-%{version} -p1

%build
%cmake -GNinja -DENABLE_COVERAGE=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-shortcut-tool
%{_bindir}/extract_shortcuts_i18n
%{_libdir}/deepin-service-manager/libplugin-*.so
%{_libexecdir}/dde-services/
%{_datadir}/deepin-service-manager/
%{_datadir}/deepin/org.deepin.dde.keybinding/
%{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/system-services/
%{_datadir}/dbus-1/system.d/
%{_datadir}/dsg/configs/
%{_datadir}/plugin-power-session/translations/
%{_datadir}/polkit-1/actions/
%{_unitdir}/deepin-service-plugin@org.deepin.dde.WallpaperCache.service.d/override.conf
%{_userunitdir}/org.deepin.dde.XSettings1.service
%{_userunitdir}/dde-session-pre.target.wants/org.deepin.dde.XSettings1.service

%files devel
%{_prefix}/lib/cmake/DdeShortcutI18n/

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
