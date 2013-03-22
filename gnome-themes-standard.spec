Summary:	Default themes for GNOME environment
Summary(pl.UTF-8):	Domyślne motywy dla środowiska GNOME
Name:		gnome-themes-standard
Version:	3.6.5
Release:	2
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-standard/3.6/%{name}-%{version}.tar.xz
# Source0-md5:	0053b0680fe8961d4ebc88ede71aca6e
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.24.15
BuildRequires:	gtk+3-devel >= 3.6.2
BuildRequires:	intltool >= 0.40
BuildRequires:	librsvg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post):	gtk-update-icon-cache
Requires:	gnome-icon-theme >= 3.4.0
Suggests:	gtk2-theme-engine-adwaita
Obsoletes:	gnome-themes-HighContrast < 3.0-1
Obsoletes:	gnome-themes-HighContrastLargePrint < 3.0-1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME environment.

%description -l pl.UTF-8
Domyślne motywy dla środowiska GNOME.

%package -n gtk2-theme-engine-adwaita
Summary:	Adwaita gtk2 theme
Group:		Themes/GTK+

%description -n gtk2-theme-engine-adwaita
This package contains a gtk2 theme for presenting widgets with a GNOME
look and feel.

%prep
%setup -q

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.0.0/theming-engines/libadwaita.la

# gtk+2 cache
touch $RPM_BUILD_ROOT%{_iconsdir}/HighContrast/icon-theme.cache

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache HighContrast

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/3.0.0/theming-engines/libadwaita.so
%{_datadir}/themes/Adwaita
%exclude %{_datadir}/themes/Adwaita/gtk-2.0
%{_datadir}/themes/HighContrast
%exclude %{_datadir}/themes/HighContrast/gtk-2.0
%dir %{_iconsdir}/Adwaita
%{_iconsdir}/Adwaita/cursors
%dir %{_iconsdir}/HighContrast
%{_iconsdir}/HighContrast/*x*
%{_iconsdir}/HighContrast/scalable
%ghost %{_iconsdir}/HighContrast/icon-theme.cache

%files -n gtk2-theme-engine-adwaita
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-2.0/2.10.0/engines/libadwaita.so
%{_datadir}/themes/Adwaita/gtk-2.0
%{_datadir}/themes/HighContrast/gtk-2.0
%{_datadir}/gnome-background-properties/adwaita.xml

# XXX: package here, not to pull libgnome deps
%dir %{_datadir}/gnome-background-properties
