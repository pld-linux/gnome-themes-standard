Summary:	Default themes for GNOME environment
Summary(pl.UTF-8):	Domyślne motywy dla środowiska GNOME
Name:		gnome-themes-standard
Version:	2.91.91
Release:	1
License:	LGPL
Group:		Themes
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-themes-standard/2.91/%{name}-%{version}.tar.bz2
# Source0-md5:	dbe0c2eae1cf2cc710cd4bed511df7a6
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.36.1
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,postun):	gtk-update-icon-cache
Requires:	gnome-icon-theme >= 2.91.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default themes for GNOME environment.

%description -l pl.UTF-8
Domyślne motywy dla środowiska GNOME.

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
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-3.0/3.0.0/theming-engines/libadwaita.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache Adwaita
%update_icon_cache HighContrast
%update_icon_cache HighContrastInverse
%update_icon_cache LowContrast

%postun
%update_icon_cache Adwaita
%update_icon_cache HighContrast
%update_icon_cache HighContrastInverse
%update_icon_cache LowContrast

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-3.0/3.0.0/theming-engines/libadwaita.so
%{_datadir}/themes/Adwaita
%{_datadir}/themes/HighContrast
%{_datadir}/themes/HighContrastInverse
%{_datadir}/themes/LowContrast
%{_datadir}/gnome-background-properties/adwaita.xml
%{_iconsdir}/Adwaita
%{_iconsdir}/HighContrast
%{_iconsdir}/HighContrastInverse
%{_iconsdir}/LowContrast
