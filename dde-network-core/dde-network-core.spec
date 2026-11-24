Name:           dde-network-core
Version:        6.2.1
Release:        2%{?dist}
Summary:        DDE network library, service and desktop plugins
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-network-core
Source0:        %{url}/archive/%{version}/dde-network-core-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-network-core/01-skip-dss-plugin.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconf-pkg-config
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(KF6NetworkManagerQt)
BuildRequires:  cmake(DdeControlCenter)
BuildRequires:  cmake(DdeDock)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(gsettings-qt6)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libcurl-devel
BuildRequires:  systemd-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  dde-control-center-devel >= 6.2.1
BuildRequires:  dde-tray-loader-devel >= 6.2.1

Requires:       NetworkManager
Requires:       dde-daemon
Requires:       deepin-service-manager
Requires:       kf6-networkmanager-qt
Requires:       gsettings-qt6
Requires:       polkit
Recommends:     NetworkManager-wifi
Recommends:     NetworkManager-wwan
Recommends:     dnsmasq

%description
dde-network-core provides the DDE network state library, the Network1
service plugin, the control center network module, the dock network tray
plugin and the network secret dialog.

The lock-screen network module is not built because the session shell is
not part of the Fedora DDE port.

%package        devel
Summary:        Development files for dde-network-core
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development headers and pkg-config metadata for dde-network-core.

%package -n     dcc-network-plugin
Summary:        Network module for the DDE control center
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dde-control-center >= 6.2.1
Recommends:     NetworkManager-openvpn
Recommends:     NetworkManager-l2tp
Recommends:     NetworkManager-pptp
Recommends:     NetworkManager-vpnc
Recommends:     NetworkManager-openconnect
Recommends:     NetworkManager-strongswan
Recommends:     NetworkManager-sstp

%description -n dcc-network-plugin
The network configuration module for the DDE control center.

%package -n     dock-network-plugin
Summary:        Network plugin for the DDE dock
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dde-tray-loader

%description -n dock-network-plugin
The network tray plugin for the DDE dock.

%prep
%autosetup -n dde-network-core-%{version} -p1

%build
%cmake -GNinja \
  -DBUILD_TESTS=OFF \
  -DBUILD_EXAMPLE=OFF \
  -DBUILD_DSS_PLUGIN=OFF \
  -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
  -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir}
%cmake_build

%install
%cmake_install

%files
%license LICENSES/
%doc README.md
%{_libdir}/libdde-network-core6.so.*
%{_datadir}/dde-network-core/translations/
%{_datadir}/dsg/configs/org.deepin.dde.network/
%{_libdir}/deepin-service-manager/libnetwork-service.so
%{_datadir}/deepin-service-manager/system/plugin-system-network.json
%{_datadir}/deepin-service-manager/user/plugin-session-network.json
%{_datadir}/deepin-service-manager/network-service/translations/
%config(noreplace) %{_sysconfdir}/NetworkManager/conf.d/deepin.dde.daemon.conf
%{_datadir}/dbus-1/system.d/org.deepin.dde.Network1.conf
%{_datadir}/polkit-1/actions/com.deepin.dde.network.policy
%{_prefix}/lib/deepin-daemon/dde-network-secret-dialog

%files devel
%{_includedir}/libddenetworkcore/
%{_libdir}/libdde-network-core6.so
%{_libdir}/pkgconfig/dde-network-core.pc

%files -n dcc-network-plugin
%{_libdir}/dde-control-center/plugins_v1.1/network/
%{_datadir}/dde-control-center/translations/v1.1/network_*.qm
%{_datadir}/dsg/configs/org.deepin.dde.control-center/network/
%{_datadir}/dde-control-center/permission-interfaces/org.deepin.dcc-network.json

%files -n dock-network-plugin
%{_prefix}/lib/dde-dock/plugins/system-trays/libdock-network-plugin.so
%{_datadir}/dock-network-plugin/translations/
%{_datadir}/dde-dock/icons/dcc-setting/dcc-network.dci

%changelog
* Tue Nov 24 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-2
- Add qt6-qtbase-private-devel; Qt6WaylandClientPrivate needs
  Qt6CorePrivate, which the previous local buildroot provided implicitly.

* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package for DDE 25/Treeland.
- Build the control center and dock network plugins; skip the lock-screen
  plugin because dde-session-shell is not packaged yet.
