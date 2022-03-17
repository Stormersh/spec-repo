Summary:         An IPTV streaming application
Name:            hypnotix
Version:         2.6
Release:         2%{?dist}
License:         GPL3
URL:             https://github.com/linuxmint/hypnotix
Source0:         https://github.com/linuxmint/hypnotix/archive/refs/tags/%{version}.tar.gz

BuildRequires:	 make
BuildRequires:	 gettext

Requires:        gtk3
Requires:        python3-setproctitle
Requires:        python3-xapps-overrides
Requires:	 python3-cairo
Requires:	 python3-requests
Requires:	 python3-setproctitle
Requires:	 python3-gobject
Requires:	 python3-unidecode
Requires:	 python3-imdbpy
Requires:	 python-unversioned-command
Requires:	 mpv-libs



%description
An IPTV streaming application

# disable debuginfo, which is useless on binary-only packages
%define debug_package %{nil}

%prep
%setup -q -n %{name}-%{version}

%build
sed -i "s/__DEB_VERSION__/%{version}/g" usr/lib/hypnotix/hypnotix.py
sed -i '2d' usr/bin/hypnotix
sh -c "echo 'GDK_BACKEND=x11 /usr/lib/hypnotix/hypnotix.py'" >> usr/bin/hypnotix
sed -i '1396a \        options["vo"] = "x11"' usr/lib/hypnotix/hypnotix.py
make

%install
install -D     -t %{buildroot}/usr/bin usr/bin/hypnotix
install -D     -t %{buildroot}/usr/lib/hypnotix usr/lib/hypnotix/{common,hypnotix}.py
install -Dm644 -t %{buildroot}/usr/lib/hypnotix usr/lib/hypnotix/mpv.py
install -Dm644 -t %{buildroot}/usr/share/applications usr/share/applications/hypnotix.desktop
install -Dm644 -t %{buildroot}/usr/share/glib-2.0/schemas usr/share/glib-2.0/schemas/org.x.hypnotix.gschema.xml
install -Dm644 -t %{buildroot}/usr/share/hypnotix usr/share/hypnotix/*.{css,png,ui}
install -Dm644 -t %{buildroot}/usr/share/hypnotix/pictures usr/share/hypnotix/pictures/*.svg
install -Dm644 -t %{buildroot}/usr/share/hypnotix/pictures/badges usr/share/hypnotix/pictures/badges/*
install -Dm644 -t %{buildroot}/usr/share/icons/hicolor/scalable/apps usr/share/icons/hicolor/scalable/apps/hypnotix.svg

cp -a usr/share/locale %{buildroot}/usr/share/locale


%files
/usr/bin/hypnotix
/usr/lib/hypnotix/{common,hypnotix}.py
/usr/lib/hypnotix/mpv.py
/usr/share/applications/hypnotix.desktop
/usr/share/glib-2.0/schemas/org.x.hypnotix.gschema.xml
/usr/share/hypnotix/*.{css,png,ui}
/usr/share/hypnotix/pictures/*.svg
/usr/share/locale/*/LC_MESSAGES/hypnotix.mo
/usr/share/hypnotix/pictures/badges/*
/usr/share/icons/hicolor/scalable/apps/hypnotix.svg
