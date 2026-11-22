%global debug_package %{nil}

%global repo seetaface-boxes
%global commit 2001378bec09761ba207e10ba4e9ccc5bb8eb9c1
%global shortcommit 2001378b

Name:           seetaface-boxes
Version:        6.0.0
Release:        0.1.20251122git%{shortcommit}%{?dist}
Summary:        SeetaFace face detector module
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
SeetaFace face detector module.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       seetaface-common
%description    devel
This package contains development files for %{name}.

%package -n     seetaface-common
Summary:        Common SeetaFace headers
BuildArch:      noarch

%description -n seetaface-common
This package contains the common SeetaFace headers shared by the
seetaface modules.

%files -n seetaface-common
%{_includedir}/seeta/Common/

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
%{_libdir}/libSeetaFaceDetector600.so

%files devel
%{_includedir}/seeta/CFaceDetector.h
%{_includedir}/seeta/CFaceInfo.h
%{_includedir}/seeta/FaceDetector.h
%{_includedir}/seeta/SeetaFaceDetectorConfig.h
%{_datadir}/cmake/FindSeetaFaceDetector.cmake
%exclude %{_includedir}/seeta/Common/


%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.0.0-0.1.20251122git2001378b
- Initial Fedora package (upstream commit 2001378bec09761ba207e10ba4e9ccc5bb8eb9c1).
