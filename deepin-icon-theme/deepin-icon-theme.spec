Name:           deepin-icon-theme
Version:        2026.02.28
Release:        1%{?dist}
Summary:        Deepin icon themes

License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-icon-theme
Source0:        %{url}/archive/%{version}/deepin-icon-theme-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-icon-theme/01-hicolor-destdir.patch
BuildArch:      noarch

BuildRequires:  make

Requires:       hicolor-icon-theme

%description
Deepin icon themes provide the Bloom, Bloom Dark, Bloom Classic, Vintage
and hicolor icon sets used by the DDE desktop.

%prep
%autosetup -n deepin-icon-theme-%{version} -p1

%build
# Data-only icon package.

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/bloom/
%{_datadir}/icons/bloom-dark/
%{_datadir}/icons/bloom-classic/
%{_datadir}/icons/bloom-classic-dark/
%{_datadir}/icons/vintage/
%{_datadir}/icons/hicolor/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 2026.02.28-1
- Initial Fedora package.
