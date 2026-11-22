%global debug_package %{nil}

Name:           dde-shell
Version:        6.2.1
Release:        1%{?dist}
Summary:        DDE shell, dock and desktop plugin framework
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-shell
Source0:        %{url}/archive/%{version}/dde-shell-%{version}.tar.gz
Patch0:         01-optional-examples.patch
Patch1:         02-strip-usr-include.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickTemplates2)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandCompositor)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6WaylandCompositorPrivate)
BuildRequires:  cmake(Qt6QuickTemplates2Private)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(DDEAPI)
BuildRequires:  cmake(DDEApplicationManager)
BuildRequires:  cmake(DdeTrayLoader)
BuildRequires:  cmake(TreelandProtocols) >= 0.9.0
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-io)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-res)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  yaml-cpp-devel

Requires:       dde-application-manager
Requires:       dde-tray-loader
Requires:       treeland-protocols

%description
dde-shell provides the DDE shell process, the dock, the desktop containment
and the plugin framework used by DDE applets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the dde-shell headers and CMake configuration.

%prep
%autosetup -n dde-shell-%{version} -p1

%build
%cmake -GNinja -DBUILD_WITH_X11=ON -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF \
  -DINCLUDE_INSTALL_DIR=%{_includedir}/dde-shell \
  -DCMAKE_CXX_FLAGS="-Wno-deprecated-declarations -fPIE"
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-shell
%{_libdir}/libdde-shell.so.1*
%{_libdir}/libdde-shell-dock.so.1*
%{_libdir}/libds-notification-shared.so.1*
%{_libdir}/qt6/qml/org/deepin/ds/
%{_libdir}/dde-shell/
%{_datadir}/dde-shell/
%{_datadir}/applications/org.deepin.dde-shell.desktop
%{_datadir}/dsg/configs/org.deepin.dde.shell/
%{_datadir}/dsg/configs/org.deepin.ds.dock/
%{_datadir}/dde-dock/icons/dcc-setting/dcc-multitasking-view.dci
%{_datadir}/dsg/configs/overrides/org.deepin.dde.shell/
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.shell.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.dde.shell.json
%{_userunitdir}/dde-shell@.service
%{_userunitdir}/dde-shell-plugin@.service
%exclude %{_libdir}/dde-shell/org.deepin.ds.example*
%exclude %{_datadir}/dde-shell/org.deepin.ds.example*
%exclude %{_datadir}/dsg/configs/org.deepin.dde.shell/org.deepin.ds.example.json

%files devel
%{_includedir}/dde-shell/
%{_libdir}/libdde-shell.so
%{_libdir}/libdde-shell-dock.so
%{_libdir}/libds-notification-shared.so
%{_libdir}/cmake/DDEShell/
%{_libdir}/cmake/DDEShellDock/

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
