%global tag 0.9.3-3

Name:           dde-seatd
Version:        0.9.3
Release:        5%{?dist}
Summary:        Seat management daemon and library for DDE
License:        MIT
URL:            https://github.com/linuxdeepin/dde-seatd
Source0:        %{url}/archive/%{tag}/dde-seatd-%{tag}.tar.gz
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-seatd/dde-seatd.conf
Source2:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-seatd/90-dde-seatd.preset

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  scdoc

Provides:       group(seat) = ZyBzZWF0IC0A

%description
dde-seatd is the DDE fork of seatd.  It provides the seatd daemon and the
libseat seat management library used by Deepin session components.  The
binary and library names intentionally match upstream seatd; this package
conflicts with the Fedora seatd package.

%package        libs
Summary:        Seat management library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    libs
This package contains the libseat shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n dde-seatd-%{tag} -p1

%build
%meson -Dlibseat-seatd=enabled -Dlibseat-logind=systemd -Dman-pages=disabled
%meson_build

%install
%meson_install
install -Dm644 %{SOURCE1} %{buildroot}%{_sysusersdir}/dde-seatd.conf
install -Dm644 %{SOURCE2} %{buildroot}%{_presetdir}/90-dde-seatd.preset

%post
%systemd_post dde-seatd.service

%preun
%systemd_preun dde-seatd.service

%postun
%systemd_postun_with_restart dde-seatd.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/dde-seatd
%{_bindir}/dde-seatd-launch
%{_unitdir}/dde-seatd.service
%{_sysusersdir}/dde-seatd.conf
%{_presetdir}/90-dde-seatd.preset

%files libs
%{_libdir}/libdde-seat.so.1*

%files devel
%{_includedir}/dde-seatd/libseat.h
%{_libdir}/libdde-seat.so
%{_libdir}/pkgconfig/libdde-seat.pc

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 0.9.3-1
- Initial Fedora package.
