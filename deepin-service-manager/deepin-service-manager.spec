Name:           deepin-service-manager
Version:        6.2.1
Release:        2%{?dist}
Summary:        Service manager framework for DDE
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-service-manager
Source0:        %{url}/archive/%{version}/deepin-service-manager-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  pkgconfig(dbus-1)

%description
Deepin service manager loads and manages DDE service plugins for both the
system and the user session.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains libdeepin-qdbus-service development files.

%prep
%autosetup -n deepin-service-manager-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/deepin-service-manager
%{_libdir}/libdeepin-qdbus-service.so*
%{_datadir}/deepin-service-manager/
%{_datadir}/dbus-1/system.d/org.deepin.ServiceManager1.conf
%{_datadir}/deepin-debug-config/deepin-debug-config.d/org.deepin.service.manager.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/org.deepin.service.manager.json
%{_unitdir}/deepin-service-manager.service
%{_unitdir}/deepin-service-group@.service
%{_unitdir}/deepin-service-plugin@.service
%{_unitdir}/deepin-service-group@deepin-daemon.service.d/override.conf
%{_unitdir}/multi-user.target.wants/deepin-service-manager.service
%{_userunitdir}/deepin-service-manager.service
%{_userunitdir}/deepin-service-group@.service
%{_userunitdir}/deepin-service-plugin@.service
%{_userunitdir}/dde-session-initialized.target.wants/deepin-service-manager.service

%files devel
%{_includedir}/deepin-qdbus-service/
%{_libdir}/libdeepin-qdbus-service.so
%{_libdir}/pkgconfig/deepin-qdbus-service.pc
%{_libdir}/cmake/deepin-qdbus-service/

%post
%systemd_post deepin-service-manager.service

%preun
%systemd_preun deepin-service-manager.service

%postun
%systemd_postun_with_restart deepin-service-manager.service

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-2
- Add the missing Dtk6Core build dependency.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
