%define _snap 20040228
Summary:	.NET language bindings for GtkSourceView
Summary(pl):	Wi±zania GtkSourceView dla .NET
Name:		gtksourceview-sharp
Version:	0.1.0
Release:	0.%{_snap}
License:	LGPL
Group:		Development/Libraries
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	89860497088518bd92c0966912e8c9e4
BuildRequires:	autoconf
BuildRequires:	automake >= 1.7
BuildRequires:	gtk-sharp-devel >= 0.17
BuildRequires:	gtksourceview-devel >= 0.7.0
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:  mono-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to Gtk+2 and GNOME2 libraries.

%description -l pl
Pakiet ten dostarcza wi±zania dla .NET do bibliotek z Gtk+2 oraz
GNOME2.

%package devel
Summary:	Development part of GtkSourceView#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development part of GtkSourceView#.

%prep
%setup -q -n %{name}-%{_snap}

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/*.dll
%{_datadir}/gtksourceview*/language-specs/*
%{_datadir}/mime-info/*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS
%{_datadir}/gapi/*
%{_pkgconfigdir}/*
