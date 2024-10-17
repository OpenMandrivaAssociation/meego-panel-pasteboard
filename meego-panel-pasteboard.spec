Name: meego-panel-pasteboard
Summary: Pasteboard panel for MeeGo
Group: Graphical desktop/Other 
Version: 0.0.8
License: LGPL 2.1
URL: https://www.meego.com
Release: %mkrel 1
Source0: http://repo.meego.com/MeeGo/releases/1.1/netbook/repos/source//%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: clutter-devel
BuildRequires: gtk2-devel
BuildRequires: nbtk-devel
BuildRequires: libmeego-panel-devel
BuildRequires: intltool
BuildRequires: gettext
BuildRequires: gnome-common
Obsoletes: moblin-panel-pasteboard <= 0.0.3

%description
MeeGo pasteboard panel

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README NEWS AUTHORS ChangeLog
%{_libexecdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/dbus-1/services/*service
%{_datadir}/mutter-meego/*

