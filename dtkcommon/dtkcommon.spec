%global debug_package %{nil}

Name:           dtkcommon
Version:        6.7.54
Release:        2%{?dist}
Summary:        A public project for building DTK libraries
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/dtkcommon
Source0:        %{url}/archive/%{version}/dtkcommon-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc-c++
BuildRequires:  make

%description
A public project for building DTK libraries.  It provides the DTK CMake
helper modules and the shared DTK DConfig metadata.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains the DTK CMake helper modules.

%prep
%autosetup -n dtkcommon-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_datadir}/dsg/configs/org.deepin.dtk.preference.json

%files devel
%{_libdir}/cmake/Dtk/
%{_libdir}/cmake/Dtk6/
%{_libdir}/cmake/DtkBuildHelper/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.7.54-2
- Require ninja-build for the Ninja CMake generator.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 6.7.54-1
- Initial Fedora package (DTK 6.7.54, Qt 6 only).
