#
# Conditional build:
# _with_tests - perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBIx
%define	pnam	AbstractLite
Summary:	DBIx::AbstractLite - Lightweight DBI SQL abstraction in a hybrid interface
#Summary(pl):	
Name:		perl-DBIx-AbstractLite
Version:	0.02
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_with_tests:1}%{!?_with_tests:0}
BuildRequires:	perl(Error::Dumb)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is based on DBIx::Abstract, but is much simpler.  It also
doesn't deviate from the DBI interface as much as DBIx::Abstract does.
The main similarity between DBIx::AbstractLite and DBIx::Abstract is in
the select method.  Unlike Abstract, AbstractLite is not 100% abstract
in that it still allows conventional access to the DBI interface, using
plain SQL and the DBI statement handle methods.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
