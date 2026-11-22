Name:           dde-account-faces
Version:        1.0.19
Release:        1%{?dist}
Summary:        Default account avatar images for DDE
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-account-faces
Source0:        %{url}/archive/%{version}/dde-account-faces-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make

Requires:       accountsservice

%description
dde-account-faces provides the default user avatar images used by
AccountsService and the DDE account settings.

%prep
%autosetup -n dde-account-faces-%{version} -p1

%build
%make_build

%install
%make_install PREFIX=%{_var}

%files
%license LICENSE
%doc README.md
%{_var}/lib/AccountsService/icons/

%changelog
* Sat Nov 21 2026 mozixun <mozixun@fedoraproject.org> - 1.0.19-1
- Initial Fedora package.
