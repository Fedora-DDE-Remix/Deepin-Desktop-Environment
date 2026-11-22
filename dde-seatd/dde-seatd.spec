Name:           dde-seatd
Version:        0.9.3
Release:        1%{?dist}
Summary:        Seat management daemon and library for DDE
License:        MIT
URL:            https://github.com/linuxdeepin/dde-seatd
Source0:        %{url}/archive/%{version}/dde-seatd-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  scdoc

Conflicts:      seatd

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
%autosetup -n dde-seatd-%{version} -p1

%build
%meson -Dlibseat-seatd=enabled -Dlibseat-logind=systemd -Dman-pages=disabled
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_bindir}/seatd
%{_bindir}/seatd-launch

%files libs
%{_libdir}/libseat.so.1*

%files devel
%{_includedir}/libseat.h
%{_libdir}/libseat.so
%{_libdir}/pkgconfig/libseat.pc

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 0.9.3-1
- Initial Fedora package.
