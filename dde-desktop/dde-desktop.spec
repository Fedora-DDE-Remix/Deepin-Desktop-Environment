%global debug_package %{nil}

Name:           dde-desktop
Version:        1.0.0
Release:        1%{?dist}
Summary:        Complete DDE desktop environment

License:        MIT
URL:            https://github.com/Fedora-DDE-Remix/Deepin-Desktop-Environment
Source0:        README.md
Source1:        90-dde-desktop.preset
Source2:        LICENSE
BuildArch:      noarch

BuildRequires:  systemd-rpm-macros

Requires:       NetworkManager
Requires:       accountsservice
Requires:       dde-account-faces
Requires:       dde-api
Requires:       dde-app-services
Requires:       dde-appearance
Requires:       dde-application-manager
Requires:       dde-clipboard
Requires:       dde-control-center
Requires:       dde-daemon
Requires:       dde-file-manager
Requires:       dde-file-manager-desktop
Requires:       dde-file-manager-services-plugins
Requires:       dde-launchpad
Requires:       dde-polkit-agent
Requires:       dde-seatd
Requires:       dde-services
Requires:       dde-session
Requires:       dde-shell
Requires:       dde-tray-loader
Requires:       ddm
Requires:       deepin-compressor
Requires:       deepin-draw
Requires:       deepin-editor
Requires:       deepin-fcitx5configtool-plugin
Requires:       deepin-font-manager
Requires:       deepin-image-viewer
Requires:       deepin-qt6integration
Requires:       deepin-reader
Requires:       deepin-scanner
Requires:       deepin-system-monitor
Requires:       deepin-terminal
Requires:       deepin-voice-note
Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
Requires:       deepin-default-settings
Requires:       deepin-service-manager
Requires:       deepin-wayland-protocols
Requires:       dde-calendar
Requires:       fcitx5
Requires:       gio-qt
Requires:       gnome-logs
Requires:       gsettings-qt6
Requires:       mediawriter
Requires:       pipewire
Requires:       pipewire-pulseaudio
Requires:       polkit
Requires:       treeland
Requires:       treeland-protocols
Requires:       udisks2
Requires:       udisks2-qt6
Requires:       upower
Requires:       util-dfm
Requires:       vlc
Requires:       wireplumber
Requires:       xdg-desktop-portal
Requires:       xdg-desktop-portal-gtk
Requires:       xdg-user-dirs

Recommends:     deepin-desktop-theme
Recommends:     deepin-icon-theme
Recommends:     deepin-manual
Recommends:     deepin-wallpapers
Recommends:     fcitx5-chinese-addons

Suggests:       deepin-deepinid-client
Suggests:       deepin-face

%description
dde-desktop is a meta package that installs a complete DDE Wayland desktop:
the DDE compositor, DDM, dde-session, dde-shell, the DDE daemons and
services, the control center, file manager, launcher and the standard
Deepin applications.

Music playback is provided by VLC, log viewing by GNOME Logs, and USB image
writing by Fedora Media Writer.  A systemd preset enables DDM, the DDE seat
manager and the DDE system services.

%prep
%setup -q -T -c
cp %{SOURCE0} README.md
cp %{SOURCE2} LICENSE

%build
# Meta package: no build step.

%install
install -Dm644 %{SOURCE1} %{buildroot}%{_presetdir}/90-dde-desktop.preset

%post
%systemd_post ddm.service dde-seatd.service dde-system-daemon.service dde-dconfig-daemon.service deepin-service-manager.service

%files
%license LICENSE
%doc README.md
%{_presetdir}/90-dde-desktop.preset

%changelog
* Sun Nov 22 2026 mozixun <mozixun@fedoraproject.org> - 1.0.0-1
- Initial Fedora meta package.
