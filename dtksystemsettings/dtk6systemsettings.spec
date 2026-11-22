%global srcname dtksystemsettings

Name:           dtk6systemsettings
Version:        6.6.22
Release:        1%{?dist}
Summary:        Deepin Tool Kit system settings library
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtksystemsettings
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Dtk6Core) >= %{version}
BuildRequires:  doxygen

%description
Deepin Tool Kit system settings library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1

%build
%cmake -GNinja -DDTK5=OFF -DBUILD_DOCS=OFF -DBUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdtk6systemsettings.so.6*

%files devel
%{_libdir}/libdtk6systemsettings.so
%{_includedir}/dtk6/DSystemSettings/
%{_libdir}/cmake/Dtk6SystemSettings/
%{_libdir}/pkgconfig/dtk6systemsettings.pc
%{_libdir}/qt6/qt_lib_dtk6systemsettings.pri

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.6.22-1
- Initial Fedora package (DTK 6.6.22, Qt 6 only).
