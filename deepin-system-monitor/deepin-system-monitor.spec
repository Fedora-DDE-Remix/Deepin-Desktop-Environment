Name:           deepin-system-monitor
Version:        6.5.49
Release:        2%{?dist}
Summary:        System monitor for the Deepin desktop environment

License:        GPL-3.0-or-later AND MIT AND LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-system-monitor
Source0:        %{url}/archive/%{version}/deepin-system-monitor-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-system-monitor/deepin_system_monitor.te
Source2:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-system-monitor/deepin_system_monitor.fc
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-system-monitor/01-skip-ts-convert.patch

BuildRequires:  cmake
BuildRequires:  selinux-policy-devel
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  qt6-linguist
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(PolkitQt6-1)
BuildRequires:  dde-tray-loader-devel
BuildRequires:  pkgconfig(dde-dock)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  libpcap-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXext-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  libicu-devel
BuildRequires:  systemd-devel

Requires:       dde-tray-loader
Requires:       deepin-service-manager
Requires:       polkit
Requires:       hicolor-icon-theme
Requires:       dde-daemon-selinux >= 6.2.1-9
Requires:       %{name}-selinux = %{version}-%{release}
Recommends:     deepin-manual

%description
Deepin System Monitor displays CPU, memory, disk and network usage,
lists processes and services, and provides the DDE dock plugin that shows
system load in the panel.

%package        selinux
Summary:        SELinux mount rules for the Deepin system monitor
Requires:       selinux-policy-targeted
Requires:       policycoreutils

%description    selinux
This package allows systemd's init_t domain to set up the InaccessiblePaths
mounts used by the system monitor's root service.  It grants only the
mount-on permission for /etc/shadow and /etc/selinux, not read or write
access to those files.

%prep
%autosetup -n deepin-system-monitor-%{version} -p1

%build
%cmake -GNinja -DVERSION=%{version} -DDOTEST=OFF
%cmake_build
cp %{SOURCE1} deepin_system_monitor.te
cp %{SOURCE2} deepin_system_monitor.fc
make -f /usr/share/selinux/devel/Makefile deepin_system_monitor.pp

%install
%cmake_install
install -Dm644 deepin_system_monitor.pp %{buildroot}%{_datadir}/selinux/packages/deepin_system_monitor.pp

%post
%systemd_post deepin-system-monitor-system-server.service

%preun
%systemd_preun deepin-system-monitor-system-server.service

%postun
%systemd_postun_with_restart deepin-system-monitor-system-server.service

%post selinux
if [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -i /usr/share/selinux/packages/deepin_system_monitor.pp 2>/dev/null || :
fi

%postun selinux
if [ "$1" -eq 0 ] && [ -x /usr/sbin/semodule ]; then
    /usr/sbin/semodule -r deepin_system_monitor 2>/dev/null || :
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-system-monitor
%{_bindir}/deepin-system-monitor-plugin-popup
%{_bindir}/deepin-system-monitor-server
%{_prefix}/lib/dde-dock/plugins/libdeepin-system-monitor-plugin.so
%{_prefix}/lib/deepin-daemon/deepin-system-monitor-system-server
%{_unitdir}/deepin-system-monitor-system-server.service
%{_libdir}/deepin-service-manager/libdeepin-system-monitor-daemon.so
%{_datadir}/applications/deepin-system-monitor.desktop
%{_datadir}/dbus-1/services/com.deepin.SystemMonitorPluginPopup.service
%{_datadir}/dbus-1/services/com.deepin.SystemMonitorServer.service
%{_datadir}/dbus-1/system-services/org.deepin.SystemMonitorSystemServer.service
%{_datadir}/dbus-1/system.d/org.deepin.SystemMonitorSystemServer.conf
%{_datadir}/dde-dock/icons/dcc-setting/dcc-system-monitor.dci
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.system-monitor.json
%{_datadir}/deepin-service-manager/other/deepin-system-monitor-system-server.json
%{_datadir}/deepin-service-manager/user/deepin-system-monitor-daemon.json
%{_datadir}/deepin-system-monitor/
%{_datadir}/deepin-system-monitor-plugin/
%{_datadir}/deepin-system-monitor-plugin-popup/
%{_datadir}/deepin-manual/manual-assets/application/deepin-system-monitor/
%{_datadir}/dsg/configs/org.deepin.system-monitor/
%{_datadir}/glib-2.0/schemas/com.deepin.dde.dock.module.system-monitor.gschema.xml
%{_datadir}/polkit-1/actions/com.deepin.pkexec.deepin-system-monitor.policy
%{_datadir}/polkit-1/actions/org.deepin.deepin-system-monitor-system-server.policy

%files selinux
%{_datadir}/selinux/packages/deepin_system_monitor.pp

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 6.5.49-2
- Add deepin-system-monitor-selinux, allowing init_t to set up the
  InaccessiblePaths mounts for /etc/shadow and /etc/selinux.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.5.49-1
- Initial Fedora package.
