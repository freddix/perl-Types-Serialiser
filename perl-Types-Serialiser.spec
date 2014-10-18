%include	/usr/lib/rpm/macros.perl

%define		pdir	Types
%define		pnam	Serialiser

Summary:	Simple data types for common serialisation formats
Name:		perl-types-serialiser
Version:	1.0
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	76460a2bfbc644672499af89192e03fe
URL:		http://search.cpan.org/~mlehmann/Types-Serialiser-1.0
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides some extra datatypes that are used by common
serialisation formats such as JSON or CBOR.

%prep
%setup -qn %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes COPYING README
%dir %{perl_vendorlib}/Types
%{perl_vendorlib}/Types/*.pm
%{perl_vendorlib}/Types/Serialiser
%{_mandir}/man3/Types::Serialiser.3pm*
%{_mandir}/man3/Types::Serialiser::Error.3pm*

