%define	snap	20120426
Summary:	Asterisk huawei 3g dongle channel driver
Name:		asterisk-chan_dongle
Version:	1.1
Release:	0.%{snap}.1
License:	GPL v2
Group:		Applications
# Source0:	http://asterisk-chan-dongle.googlecode.com/files/chan_dongle-%{version}.tgz
# svn checkout http://asterisk-chan-dongle.googlecode.com/svn/trunk/ chan_dongle
Source0:	chan_dongle-%{snap}.tar.bz2
# Source0-md5:	de30dbb362a76d4783e9457c722465e8
URL:		http://wiki.e1550.mobi/
BuildRequires:	asterisk-devel >= 1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
chan_dongle is an Asterisk channel driver for Huawei UMTS/3G USB
modems (dongles). At this moment, the supported features are:

- Voice calls, dialling by modem name, group, round robin, provider
  name, IMEI or IMSI.
- Call waiting
- Call holding
- Conference (multiparty) call
- Send SMS from CLI, asterisk manager and dialplan
- Receive SMS (latin charset and multiline included)
- Send USSD
- Receive USSD (latin charset and multiline included)
- Send DTMF (excluding A,B,C,D letters not supported by Huawei)
- Receive DTMF

%prep
%setup -q -n chan_dongle

%build
install /usr/share/automake/{config.*,install-sh,missing} .
%{__aclocal}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -D etc/dongle.conf $RPM_BUILD_ROOT%{_sysconfdir}/asterisk/dongle.conf
install -D chan_dongle.so $RPM_BUILD_ROOT%{_libdir}/asterisk/modules/chan_dongle.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README.txt TODO.txt etc/extensions.conf
%attr(755,root,root) %{_libdir}/asterisk/modules/chan_dongle.so
%attr(640,root,asterisk) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/asterisk/dongle.conf
