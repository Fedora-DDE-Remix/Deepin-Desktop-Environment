Name:           udisks2-qt6
Version:        6.0.1
Release:        1%{?dist}
Summary:        Qt 6 wrapper for the UDisks2 D-Bus API
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/udisks2-qt6
Source0:        %{url}/archive/%{version}/udisks2-qt6-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)

%description
udisks2-qt6 is a Qt 6 library for accessing the UDisks2 D-Bus API.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n udisks2-qt6-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libudisks2-qt6.so.*

%files devel
%{_includedir}/udisks2-qt6/
%{_libdir}/libudisks2-qt6.so
%{_libdir}/pkgconfig/udisks2-qt6.pc
%{_libdir}/cmake/udisks2-qt6/

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.0.1-1
- Initial Fedora package.
