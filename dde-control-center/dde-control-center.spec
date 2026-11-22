Name:           dde-control-center
Version:        6.1.113
Release:        1%{?dist}
Summary:        Control center for the Deepin desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-control-center
Source0:        %{url}/archive/%{version}/dde-control-center-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6QmlModelsPrivate)
BuildRequires:  cmake(Qt6QuickPrivate)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(DDEShell)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  pkgconfig(dareader)
BuildRequires:  pkgconfig(libdeepin_pw_check)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  openssl-devel
BuildRequires:  doxygen
BuildRequires:  gtest-devel
BuildRequires:  qt6-linguist

Requires:       dde-daemon
Requires:       dde-shell
Requires:       deepin-pw-check
Requires:       dareader
Requires:       polkit
Requires:       fcitx5

%description
The Deepin Control Center is the settings application for the Deepin desktop
environment.  It provides display, sound, network, Bluetooth, keyboard,
mouse, power, personalization and account settings.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the dde-control-center plugin development files.

%prep
%autosetup -n dde-control-center-%{version} -p1

%build
export PATH=%{_qt6_bindir}:$PATH
%cmake -GNinja \
  -DENABLE_WARNINGS_AS_ERRORS=OFF \
  -DDISABLE_AUTHENTICATION=OFF \
  -DDISABLE_PRIVACY_PLUGIN=ON \
  -DDISABLE_LANGUAGE=OFF \
  -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-control-center
%{_libexecdir}/deepin/dde-control-center
%{_libdir}/libdde-control-center.so.6*
%{_libdir}/libdcc-shared-utils.so.6*
%{_libdir}/libdcc-wallpaper-thumbnailer.so
%{_libdir}/dde-control-center/
%{_libdir}/dde-grand-search-daemon/plugins/searcher/
%{_datadir}/applications/org.deepin.dde.control-center.desktop
%{_datadir}/dbus-1/services/org.deepin.dde.ControlCenter1.service
%{_datadir}/dde-control-center/
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.control-center.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.dde.control-center.json
%{_datadir}/dsg/configs/org.deepin.dde.control-center/
%{_datadir}/dsg/configs/org.deepin.region-format.json
%{_datadir}/metainfo/org.deepin.dde.controlcenter.metainfo.xml
%{_userunitdir}/org.deepin.dde.control-center.service

%files devel
%{_includedir}/dde-control-center/
%{_libdir}/libdde-control-center.so
%{_libdir}/libdcc-shared-utils.so
%{_libdir}/cmake/DdeControlCenter/

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.1.113-1
- Initial Fedora package.
