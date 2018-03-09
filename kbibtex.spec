%define major 0.7
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		kbibtex
Version:	0.7
Release:	1
Summary:	A BibTeX editor for KDE
Group:		Editors
License:	GPLv2+
URL:		http://home.gna.org/kbibtex/
Source0:	http://download.kde.org/stable/KBibTeX/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(poppler-qt4)

%description
KBibTeX is a BibTeX editor for KDE.

%package -n %{develname}
Summary:  Development files for KBibTeX
Group:    Development/KDE and Qt
Requires: %{libname} = %{version}

%description -n %{develname}
Development files for KBibTeX.

%package -n %{libname}
Summary:  Library files for KBibTeX
Group:    System/Libraries

%description -n %{libname}
Library files for KBibTeX.

%prep
%setup -q

%build
export CC=gcc
export CXX=g++
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %name --with-html

%files -f %{name}.lang
%doc README
%{_kde_bindir}/%{name}
%{_kde_libdir}/kde4/kbibtexpart.so
%{_kde_appsdir}/%{name}*
%{_kde_configdir}/kbibtexrc
%{_kde_datadir}/mime/packages/*.xml
%{_kde_services}/*.desktop
%{_kde_applicationsdir}/*.desktop
%{_kde_datadir}/appdata/%{name}.appdata.xml
%{_kde_iconsdir}/*/*/*/*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_includedir}/kbibtex
%{_kde_libdir}/*.so
