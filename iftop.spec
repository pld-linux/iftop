Summary:	Display bandwidth usage on an interface
Summary(pl):	Wy¶wietlanie obci±¿enia na danym interfejsie
Name:		iftop
Version:	0.17
Release:	1.1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.ex-parrot.com/~pdw/iftop/download/%{name}-%{version}.tar.gz
# Source0-md5:	062bc8fb3856580319857326e0b8752d
Patch0:		%{name}-ncurses.patch
URL:		http://www.ex-parrot.com/~pdw/iftop/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Iftop does for network usage what top(1) does for CPU usage. It
listens to network traffic on a named interface and displays a table
of current bandwidth usage by pairs of hosts. Handy for answering the
question "why is our ADSL link so slow?".

%description -l pl
Iftop jest tym w zastosowaniach sieciowych, czym top(1) w
zastosowaniach systemowych. Iftop s³ucha na danym interfejsie
sieciowym oraz wy¶wietla tabelê z aktualnym obci±¿eniem. Przydatny
przy odpowiedzi na pytanie "dlaczego moje po³±czenie ADSL jest takie
wolne?".

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
