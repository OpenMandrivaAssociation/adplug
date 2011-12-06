%define name adplug
%define version 2.2
%define release %mkrel 3
%define api 2.2
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
%define staticname %mklibname -s -d %name

Summary: AdLib sound player library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/%name/%{name}-%{version}.tar.bz2
Source1: http://prdownloads.sourceforge.net/adplug/adplug.db.bz2
URL: http://adplug.sourceforge.net/
License: LGPLv2+
Group: Sound
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libbinio-devel
BuildRequires: chrpath

%description
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

%package -n %libname
Group: System/Libraries
Summary: Shared library of the AdPlug audio emulator

%description -n %libname
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

This package contains the shared library required to run applications
based on AdPlug.

%package -n %develname
Group: Development/C++
Summary: Development files of AdPlug
Requires: %libname = %version
Provides: libadplug-devel = %version-%release
Requires: libbinio-devel
Obsoletes: %mklibname -d %name 2.1

%description -n %develname
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

This package contains the C++ headers and documentation required for
building programs based on AdPlug.

%package -n %staticname
Group: Development/C++
Summary: Static library of AdPlug
Requires: %develname = %version
Provides: libadplug-static-devel = %version-%release
Obsoletes: %mklibname -s -d %name 2.1

%description -n %staticname
AdPlug is a free, multi-platform, hardware independent AdLib sound player
library, mainly written in C++. AdPlug plays sound data, originally created
for the AdLib (OPL2) audio board, on top of an OPL2 emulator or by using the
real hardware. No OPL2 chip is required for playback.

It supports various audio formats from MS-DOS AdLib trackers.

This package contains the static library required for statically
linking applications based on AdPlug.

%prep
%setup -q
perl -pi -e "s!/usr/local/share/adplug!%_datadir/%name!" doc/adplugdb.1

%build
export CPPFLAGS="-I%_includedir/libbinio"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
mkdir -p %buildroot%_datadir/%name
bzcat %SOURCE1 > %buildroot%_datadir/%name/adplug.db
chrpath -d %buildroot%_bindir/adplugdb

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%post -n %develname
%_install_info libadplug.info
%postun -n %develname
%_remove_install_info libadplug.info

%files
%defattr(-,root,root)
%doc README
%_bindir/adplugdb
%_mandir/man1/adplugdb.1*
%dir %_datadir/%name/
%_datadir/%name/adplug.db

%files -n %libname
%defattr(-,root,root)
%doc AUTHORS NEWS TODO COPYING
%_libdir/libadplug-%{api}.so.%{major}*

%files -n %develname
%defattr(-,root,root)
%_includedir/adplug/
%_libdir/*.so
%attr(644,root,root) %_libdir/*.la
%_infodir/libadplug.info*
%_libdir/pkgconfig/*.pc

%files -n %staticname
%defattr(-,root,root)
%_libdir/*.a
