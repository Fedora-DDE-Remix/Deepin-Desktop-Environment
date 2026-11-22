Name:           util-dfm
Version:        1.4.6
Release:        2%{?dist}
Summary:        I/O, mount, burn and search libraries for DDE File Manager
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/util-dfm
Source0:        %{url}/archive/%{version}/util-dfm-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/util-dfm/01-openssl4-sm3.patch
Patch1:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/util-dfm/02-pc-remove-cmake-modules.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(mount)
BuildRequires:  pkgconfig(udisks2)
BuildRequires:  pkgconfig(libisoburn-1)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(liblucene++)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  boost-devel
BuildRequires:  lucene++-devel

%description
util-dfm provides the low-level DFM6 I/O, mount, burn and search libraries
used by dde-file-manager.

%package        io
Summary:        DFM6 I/O library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    io
This package contains the DFM6 I/O library.

%package        mount
Summary:        DFM6 mount library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    mount
This package contains the DFM6 mount library.

%package        burn
Summary:        DFM6 burn library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    burn
This package contains the DFM6 burn library and the dfm-burner tool.

%package        search
Summary:        DFM6 search library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    search
This package contains the DFM6 search library and the dfm-searcher tool.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-io%{?_isa} = %{version}-%{release}
Requires:       %{name}-mount%{?_isa} = %{version}-%{release}
Requires:       %{name}-burn%{?_isa} = %{version}-%{release}
Requires:       %{name}-search%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n util-dfm-%{version} -p1

%build
%cmake -GNinja -DOPT_ENABLE_QT6=ON -DBUILD_UNIT_TESTS=OFF
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md

%files io
%{_libdir}/libdfm6-io.so.1*

%files mount
%{_libdir}/libdfm6-mount.so.1*

%files burn
%{_libdir}/libdfm6-burn.so.1*
%{_bindir}/dfm-burner

%files search
%{_libdir}/libdfm6-search.so.1*
%{_bindir}/dfm-searcher
%{_datadir}/deepin/dfm-search/

%files devel
%{_includedir}/dfm6-io/
%{_includedir}/dfm6-mount/
%{_includedir}/dfm6-burn/
%{_includedir}/dfm6-search/
%{_libdir}/pkgconfig/dfm6-io.pc
%{_libdir}/pkgconfig/dfm6-mount.pc
%{_libdir}/pkgconfig/dfm6-burn.pc
%{_libdir}/pkgconfig/dfm6-search.pc
%{_libdir}/cmake/dfm6-io/
%{_libdir}/cmake/dfm6-mount/
%{_libdir}/cmake/dfm6-burn/
%{_libdir}/cmake/dfm6-search/
%{_libdir}/libdfm6-io.so
%{_libdir}/libdfm6-mount.so
%{_libdir}/libdfm6-burn.so
%{_libdir}/libdfm6-search.so

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.4.6-2
- Remove CMake-only Boostsystem/Threads names from dfm6-search.pc so the
  devel package has resolvable pkgconfig dependencies.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.4.6-1
- Initial Fedora package.
