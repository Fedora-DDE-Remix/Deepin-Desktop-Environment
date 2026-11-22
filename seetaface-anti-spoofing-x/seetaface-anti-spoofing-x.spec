%global debug_package %{nil}

%global repo seetaface-anti-spoofing-x
%global commit bdfefc9b05d6a49f17957b5aeef4919975265722
%global shortcommit bdfefc9b

Name:           seetaface-anti-spoofing-x
Version:        6.0.0
Release:        0.2.20251122git%{shortcommit}%{?dist}
Summary:        SeetaFace anti-spoofing module
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{commit}/%{repo}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  seetaface-open-role-zoo-devel
BuildRequires:  seetaface-tennis-devel
BuildRequires:  seetaface-authorize-devel
%description
SeetaFace anti-spoofing module.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       seetaface-common
%description    devel
This package contains development files for %{name}.


%prep
%autosetup -n %{repo}-%{commit} -p1

%build
%cmake -GNinja -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DCMAKE_BUILD_TYPE=Release -DPLATFORM=x64 -DCONFIGURATION=Release \
  -DSEETA_INSTALL_PATH=%{_prefix} -DSEETA_AUTHORIZE=ON -DSEETA_MODEL_ENCRYPT=ON \
  -DORZ_ROOT_DIR=%{_prefix} -DCMAKE_MODULE_PATH=%{_datadir}/cmake \
  -DCMAKE_CXX_FLAGS="-include cstdlib -include functional -include memory"
%cmake_build

%install
%cmake_install
if [ -d %{buildroot}%{_prefix}/cmake ]; then
  mkdir -p %{buildroot}%{_datadir}/cmake
  mv %{buildroot}%{_prefix}/cmake/* %{buildroot}%{_datadir}/cmake/
  rmdir %{buildroot}%{_prefix}/cmake
fi

%files
%license LICENSE
%doc README.md
%{_libdir}/libSeetaFaceAntiSpoofingX600.so

%files devel
%{_includedir}/seeta/FaceAntiSpoofing.h
%exclude %{_includedir}/seeta/Common/


%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.0.0-0.2.20251122gitbdfefc9b
- Point CMAKE_MODULE_PATH at /usr/share/cmake for the SeetaFace Find modules.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.0.0-0.1.20251122gitbdfefc9b
- Initial Fedora package (upstream commit bdfefc9b05d6a49f17957b5aeef4919975265722).
