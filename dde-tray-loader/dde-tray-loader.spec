Name:           dde-tray-loader
Version:        6.2.1
Release:        2%{?dist}
Summary:        Tray plugin loader and dock plugins for DDE
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-tray-loader
Source0:        %{url}/archive/%{version}/dde-tray-loader-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6WidgetsPrivate)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(KF6WindowSystem) >= 6.6
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xtest)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(cups)

# The loader is started by dde-shell through dde-tray-loader.target.  Do not
# add a hard dde-shell requirement here: dde-shell BuildRequires this
# package's -devel files, and a runtime requirement would create a build cycle.
Requires:       dde-daemon

%description
dde-tray-loader provides the tray plugin loader, the tray plugin interface
library and the standard dock/tray plugins for DDE.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the dde-dock plugin interfaces and CMake/pkg-config
files.

%prep
%autosetup -n dde-tray-loader-%{version} -p1

%build
%cmake -GNinja -DDTL_BUILD_WITH_QT6=ON -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_sysconfdir}
if [ -d %{buildroot}%{_prefix}/etc/dde-dock ]; then mv %{buildroot}%{_prefix}/etc/dde-dock %{buildroot}%{_sysconfdir}/; fi

%files
%license LICENSES/
%doc README.md
%{_libexecdir}/trayplugin-loader
%{_prefix}/lib/dde-dock/plugins/
%{_datadir}/dde-dock/
%{_datadir}/trayplugin-loader/translations/
%{_datadir}/dsg/configs/org.deepin.dde.dock/
%{_datadir}/dsg/configs/org.deepin.dde.tray-loader/
%{_qt6_plugindir}/wayland-shell-integration/libplugin-shell.so
%{_libdir}/libdde-trayplugin-interface.so.2*
%config(noreplace) %{_sysconfdir}/dde-dock/indicator/keybord_layout.json
%{_userunitdir}/dde-tray-loader.target
%{_userunitdir}/dde-tray-loader@.service
%{_userunitdir}/dde-tray-loader.target.wants/

%files devel
%{_includedir}/dde-dock/
%{_includedir}/dde-tray-loader/
%{_libdir}/libdde-trayplugin-interface.so
%{_libdir}/pkgconfig/dde-dock.pc
%{_libdir}/pkgconfig/dde-tray-loader.pc
%{_libdir}/cmake/DdeTrayLoader/
%{_libdir}/cmake/DdeDock/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-2
- Match upstream: require dde-daemon, not dde-shell/dde-application-manager.
  This removes the dde-shell <-> dde-tray-loader build cycle.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
