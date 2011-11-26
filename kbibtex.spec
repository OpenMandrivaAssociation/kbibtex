Name: kbibtex
Version: 0.4
Release: 1
Summary: A BibTeX editor for KDE 
Group: Editors
License: GPLv2+
URL: http://home.gna.org/kbibtex/
Source0: http://download.gna.org/kbibtex/%{version}/%{name}-%{version}.tar.bz2
BuildRequires: kdelibs4-devel
BuildRequires: libpoppler-qt4-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel

%description
KBibTeX is a BibTeX editor for KDE

%prep
%setup -qn %{name}-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-) 
%doc README
%{_kde_bindir}/*
%{_kde_libdir}/*.so
%{_kde_libdir}/kde4/*.so
%{_kde_appsdir}/%{name}*
%{_kde_datadir}/mime/packages/*.xml
%{_kde_services}/*.desktop
%{_kde_applicationsdir}/*.desktop
%{_kde_iconsdir}/*/*/*/*
%{_kde_mandir}/man1/*
