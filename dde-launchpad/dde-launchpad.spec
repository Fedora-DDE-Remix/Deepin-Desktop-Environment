Name:           dde-launchpad
Version:        6.2.1
Release:        2%{?dist}
Summary:        Application launcher for the Deepin desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-launchpad
Source0:        %{url}/archive/%{version}/dde-launchpad-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(DDEShell)
BuildRequires:  cmake(AppStreamQt)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)

Requires:       dde-shell
Requires:       dde-application-manager
Requires:       appstream

%description
dde-launchpad provides the full-screen application launcher and the dock
launcher applet for DDE.

%prep
%autosetup -n dde-launchpad-%{version} -p1

%build
%cmake -GNinja -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/launchpadcommon.so
%{_libdir}/dde-shell/org.deepin.ds.dock.launcherapplet.so
%{_datadir}/dde-shell/org.deepin.ds.dock.launcherapplet/
%{_datadir}/dsg/configs/dde-launchpad/
%{_datadir}/dsg/configs/org.deepin.dde.shell/org.deepin.ds.launchpad.json
%{_datadir}/metainfo/org.deepin.dde.shell.launchpad.appdata.xml
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.launchpad.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.dde.launchpad.json

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-2
- Add Qt6GuiPrivate/Qt6CorePrivate.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
