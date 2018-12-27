%define api 2.3
%define major 0
%define libname %mklibname %name %api %major
%define develname %mklibname -d %name
#define staticname %mklibname -s -d %name

Summary: AdLib sound player library
Name:    adplug
Version: 2.3.1
Release: 1
Source0: https://github.com/adplug/adplug/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
#Source1: http://prdownloads.sourceforge.net/adplug/adplug.db.bz2
URL: http://adplug.sourceforge.net/
License: LGPLv2+
Group: Sound

BuildRequires: pkgconfig(libbinio)
BuildRequires: chrpath
BuildRequires: gcc-c++, gcc, gcc-cpp




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


%prep
%setup -q
#perl -pi -e "s!/usr/local/share/adplug!%_datadir/%name!" doc/adplugdb.1

%build
export CC=gcc
export CXX=g++
export CPPFLAGS="-I%_includedir/libbinio"
%configure
%make

%install
%makeinstall_std
#mkdir -p %buildroot%_datadir/%name
#bzcat %SOURCE1 > %buildroot%_datadir/%name/adplug.db
#chrpath -d %buildroot%_bindir/adplugdb


%files
%doc README
%_bindir/adplugdb
%_mandir/man1/adplugdb.1*
%dir %_datadir/%name/
%_datadir/%name/adplug.db

%files -n %libname
%doc AUTHORS NEWS TODO COPYING
%_libdir/libadplug-%{api}.so.%{major}*

%files -n %develname
%doc README
%_includedir/adplug/
%_libdir/*.so
%_infodir/libadplug.info*
%_libdir/pkgconfig/*.pc



