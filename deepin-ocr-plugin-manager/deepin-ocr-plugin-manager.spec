Name:           deepin-ocr-plugin-manager
Version:        1.0.1
Release:        1%{?dist}
Summary:        OCR plugin manager for the Deepin desktop environment

License:        LGPL-2.1-or-later
URL:            https://github.com/linuxdeepin/deepin-ocr-plugin-manager
Source0:        %{url}/archive/%{version}/deepin-ocr-plugin-manager-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-ocr-plugin-manager/01-fedora-deps.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(ncnn)
BuildRequires:  pkgconfig(opencv4)
BuildRequires:  pkgconfig

%description
deepin-ocr-plugin-manager provides the PaddleOCR-based recognition engine
and plugin interface used by Deepin applications such as the image viewer.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ncnn-devel
Requires:       opencv-devel

%description    devel
This package contains development files for %{name}.

%prep
%autosetup -n deepin-ocr-plugin-manager-%{version} -p1

%build
%cmake -GNinja -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libdeepin-ocr-plugin-manager.so.1*
%{_datadir}/deepin-ocr-plugin-manager/

%files devel
%{_includedir}/deepin-ocr-plugin-manager/
%{_libdir}/libdeepin-ocr-plugin-manager.so
%{_libdir}/pkgconfig/deepin-ocr-plugin-manager.pc

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.1-1
- Initial Fedora package.
