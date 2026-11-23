Name:           dde-desktop-comps
Version:        6.2.1
Release:        1%{?dist}
Summary:        Group metadata for the Deepin Desktop Environment
License:        MIT
URL:            https://github.com/Fedora-DDE-Remix/Deepin-Desktop-Environment
Source0:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-desktop-comps/comps.xml
Source1:        https://raw.githubusercontent.com/Fedora-DDE-Remix/Deepin-Desktop-Environment/refs/heads/main/dde-desktop-comps/dde-desktop-comps.repo
BuildArch:      noarch
BuildRequires:  createrepo_c

%description
This package carries the comps group metadata for the Deepin Desktop
Environment.  It installs a small local DNF repository and enables it, so
that dde-desktop can be installed with dnf groupinstall even though the COPR
Pulp repository itself cannot publish comps metadata.

%prep
%setup -q -T -c -n %{name}-%{version}
cp %{SOURCE0} comps.xml

%build
mkdir -p repo
createrepo_c --groupfile "$PWD/comps.xml" repo

%install
install -d %{buildroot}%{_datadir}/dde-desktop/comps-repo
cp -a repo/repodata %{buildroot}%{_datadir}/dde-desktop/comps-repo/
install -Dm644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/dde-desktop-comps.repo

%files
%{_datadir}/dde-desktop/comps-repo/
%config(noreplace) %{_sysconfdir}/yum.repos.d/dde-desktop-comps.repo

%changelog
* Mon Nov 23 2026 mozixun <mozixun@fedoraproject.org> - 6.2.1-1
- Initial comps metadata carrier for dde-desktop.
