%global debug_package %{nil}

%global repo seetaface-models
%global commit a0c3132cfaa42926d16b7960b44f852f1c17a3b4

Name:           seetaface-models
Version:        1.0.0
Release:        0.1.20251122git%{expand:%(echo %{commit} | cut -c1-8)}%{?dist}
Summary:        SeetaFace model data used by deepin-face
License:        BSD-3-Clause
URL:            https://github.com/linuxdeepin/%{repo}
Source0:        %{url}/archive/%{commit}/%{repo}-%{commit}.tar.gz
BuildArch:      noarch

%description
SeetaFace model data used by the Deepin face recognition service.

%prep
%autosetup -n %{repo}-%{commit} -p1

%build
# Data-only package.

%install
install -d %{buildroot}%{_datadir}/seetaface-models
cp -a files/*.csta %{buildroot}%{_datadir}/seetaface-models/

%files
%{_datadir}/seetaface-models/*.csta

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-0.1.20251122git%{expand:%(echo %{commit} | cut -c1-8)}
- Initial Fedora package.
