Name:           dde-session
Version:        6.2.1
Release:        1%{?dist}
Summary:        DDE session manager and session targets
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-session
Source0:        %{url}/archive/%{version}/dde-session-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Tools)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)

Requires:       dde-daemon
Requires:       dde-application-manager
Requires:       dde-shell
Requires:       dde-polkit-agent

%description
dde-session provides the DDE session manager, session targets and the small
helper binaries used during login and logout.

%prep
%autosetup -n dde-session-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-session
%{_bindir}/dde-quick-login
%{_bindir}/dde-keyring-checker
%{_bindir}/dde-version-checker
%{_bindir}/dde-xsettings-checker
%{_bindir}/dde-oom-score-adj
%{_libexecdir}/dde-session-ctl
%{_libexecdir}/deepin/dde-session
%{_libexecdir}/deepin/dde-session-loader-wrapper
%{_datadir}/dbus-1/services/org.deepin.dde.Session1.service
%{_datadir}/xsessions/deepin.desktop
%{_datadir}/dsg/configs/org.deepin.dde.session/
%config(noreplace) %{_sysconfdir}/X11/Xsession.d/00deepin-dde-env
%config(noreplace) %{_sysconfdir}/X11/Xsession.d/01deepin-profile
%config(noreplace) %{_sysconfdir}/X11/Xsession.d/97deepin-keyring-wb
%config(noreplace) %{_sysconfdir}/profile.d/deepin-xdg-dir.sh
%config(noreplace) %{_sysconfdir}/xdg/autostart/dde-oom-score-adj.desktop
%{_userunitdir}/dde-session*.target
%{_userunitdir}/dde-session*.service
%{_userunitdir}/dde-session*.target.wants/
%{_userunitdir}/dde-session-shutdown.target.d/
%{_userunitdir}/dde-quick-login@x11.service
%{_userunitdir}/dde-keyring*.service
%{_userunitdir}/dde-lock.service
%{_userunitdir}/dde-polkit-agent.service
%{_userunitdir}/dde-shell@DDE.service
%{_userunitdir}/dde-shell-plugin@org.deepin.ds.desktop.service
%{_userunitdir}/dde-version-checker*.service
%{_userunitdir}/dde-xsettings-checker.service

%post
%systemd_user_post dde-session-manager.service

%preun
%systemd_user_preun dde-session-manager.service

%postun
%systemd_user_postun_with_restart dde-session-manager.service

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
