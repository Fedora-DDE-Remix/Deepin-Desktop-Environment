# DDE Desktop comps group

`dde-desktop` is a Fedora comps group, not an RPM package.  It installs the
complete DDE Wayland desktop from the
`Fedora-DDE-Remix/Deepin-Desktop-Environment` COPR repository.

The group includes:

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

## Install

```bash
sudo dnf copr enable mozixun/Fedora-DDE-Remix
sudo dnf groupinstall dde-desktop
```

The group has no versioned `packagereq` entries, so `dde-shell`,
`dde-tray-loader` and the other components can be updated independently.

## Publish the group metadata

COPR stores comps per chroot:

```bash
copr-cli edit-chroot mozixun/Fedora-DDE-Remix/fedora-45-x86_64 \
  --upload-comps comps.xml
```

Repeat for `fedora-45-aarch64` and the rawhide chroots if needed.

Each component package installs and enables its own systemd service.  Select
the `DDE` Wayland session at the DDM login screen.
