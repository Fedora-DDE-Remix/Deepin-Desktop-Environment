%global debug_package %{nil}

Name:           dde-api
Version:        6.2.1
Release:        1%{?dist}
Summary:        Go language bindings and helper services for dde-daemon
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-api
Source0:        %{url}/archive/%{version}/dde-api-%{version}.tar.gz

BuildRequires:  golang
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)

Requires:       deepin-desktop-base
Requires:       rfkill
Requires:       gvfs

%description
dde-api provides Go language bindings for dde-daemon and a set of helper
services used by the DDE session (dde-open, sound themes, display helpers,
locale helpers and polkit services).

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the DDEAPI C++ header and CMake configuration.

%prep
%autosetup -n dde-api-%{version} -p1

%build
for f in misc/polkit-action/*.policy.in; do cp "$f" "${f%.in}"; done
export GO111MODULE=on
export GOFLAGS="-mod=mod"
export GOPATH=%{_builddir}/gopath
%make_build build-binary build-dev INSTALL_LOCALE_HELPER=0

%install
export GO111MODULE=on
export GOFLAGS="-mod=mod"
export GOPATH=%{_builddir}/gopath
make DESTDIR=%{buildroot} install-binary install-misc INSTALL_LOCALE_HELPER=0 SYSTEMD_SERVICE_DIR=%{_unitdir} LIBDIR=%{_prefix}/lib
install -Dm644 misc/sysusers/deepin-daemon.conf %{buildroot}%{_sysusersdir}/deepin-daemon.conf
sed -i 's|set(DDE_API_INCLUDE_DIRS "/usr/include")|set(DDE_API_INCLUDE_DIRS "")|' %{buildroot}%{_datadir}/cmake/DDEAPI/DDEAPIConfig.cmake

%files
%license LICENSE
%doc README.md
%{_bindir}/dde-open
%{_prefix}/lib/deepin-api/
%{_datadir}/dde-api/
%{_datadir}/dbus-1/services/
%{_datadir}/dbus-1/system-services/
%{_datadir}/dbus-1/system.d/
%{_datadir}/polkit-1/actions/
%{_var}/lib/polkit-1/rules.d/
%{_datadir}/icons/hicolor/
%{_sysusersdir}/deepin-daemon.conf
%{_unitdir}/deepin-api-device.service
%{_unitdir}/deepin-login-sound.service
%{_unitdir}/deepin-shutdown-sound.service
%{_unitdir}/deepin-sound-theme-player.service

%files devel
%{_includedir}/dde-api/
%{_datadir}/cmake/DDEAPI/

%post
%systemd_post deepin-login-sound.service deepin-shutdown-sound.service deepin-api-device.service deepin-sound-theme-player.service

%preun
%systemd_preun deepin-login-sound.service deepin-shutdown-sound.service deepin-api-device.service deepin-sound-theme-player.service

%postun
%systemd_postun_with_restart deepin-login-sound.service deepin-shutdown-sound.service deepin-api-device.service deepin-sound-theme-player.service

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial Fedora package.
