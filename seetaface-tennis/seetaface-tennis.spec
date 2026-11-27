%global debug_package %{nil}

%global repo seetaface-tennis
%global commit c478b19bbd572bc0c2ff61232aa1c3fc935c62c4
%global shortcommit c478b19b

Name:           seetaface-tennis
Version:        1.0.2
Release:        0.2.20251122git%{shortcommit}%{?dist}
Summary:        TenniS tensor library for SeetaFace
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{commit}/%{repo}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  seetaface-open-role-zoo-devel
%description
TenniS tensor library for SeetaFace.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for %{name}.


%prep
%autosetup -n %{repo}-%{commit} -p1

%build
%cmake -GNinja -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DCMAKE_BUILD_TYPE=Release -DPLATFORM=x64 -DCONFIGURATION=Release \
  -DSEETA_INSTALL_PATH=%{_prefix} -DSEETA_AUTHORIZE=ON -DSEETA_MODEL_ENCRYPT=ON \
  -DORZ_ROOT_DIR=%{_prefix} -DCMAKE_MODULE_PATH=%{_prefix}/cmake \
  -DCMAKE_CXX_FLAGS:STRING="%{build_cxxflags} -include cstdlib -include functional -include memory" \
  -DTS_USE_OPENCV=OFF -DTS_BUILD_TEST=OFF -DTS_BUILD_TOOLS=OFF
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
%{_libdir}/libtennis.so

%files devel
%{_includedir}/api/
%{_datadir}/cmake/FindTenniS.cmake
%{_datadir}/cmake/TenniSConfig.cmake
%exclude %{_includedir}/seeta/Common/


%changelog
* Fri Nov 27 2026 Fedora DDE Remix <fedora-dde-remix@users.noreply.github.com> - 1.0.2-0.2.20251122gitc478b19b
- Preserve Fedora C++ build flags and required standard-library includes.

* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.2-0.1.20251122gitc478b19b
- Initial Fedora package (upstream commit c478b19bbd572bc0c2ff61232aa1c3fc935c62c4).
