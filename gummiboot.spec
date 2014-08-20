# TODO
# - pesign the .efi
Summary:	Simple EFI Boot Manager
Summary(pl.UTF-8):	Prosty boot manager EFI
Name:		gummiboot
Version:	45
Release:	1
License:	LGPL v2.1+
Group:		Base
# git clone git://anongit.freedesktop.org/gummiboot
# cd gummiboot/
# ./autogen
# ./configure
# make distcheck
Source0:	http://pkgs.fedoraproject.org/repo/pkgs/gummiboot/%{name}-%{version}.tar.xz/5d4957390e959cb9f325b87712ddd3f1/gummiboot-%{version}.tar.xz
# Source0-md5:	5d4957390e959cb9f325b87712ddd3f1
URL:		http://freedesktop.org/wiki/Software/gummiboot
BuildRequires:	docbook-style-xsl
BuildRequires:	gnu-efi
BuildRequires:	libblkid-devel >= 2.20
BuildRequires:	libxslt-progs
#BuildRequires:	pesign
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libblkid >= 2.20
ExclusiveArch:	%{ix86} %{x8664} ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gummiboot is a simple UEFI boot manager which executes configured EFI
images. The default entry is selected by a configured pattern (glob)
or an on-screen menu.

gummiboot operates on the EFI System Partition (ESP) only. gummiboot
reads simple and entirely generic boot loader configuration files; one
file per boot loader entry to select from.

Configuration file fragments, kernels, initrds, other EFI images need
to reside on the ESP.

%description -l pl.UTF-8
gummiboot to prosty boot manager UEFI wywołujący skonfigurowane obrazy
EFI. Wpis domyślny jest wybierany poprez skonfigurowany wzorzec (glob)
lub menu na ekranie.

gummiboot operuje tylko na partycji systemowej EFI (ESP). Odczytuje
proste i całkowicie ogólne pliki konfiguracyjne boot loadera - jeden
plik na wpis boot loadera, spośród których można wybierać.

Składniki pliku konfiguracyjnego, jądra, initrd oraz inne obrazy EFI
muszą być obecne na partycji ESP.

%prep
%setup -q

%build
%configure \
	--bindir=%{_sbindir} \
	--disable-silent-rules \
	--libexecdir=%{_prefix}/lib

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_bindir}/gummiboot update || :

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/gummiboot
%{_mandir}/man8/gummiboot.8*
%dir %{_prefix}/lib/%{name}
%{_prefix}/lib/%{name}/gummiboot*.efi
