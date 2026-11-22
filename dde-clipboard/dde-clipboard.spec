Name:           dde-clipboard
Version:        6.1.39
Release:        1%{?dist}
Summary:        Clipboard history service for DDE
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-clipboard
Source0:        %{url}/archive/%{version}/dde-clipboard-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  cmake(DDEShell)
BuildRequires:  cmake(DdeTrayLoader)
BuildRequires:  pkgconfig(gio-qt6)

Requires:       dde-shell
Requires:       dde-tray-loader
Requires:       gio-qt6

%description
dde-clipboard provides clipboard history, a clipboard daemon and the dock
clipboard plugin.

%prep
%autosetup -n dde-clipboard-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-clipboard
%{_bindir}/dde-clipboard-daemon
%{_prefix}/lib/dde-dock/plugins/libdock-clipboard-plugin.so
%{_datadir}/dde-dock/
%{_datadir}/dde-clipboard/
%{_datadir}/dbus-1/services/org.deepin.dde.Clipboard1.service
%{_datadir}/dbus-1/services/org.deepin.dde.ClipboardLoader1.service
%{_datadir}/dbus-1/services/org.deepin.dde.daemon.Clipboard1.service
%{_datadir}/dsg/configs/org.deepin.dde.clipboard/
%config(noreplace) %{_sysconfdir}/xdg/autostart/dde-clipboard.desktop
%{_userunitdir}/dde-clipboard.service
%{_userunitdir}/dde-clipboard-daemon.service

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.1.39-1
- Initial Fedora package.
