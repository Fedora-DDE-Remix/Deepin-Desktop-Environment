Name:           deepin-sound-theme
Version:        15.10.6
Release:        1%{?dist}
Summary:        Deepin sound theme

License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-sound-theme
Source0:        %{url}/archive/%{version}/deepin-sound-theme-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make

%description
Deepin sound theme provides the login, logout, notification and system
event sounds used by the DDE desktop.

%prep
%autosetup -n deepin-sound-theme-%{version} -p1

%build
# Data-only sound package.

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_datadir}/sounds/deepin/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 15.10.6-1
- Initial Fedora package.
