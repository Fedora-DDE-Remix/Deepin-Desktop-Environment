Name:           dde-app-services
Version:        1.0.47
Release:        1%{?dist}
Summary:        DConfig service and tools for DDE
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-app-services
Source0:        %{url}/archive/%{version}/dde-app-services-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Gui)
BuildRequires:  pkgconfig(libsystemd)

%description
dde-app-services provides the DConfig configuration daemon, the dde-dconfig
command line tool and the DConfig editor.

%prep
%autosetup -n dde-app-services-%{version} -p1

%build
%cmake -GNinja -DDTK_VERSION=6 -DBUILD_DOCS=OFF -DBUILD_TESTING=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-dconfig
%{_bindir}/dde-dconfig-daemon
%{_bindir}/dde-dconfig-editor
%{_datadir}/dbus-1/interfaces/org.desktopspec.ConfigManager*.xml
%{_datadir}/dbus-1/system.d/org.desktopspec.ConfigManager.conf
%{_datadir}/dbus-1/system-services/org.desktopspec.ConfigManager.service
%{_unitdir}/dde-dconfig-daemon.service
%{_datadir}/dde-dconfig/
%{_datadir}/dde-dconfig-editor/
%{_datadir}/dsg/configs/
%{_datadir}/deepin-debug-config/deepin-debug-config.d/dde-dconfig-daemon.json
%{_datadir}/deepin-log-viewer/deepin-log.conf.d/dde-dconfig-daemon.json
%{_datadir}/bash-completion/completions/dde-dconfig
%{_datadir}/zsh/vendor-completions/_dde-dconfig

%post
%systemd_post dde-dconfig-daemon.service

%preun
%systemd_preun dde-dconfig-daemon.service

%postun
%systemd_postun_with_restart dde-dconfig-daemon.service

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.0.47-1
- Initial Fedora package.
