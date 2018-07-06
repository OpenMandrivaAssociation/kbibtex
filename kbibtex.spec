%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		kbibtex
Version:	0.8.1
Release:	1
Summary:	A BibTeX editor for KDE
Group:		Editors
License:	GPLv2+
URL:		http://home.gna.org/kbibtex/
Source0:	http://download.kde.org/stable/KBibTeX/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(poppler-qt5)
BuildRequires: cmake(ECM)

BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Quick)
BuildRequires: cmake(Qt5WebChannel)
BuildRequires: cmake(Qt5WebEngineCore)
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5WebKitWidgets)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5XmlPatterns)
BuildRequires: cmake(Qt5)
BuildRequires: cmake(Qt5Test)

BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Parts)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Service)
BuildRequires: cmake(KF5Wallet)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5)

BuildRequires: cmake(Qca-qt5)

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
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %name --with-html --with-man

%files -f %{name}.lang
%doc README
%{_bindir}/%{name}
%{_libdir}/qt5/plugins/kbibtexpart.so
%{_datadir}/%{name}
%{_datadir}/kxmlgui5/%{name}*/*.rc
%{_sysconfdir}/xdg/kbibtexrc
%{_datadir}/mime/packages/*.xml
%{_datadir}/kservices5/*.desktop
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_iconsdir}/*/*/*/*
%{_mandir}/man1/%{name}.*

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_libdir}/*.so
