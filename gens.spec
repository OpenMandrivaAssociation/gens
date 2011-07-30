%define name gens
%define version 2.15.5
%define release %mkrel 2

Name: %{name}
Summary: Sega Genesis/MegaDrive emulator
Version: %{version}
Release: %{release}
Group:   Emulators
Source:  http://sourceforge.net/projects/gens/files/Gens%20Source%20Code/Gens%20%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.16.png.bz2
Source2: %{name}.32.png.bz2
Source3: %{name}.48.png.bz2
Patch1:  gens-libgl.patch
Patch2:  gens-rpmlint.patch
Patch3:  gens-2.15.5-strings.patch
Url:       http://sourceforge.net/projects/gens/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License: GPLv2
ExclusiveArch: %ix86
BuildRequires: gtk2-devel
BuildRequires: SDL1.2-devel
BuildRequires: nasm

%description
Gens is a GPL emulator for the genesis, ported from win32
to BeOS and linux. It was the fastest on win32, and is pretty fast on linux.

%prep
%setup -q
%patch1 -p0
%patch2 -p0
%patch3 -p1

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}%{_miconsdir}
mkdir -p %{buildroot}%{_iconsdir}
mkdir -p %{buildroot}%{_liconsdir}
mkdir -p %{buildroot}%{_menudir}
bzcat %{SOURCE1} > %{buildroot}%{_miconsdir}/%{name}.png
bzcat %{SOURCE2} > %{buildroot}%{_iconsdir}/%{name}.png
bzcat %{SOURCE3} > %{buildroot}%{_liconsdir}/%{name}.png

install -d -m 755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Gens
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Emulators;Game;Emulator;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING README INSTALL BUGS
%{_bindir}/%{name}
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}//applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png

