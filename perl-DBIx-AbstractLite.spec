#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	DBIx
%define		pnam	AbstractLite
Summary:	DBIx::AbstractLite - lightweight DBI SQL abstraction in a hybrid interface
Summary(pl.UTF-8):	DBIx::AbstractLite - lekka abstrakcja DBI SQL w hybrydowym interfejsie
Name:		perl-DBIx-AbstractLite
Version:	0.02
Release:	5
# same as perl
License:	GP v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a45ded7d5a4b80e54f6add8c161a3f42
URL:		http://search.cpan.org/dist/DBIx-AbstractLite/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Error::Dumb)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is based on DBIx::Abstract, but is much simpler. It also
doesn't deviate from the DBI interface as much as DBIx::Abstract does.
The main similarity between DBIx::AbstractLite and DBIx::Abstract is
in the select method. Unlike Abstract, AbstractLite is not 100%%
abstract in that it still allows conventional access to the DBI
interface, using plain SQL and the DBI statement handle methods.

%description -l pl.UTF-8
Ten moduł jest bazowany na DBIx::Abstract, ale jest o wiele prostszy.
Także nie odbiega od interfejsu DBI tak bardzo jak DBIx::Abstract.
Główne podobieństwo pomiędzy DBIx::AbstractLite i DBIx::Abstract to
metoda select. W przeciwieństwie do Abstract, AbstractLite nie jest w
100%% abstrakcyjny w tym, że nadal pozwala na konwencjonalny dostęp do
interfejsu DBI, przy użyciu zwykłych metod obsługi SQL i wyrażeń DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
