Name:           deepin-pdfium
Version:        1.5.8
Release:        2%{?dist}
Summary:        PDF rendering library based on PDFium
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-pdfium
Source0:        %{url}/archive/%{version}/deepin-pdfium-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-pdfium/01-backport-reader-api.patch

Provides:       bundled(pdfium)

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  pkgconfig(chardet)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libjpeg)

%description
deepin-pdfium is a PDF rendering library based on the bundled PDFium engine,
used by the DDE file manager and document applications.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n deepin-pdfium-%{version} -p1

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdeepin-pdfium.so.1*

%files devel
%{_includedir}/deepin-pdfium/
%{_libdir}/libdeepin-pdfium.so
%{_libdir}/pkgconfig/deepin-pdfium.pc
%{_libdir}/cmake/deepin-pdfium/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.5.8-2
- Backport fileIdentifier() and imageObjectRects() for deepin-reader 6.6.

* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.5.8-1
- Initial Fedora package.
