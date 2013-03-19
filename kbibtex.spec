# Keep libraries private
%if %{_use_internal_dependency_generator}
%define __noautoprov 'kbibtexpart\\.so(.*)|libkbibtexgui.so(.*)|libkbibtexio.so(.*)|libkbibtexproc.so(.*)|libkbibtexws.so'
%define __noautoreq 'kbibtexpart\\.so(.*)|libkbibtexgui.so(.*)|libkbibtexio.so(.*)|libkbibtexproc.so(.*)|libkbibtexws.so'
%endif

Name:		kbibtex
Version:	0.4.1
Release:	1
Summary:	A BibTeX editor for KDE
Group:		Editors
License:	GPLv2+
URL:		http://home.gna.org/kbibtex/
Source0:	http://download.gna.org/kbibtex/0.4/%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(poppler-qt4)

%description
KBibTeX is a BibTeX editor for KDE.

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%files
%doc README
%{_kde_bindir}/%{name}
%{_kde_libdir}/libkbibtexgui.so
%{_kde_libdir}/libkbibtexio.so
%{_kde_libdir}/libkbibtexproc.so
%{_kde_libdir}/libkbibtexws.so
%{_kde_libdir}/kde4/kbibtexpart.so
%{_kde_appsdir}/%{name}*
%{_kde_configdir}/kbibtexrc
%{_kde_datadir}/mime/packages/*.xml
%{_kde_services}/*.desktop
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_mandir}/man1/*

