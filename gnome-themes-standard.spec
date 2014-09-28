Summary:	Default themes for GNOME environment
Summary(pl.UTF-8):	Domyślne motywy dla środowiska GNOME
Name:		gnome-themes-standard
Version:	3.14.0
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-standard/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	fe121e92298b527f6f614050bddd866a
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	cairo-devel
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.24.15
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.40
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post):	gtk-update-icon-cache
Requires:	adwaita-icon-theme
Requires:	gtk+3 >= 3.14.0
Suggests:	gtk2-theme-engine-adwaita
Obsoletes:	gnome-themes-HighContrast < 3.0-1
Obsoletes:	gnome-themes-HighContrastLargePrint < 3.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME environment.

%description -l pl.UTF-8
Domyślne motywy dla środowiska GNOME.

%package -n gtk2-theme-engine-adwaita
Summary:	Adwaita GTK+ 2 theme
Summary(pl.UTF-8):	Motyw Adwaita dla GTK+ 2
Group:		Themes/GTK+
Requires:	gtk+2 >= 2:2.24.15

%description -n gtk2-theme-engine-adwaita
This package contains a GTK+ 2 theme for presenting widgets with a
GNOME look and feel.

%description -n gtk2-theme-engine-adwaita -l pl.UTF-8
Ten pakiet zawiera motyw GTK+ 2 do prezentowania widgetów z wyglądem
i zachowaniem GNOME.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.la

# gtk+2 cache
touch $RPM_BUILD_ROOT%{_iconsdir}/HighContrast/icon-theme.cache

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache HighContrast

%files
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Adwaita
%{_datadir}/themes/Adwaita/gtk-3.0
%{_datadir}/themes/Adwaita/metacity-1
%{_datadir}/themes/Adwaita/index.theme
%dir %{_datadir}/themes/HighContrast
%{_datadir}/themes/HighContrast/gtk-3.0
%{_datadir}/themes/HighContrast/metacity-1
%{_datadir}/themes/HighContrast/index.theme
%dir %{_iconsdir}/HighContrast
%{_iconsdir}/HighContrast/*x*
%{_iconsdir}/HighContrast/scalable
%ghost %{_iconsdir}/HighContrast/icon-theme.cache

%files -n gtk2-theme-engine-adwaita
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.so
%{_datadir}/themes/Adwaita/gtk-2.0
%{_datadir}/themes/HighContrast/gtk-2.0
