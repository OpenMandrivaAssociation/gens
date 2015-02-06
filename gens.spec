Name:		gens
Summary:	Sega Genesis/MegaDrive emulator
Version:	2.15.5
Release:	4
Group:		Emulators
License:	GPLv2
Url:		http://sourceforge.net/projects/gens/
Source0:	http://sourceforge.net/projects/gens/files/Gens%20Source%20Code/Gens%20%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.16.png.bz2
Source2:	%{name}.32.png.bz2
Source3:	%{name}.48.png.bz2
Patch1:		gens-libgl.patch
Patch2:		gens-rpmlint.patch
Patch3:		gens-2.15.5-strings.patch
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	nasm
ExclusiveArch:	%ix86
Conflicts:	gens-gs

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



%changelog
* Sat Jul 30 2011 Andrey Bondrov <abondrov@mandriva.org> 2.15.5-2mdv2012.0
+ Revision: 692361
- Fix BuildRequires
- Add Conflicts
- imported package gens


* Tue Jul 19 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 2.15.5-1mdv2011.0
- New version
- Major spec rewrite

* Mon Jun 11 2007 Guillaume Bedot <littletux@zarb.org> 2.12-0.2005feb13.2plf2008.0
- xdg menu, fix gui icons, autotools versions

* Sun Apr 23 2006 Michael Scherer <misc@zarb.org> 2.12-0.2005feb13.1plf
- New snapshot, close #110
- pach for gcc4 build
- use mkrel
- new menu 

* Sat Sep 25 2004 Michael Scherer <misc@zarb.org> 2.12-0.rc3.1plf 
- rc3
- fix rpmlint warning
- fix compile

* Tue Jul 22 2003 Michael Scherer <scherer.michael@free.fr> 2.12-0.rc2.2plf 
- fix description
- added a menu && icons

* Mon Jul 21 2003 Michael Scherer <scherer.michael@free.fr> 2.12-0.rc2.1plf
- initial spec

