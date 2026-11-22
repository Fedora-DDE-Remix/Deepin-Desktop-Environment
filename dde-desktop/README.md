# DDE Desktop meta package

`dde-desktop` installs the complete DDE Wayland desktop environment from the
`Fedora-DDE-Remix/Deepin-Desktop-Environment` COPR repository.

It pulls in:

- Treeland, DDM, the DDE session manager and dde-shell;
- dde-daemon, dde-api, dde-application-manager, dde-tray-loader and the
  DDE services;
- the Deepin control center, file manager, launcher, clipboard, appearance
  and polkit agent;
- the Deepin terminal, editor, archive manager, image viewer, drawing tool,
  document viewer, scanner, calendar, system monitor, voice notes and font
  manager;
- Fedora desktop base services (NetworkManager, PipeWire, WirePlumber,
  udisks2, UPower, AccountsService and XDG portals).

The following Deepin applications are intentionally replaced by Fedora
components:

| Deepin component | Replacement |
|---|---|
| Deepin Music | VLC |
| Deepin Log Viewer | GNOME Logs |
| Deepin Boot Maker | Fedora Media Writer |

The package also installs a systemd preset that enables DDM, the DDE seat
daemon and the DDE system services.  Select the `DDE` Wayland session at the
DDM login screen.

Deepin theme/icon/wallpaper packages are not part of the current COPR spec
set; the desktop falls back to the icon theme shipped by Fedora.  They can
be added later without changing this meta package.
