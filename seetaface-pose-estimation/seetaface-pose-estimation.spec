%global debug_package %{nil}

%global repo seetaface-pose-estimation
%global commit 11f3645bbb29ab75d158fd588d579989f14b1d28
%global shortcommit 11f3645b

Name:           seetaface-pose-estimation
Version:        6.0.0
Release:        0.3.20251122git%{shortcommit}%{?dist}
Summary:        SeetaFace pose estimation module
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
SeetaFace pose estimation module.

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
  -DCMAKE_CXX_FLAGS:STRING="%{build_cxxflags} -include cstdlib -include functional -include memory"
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
%{_libdir}/libSeetaPoseEstimation600.so

%files devel
%{_includedir}/seeta/PoseEstimator.h
%{_datadir}/cmake/FindSeetaPoseEstimation.cmake
%exclude %{_includedir}/seeta/Common/


%changelog
* Fri Nov 27 2026 Fedora DDE Remix <fedora-dde-remix@users.noreply.github.com> - 6.0.0-0.3.20251122git11f3645b
- Preserve Fedora C++ build flags and required standard-library includes.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.0.0-0.2.20251122git11f3645b
- Point CMAKE_MODULE_PATH at /usr/share/cmake for the SeetaFace Find modules.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 6.0.0-0.1.20251122git11f3645b
- Initial Fedora package (upstream commit 11f3645bbb29ab75d158fd588d579989f14b1d28).
