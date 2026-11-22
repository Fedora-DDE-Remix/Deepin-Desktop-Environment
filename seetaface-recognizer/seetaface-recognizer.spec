%global debug_package %{nil}

%global repo seetaface-recognizer
%global commit e24568052fd38b58ec8f2852138f9cbb4154edf4
%global shortcommit e2456805

Name:           seetaface-recognizer
Version:        6.1.0
Release:        0.1.20251122git%{shortcommit}%{?dist}
Summary:        SeetaFace face recognition module
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
SeetaFace face recognition module.

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
  -DORZ_ROOT_DIR=%{_prefix} -DCMAKE_MODULE_PATH=%{_prefix}/cmake \
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
%{_libdir}/libSeetaFaceRecognizer610.so

%files devel
%{_includedir}/seeta/CStream.h
%{_includedir}/seeta/FaceDatabase.h
%{_includedir}/seeta/FaceRecognizer.h
%{_includedir}/seeta/Stream.h
%{_includedir}/seeta/SeetaFaceRecognizerConfig.h
%{_datadir}/cmake/FindSeetaFaceRecognizer.cmake
%exclude %{_includedir}/seeta/Common/


%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.1.0-0.1.20251122gite2456805
- Initial Fedora package (upstream commit e24568052fd38b58ec8f2852138f9cbb4154edf4).
