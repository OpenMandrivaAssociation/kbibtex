Name: kbibtex
Version: 0.3
Release: 0.beta2.1
Summary: A BibTeX editor for KDE 
Group: Editors
License: GPLv2+
URL: http://home.gna.org/kbibtex/
Source0: http://download.gna.org/kbibtex/0.3/%{name}-%{version}-beta2.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: kdelibs4-devel
BuildRequires: libpoppler-qt4-devel
BuildRequires: libxml2-devel
BuildRequires: libxslt-devel

%description
KBibTeX is a BibTeX editor for KDE

%prep
%setup -qn %{name}-%{version}-beta2

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
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
