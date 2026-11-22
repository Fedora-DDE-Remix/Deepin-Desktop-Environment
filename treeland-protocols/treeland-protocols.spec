Name:           treeland-protocols
Version:        0.9.1
Release:        2%{?dist}
Summary:        Wayland protocol definitions for Treeland
License:        MIT
URL:            https://github.com/linuxdeepin/treeland-protocols
Source0:        %{url}/archive/%{version}/treeland-protocols-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  make

%description
Wayland protocol XML definitions used by the Treeland compositor and its
clients.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains CMake and pkg-config files for %{name}.

%prep
%autosetup -n treeland-protocols-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSES/
%doc README.md
%{_datadir}/treeland-protocols/

%files devel
%{_datadir}/cmake/TreelandProtocols/
%{_datadir}/pkgconfig/treeland-protocols.pc

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 0.9.1-2
- Require ninja-build for the Ninja CMake generator.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 0.9.1-1
- Initial Fedora package.
