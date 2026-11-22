Name:           deepin-gtk-theme
Version:        25.3.7
Release:        1%{?dist}
Summary:        Deepin GTK themes

License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-gtk-theme
Source0:        %{url}/archive/%{version}/deepin-gtk-theme-%{version}.tar.gz
Patch0:         https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/deepin-gtk-theme/01-fsf-address.patch
BuildArch:      noarch

BuildRequires:  make

Requires:       deepin-icon-theme

%description
Deepin GTK themes provide the light and dark GTK theme used by Deepin
applications and GTK applications on the DDE desktop.

%prep
%autosetup -n deepin-gtk-theme-%{version} -p1

%build
# Data-only theme package.

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_datadir}/themes/deepin/
%{_datadir}/themes/deepin-dark/

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 25.3.7-1
- Initial Fedora package.
