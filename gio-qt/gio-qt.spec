Name:           gio-qt
Version:        0.0.16
Release:        1%{?dist}
Summary:        GIO wrapper for Qt
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/gio-qt
Source0:        %{url}/archive/%{version}/gio-qt-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(giomm-2.4)
BuildRequires:  glibmm24-devel

%description
gio-qt is a GIO wrapper for Qt, used by DDE clipboard and file manager
integration.

%package        qt6
Summary:        Qt 6 build of %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    qt6
This package contains the Qt 6 build of gio-qt.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-qt6%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n gio-qt-%{version} -p1

%build
%cmake -GNinja -DBUILD_TESTS=OFF -DBUILD_UTILS=OFF -DBUILD_DOCS=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libgio-qt.so.0*

%files qt6
%{_libdir}/libgio-qt6.so.0*

%files devel
%{_includedir}/gio-qt/
%{_libdir}/libgio-qt.so
%{_libdir}/libgio-qt6.so
%{_libdir}/pkgconfig/gio-qt.pc
%{_libdir}/pkgconfig/gio-qt6.pc

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 0.0.16-1
- Initial Fedora package.
