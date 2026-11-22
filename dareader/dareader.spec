Name:           dareader
%global commit 79892d8d4e223b436b0f9a9bb55a5735b553cc76

Version:        1.0.1
Release:        1.20260729git79892d8%{?dist}
Summary:        Library for reading image/video data from deepin-authentication
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dareader
Source0:        %{url}/archive/%{commit}/dareader-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
dareader reads image and video data passed by the Deepin authentication
service over a file descriptor.

%package        libs
Summary:        Shared library for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    libs
This package contains the dareader shared library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n dareader-%{commit} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libdareader.so.1*

%files devel
%{_includedir}/dareader/
%{_libdir}/libdareader.so
%{_libdir}/pkgconfig/dareader.pc

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.0.1-1.20260729git79892d8
- Initial Fedora package.
