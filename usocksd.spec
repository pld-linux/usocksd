Summary:	User-mode SOCKS5 daemon
Summary(pl):	Demon SOCKS5 dzia³aj±cy w przestrzeni u¿ytkownika
Name:		usocksd
Version:	0.9.3
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://sites.inka.de/sites/bigred/sw/%{name}-%{version}.tar.gz
# Source0-md5:	9d7876d8e11652017db5e2caa0193932
Patch0:		%{name}-axcheck.patch
URL:		http://sites.inka.de/~bigred/hadinet/usocksd.html
BuildRequires:	autoconf
BuildRequires:	automake
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
User-mode SOCKS5 daemon.

%description -l pl
Demon SOCKS5 dzia³aj±cy w przestrzeni u¿ytkownika.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D usocksd   $RPM_BUILD_ROOT%{_bindir}/usocksd
install -D usocksd.1 $RPM_BUILD_ROOT%{_mandir}/man1/usocksd.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/usocksd
%{_mandir}/man1/usocksd.1*
