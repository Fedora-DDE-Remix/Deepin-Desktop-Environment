Name:           dde-control-center
Version:        6.2.1
Release:        2%{?dist}
Summary:        Control center for the Deepin desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-control-center
Source0:        %{url}/archive/%{version}/dde-control-center-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-control-center/fedora-logo.png
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-control-center/01-fedora-branding.patch
Patch1:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-control-center/02-skip-ts-convert.patch

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
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6QmlModelsPrivate)
BuildRequires:  cmake(Qt6QuickPrivate)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  pkgconfig(wlr-protocols)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(DDEShell)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  pkgconfig(dareader)
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(libdeepin_pw_check)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(xcursor)
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
  -DDVERSION=%{version} \
  -DENABLE_WARNINGS_AS_ERRORS=OFF \
  -DDISABLE_AUTHENTICATION=OFF \
  -DDISABLE_PRIVACY_PLUGIN=ON \
  -DDISABLE_LANGUAGE=OFF \
  -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/dde-control-center/logo/fedora-logo.png

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
%{_prefix}/lib/dde-dock/plugins/
%{_datadir}/dde-dock/
%{_datadir}/dock-bluetooth-plugin/
%{_datadir}/dock-brightness-plugin/
%{_datadir}/dock-eye-comfort-mode-plugin/
%{_datadir}/dock-sound-plugin/
%{_datadir}/dock-wirelesscasting-plugin/
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.dde.control-center.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.dde.control-center.json
%{_datadir}/dsg/configs/org.deepin.dde.control-center/
%{_datadir}/dsg/configs/org.deepin.dde.dock/
%{_datadir}/dsg/configs/org.deepin.dde.tray-loader/
%{_datadir}/dsg/configs/org.deepin.region-format.json
%{_datadir}/metainfo/org.deepin.dde.controlcenter.metainfo.xml
%{_userunitdir}/org.deepin.dde.control-center.service

%files devel
%{_includedir}/dde-control-center/
%{_libdir}/libdde-control-center.so
%{_libdir}/libdcc-shared-utils.so
%{_libdir}/cmake/DdeControlCenter/

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-2
- Build with DVERSION=6.2.1 so the application reports the RPM version.
- Add 5px more space between the Fedora logo and the copyright text.

* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Update to 6.2.1.
- Add Fedora DDE Remix branding: report Fedora, the Fedora release number
  and the Fedora DDE Remix edition on the system information page, and show
  the Fedora logo instead of the Deepin one.
- Do not require deepin-desktop-ts-convert; install the shipped desktop file.
- Package the dock plugins added in 6.2.1 (sound, Bluetooth, brightness,
  eye comfort mode and wireless casting).
- Add the Qt6 Svg/Widgets, Dtk6Widget, dde-dock and Xcursor build
  requirements used by the new dock plugins.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.1.113-3
- Add wlr-protocols for the Treeland integration.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.1.113-2
- Add cmake(Qt6CorePrivate), required by Qt6 private components.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.1.113-1
- Initial Fedora package.
