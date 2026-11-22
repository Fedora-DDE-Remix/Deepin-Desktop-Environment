Name:           dde-application-manager
Version:        6.2.1
Release:        1%{?dist}
Summary:        Application manager for the Deepin desktop environment
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-application-manager
Source0:        %{url}/archive/%{version}/dde-application-manager-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(TreelandProtocols)
BuildRequires:  cmake(DDEAPI)

Requires:       dde-daemon
Requires:       glib2

%description
dde-application-manager implements the org.desktopspec application manager
D-Bus interfaces used by the DDE shell, dock and launcher.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the DDEApplicationManager CMake configuration.

%prep
%autosetup -n dde-application-manager-%{version} -p1

%build
%cmake -GNinja -DBUILD_TESTING=OFF -DBUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install
# Debian-only update hook.
rm -rf %{buildroot}%{_sysconfdir}/dpkg %{buildroot}%{_prefix}/etc/dpkg
rm -f  %{buildroot}%{_libexecdir}/dde-application-manager/debFix.sh
rm -f  %{buildroot}%{_datadir}/deepin/dde-application-manager/hooks.d/2-debFix.json

%post
%systemd_post org.desktopspec.ApplicationUpdateNotifier1.service

%preun
%systemd_preun org.desktopspec.ApplicationUpdateNotifier1.service

%postun
%systemd_postun_with_restart org.desktopspec.ApplicationUpdateNotifier1.service

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-application-manager
%{_bindir}/dde-am
%{_bindir}/app-identifier
%{_libexecdir}/deepin/application-manager/
%{_unitdir}/org.desktopspec.ApplicationUpdateNotifier1.service
%{_userunitdir}/org.desktopspec.ApplicationManager1.service
%{_userunitdir}/dde-autostart.service
%{_userunitdir}/dde-autostart@quick-login.service
%{_userunitdir}/dde-session-pre.target.wants/org.desktopspec.ApplicationManager1.service
%{_userunitdir}/dde-session.target.wants/dde-autostart.service
%{_userunitdir}/app-DDE-.service.d/override.conf
%{_datadir}/dbus-1/system-services/org.desktopspec.ApplicationUpdateNotifier1.service
%{_datadir}/dbus-1/system.d/org.desktopspec.ApplicationUpdateNotifier1.conf
%{_datadir}/dbus-1/services/org.desktopspec.ApplicationManager1.service
%{_datadir}/dde-application-manager/
%{_datadir}/deepin/dde-application-manager/
%{_datadir}/dsg/configs/org.deepin.dde.application-manager/
%{_datadir}/bash-completion/completions/dde-am

%files devel
%{_libdir}/cmake/DDEApplicationManager/

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
