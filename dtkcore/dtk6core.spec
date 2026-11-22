%global srcname dtkcore

Name:           dtk6core
Version:        6.7.54
Release:        2%{?dist}
Summary:        Deepin tool kit core modules
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        %{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6CorePrivate)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6ToolsTools)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Dtk6Log)
BuildRequires:  cmake(DtkBuildHelper) >= %{version}
BuildRequires:  cmake(spdlog)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(libsystemd)

Requires:       deepin-desktop-base

%description
Deepin tool kit core modules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       dtkcommon-devel%{_isa}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n %{srcname}-%{version} -p1 -C
# Fedora does not provide /etc/os-version; deepin-desktop-base provides
# /etc/dde-version instead.
sed -i 's|/etc/os-version|/etc/dde-version|' src/dsysinfo.cpp

%build
%cmake -GNinja -DDTK5=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdtk6core.so.6*
%{_libexecdir}/dtk6/DCore/

%files devel
%{_libdir}/libdtk6core.so
%{_includedir}/dtk6/DCore/
%{_libdir}/cmake/Dtk6Core/
%{_libdir}/cmake/Dtk6CMake/
%{_libdir}/cmake/Dtk6DConfig/
%{_libdir}/cmake/Dtk6Tools/
%{_libdir}/pkgconfig/dtk6core.pc
%{_qt6_archdatadir}/mkspecs/modules/*.pri
%{_qt6_archdatadir}/mkspecs/features/*.prf

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.7.54-2
- Do not require a 6.7.54 CMake version from dtk6log; upstream's CMake
  package version is 0.7.54.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.7.54-1
- Initial Fedora package (DTK 6.7.54, Qt 6 only).
