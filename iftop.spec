Summary:	Display bandwidth usage on an interface
Summary(pl):	Wy¶wietla obci±¿enie na danym interfejsie
Name:		iftop
Version:	0.13
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ex-parrot.com/~pdw/iftop/download/%{name}-%{version}.tar.gz
# Source0-md5: f8f7f55e4d855bf5ea581a4013226f71
Patch0:		%{name}.curses.patch
URL:		http://www.ex-parrot.com/~pdw/iftop/download/
BuildRequires:	pcre-devel
BuildRequires:  ncurses-devel
Requires:	libpcap
Requires:       ncurses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iftop does for network usage what top(1) does for CPU usage. It listens to
network traffic on a named interface and displays a table of current bandwidth
usage by pairs of hosts. Handy for answering the question "why is our ADSL
link so slow?".

%description -l pl
Iftop jest tym w zastosowaniach sieciowych, czym top(1) w zastosowaniach
systemowych. Iftop s³ucha na danym interfejsie sieciowym oraz wy¶wietla
tabelê z aktualnym obci±¿eniem. Przydatny przy odpowiedzi na pytanie
"dlaczego moje po³±czenie ADSL jest takie wolne?".

%prep
%setup -q 
%patch0 -p1

%build
rm -f missing
%{__autoconf}
%configure
%{__make} CC="%{__cc} %{rpmcflags} -Wall -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc ChangeLog README NEWS TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
