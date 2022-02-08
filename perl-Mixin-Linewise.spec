#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Mixin
%define		pnam	Linewise
Summary:	Mixin::Linewise - write your linewise code for handles; this does the rest
#Summary(pl.UTF-8):	
Name:		perl-Mixin-Linewise
Version:	0.110
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/R/RJ/RJBS/Mixin-Linewise-%{version}.tar.gz
# Source0-md5:	466b2b42a0cec2b163729fa581ac4b1d
URL:		http://search.cpan.org/dist/Mixin-Linewise/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(PerlIO::utf8_strict)
BuildRequires:	perl-Sub-Exporter
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It's boring to deal with opening files for IO, converting strings to
handle-like objects, and all that.  With Mixin::Linewise::Readers and
Mixin::Linewise::Writers, you can just write a method to handle
handles, and methods for handling strings and filenames are added for
you.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Mixin
%{perl_vendorlib}/Mixin/*.pm
%{perl_vendorlib}/Mixin/Linewise
%{_mandir}/man3/*
