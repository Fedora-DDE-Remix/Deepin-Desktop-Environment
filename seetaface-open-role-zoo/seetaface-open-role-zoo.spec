%global debug_package %{nil}

%global repo seetaface-open-role-zoo
%global commit 52fc4cafd73ebc54d743257852b84cf14a88b8e5
%global shortcommit 52fc4caf

Name:           seetaface-open-role-zoo
Version:        1.0.0
Release:        0.1.20251122git%{shortcommit}%{?dist}
Summary:        OpenRoleZoo utility library for SeetaFace
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{commit}/%{repo}-%{commit}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

%description
OpenRoleZoo utility library for SeetaFace.

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
  -DCMAKE_CXX_FLAGS="-include cstdlib -include functional -include memory" \
  -DORZ_INSTALL=ON
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
%{_bindir}/orz_resources

%files devel
%{_includedir}/orz/
%{_libdir}/libORZ_static.a
%exclude %{_includedir}/seeta/Common/


%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-0.1.20251122git52fc4caf
- Initial Fedora package (upstream commit 52fc4cafd73ebc54d743257852b84cf14a88b8e5).
