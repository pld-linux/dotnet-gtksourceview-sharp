Summary:	.NET language bindings for GtkSourceView
Summary(pl):	Wi±zania GtkSourceView dla .NET
Name:		dotnet-gtksourceview
Version:	0.2
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.go-mono.com/archive/gtksourceview-sharp-%{version}.tar.gz
# Source0-md5:	0eed28f53e016a53a911933c874c5f4a
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
BuildRequires:	dotnet-gtk-devel >= 0.91
BuildRequires:	gtksourceview-devel >= 1.0.1
BuildRequires:	libtool
BuildRequires:	monodoc >= 0.15
BuildRequires:	mono-csharp
BuildRequires:  mono-devel >= 0.91
Requires:	gtksourceview >= 0.1.0
Requires:	dotnet-gtk
Provides:	gtksourceview-sharp
Obsoletes:	gtksourceview-sharp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Gtk+2 and GNOME2 libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z Gtk+2 oraz
GNOME2.

%package devel
Summary:	Development part of GtkSourceView#
Summary(pl):	Czê¶æ GtkSourceView# przeznaczona dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	gtksourceview-sharp-devel
Obsoletes:	gtksourceview-sharp-devel

%description devel
Development part of GtkSourceView#.

%description devel -l pl
Czê¶æ GtkSourceView# przeznaczona dla programistów.

%prep
%setup -q -n gtksourceview-sharp-%{version}
sed -i -e 's/`monodoc --get-sourcesdir`/$(DESTDIR)&/' doc/Makefile.am
sed -i -e 's/apidir = $(DESTDIR)@gtk/apidir = @gtk/' gtksourceview/makefile.am

%build
rm -rf autom4te.cache
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT`monodoc --get-sourcesdir`

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
# already in main package
rm -f $RPM_BUILD_ROOT%{_datadir}/gtksourceview-1.0/language-specs/csharp.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/mono/gac/*
%{_datadir}/mime-info/*
%{_datadir}/gtksourceview-1.0/language-specs/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%{_libdir}/mono/gtk-sharp/*
%{_libdir}/monodoc/sources/*
%{_datadir}/gapi/*
%{_pkgconfigdir}/*
