%global debug_package %{nil}

%global repo seetaface-quality-assessor
%global commit 4ea33f03e9dac73a21502f1f69fcb0c0f0dd7ce0
%global shortcommit 4ea33f03

Name:           seetaface-quality-assessor
Version:        3.0.0
Release:        0.3.20251122git%{shortcommit}%{?dist}
Summary:        SeetaFace image quality assessment module
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{commit}/%{repo}-%{commit}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/seetaface-quality-assessor/01-install-prefix.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  seetaface-open-role-zoo-devel
BuildRequires:  seetaface-tennis-devel
BuildRequires:  seetaface-authorize-devel
BuildRequires:  seetaface-pose-estimation-devel
%description
SeetaFace image quality assessment module.

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
%{_libdir}/libSeetaQualityAssessor300.so

%files devel
%{_includedir}/seeta/CStruct.h
%{_includedir}/seeta/Struct.h
%{_includedir}/seeta/QualityAssessor.h
%{_includedir}/seeta/QualityOfBrightness.h
%{_includedir}/seeta/QualityOfClarity.h
%{_includedir}/seeta/QualityOfIntegrity.h
%{_includedir}/seeta/QualityOfLBN.h
%{_includedir}/seeta/QualityOfPose.h
%{_includedir}/seeta/QualityOfPoseEx.h
%{_includedir}/seeta/QualityOfResolution.h
%{_includedir}/seeta/QualityStructure.h
%exclude %{_includedir}/seeta/Common/


%changelog
* Fri Nov 27 2026 Fedora DDE Remix <fedora-dde-remix@users.noreply.github.com> - 3.0.0-0.3.20251122git4ea33f03
- Preserve Fedora C++ build flags and required standard-library includes.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 3.0.0-0.2.20251122git4ea33f03
- Point CMAKE_MODULE_PATH at /usr/share/cmake where the SeetaFace
  development packages install their Find modules.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 3.0.0-0.1.20251122git4ea33f03
- Initial Fedora package (upstream commit 4ea33f03e9dac73a21502f1f69fcb0c0f0dd7ce0).
