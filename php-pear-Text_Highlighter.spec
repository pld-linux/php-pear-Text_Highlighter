# TODO:
# - think about renaming generate script
# - error: php-pear-Text_Highlighter-0.6.5-1 (cnfl rails = 0.12.1-1) conflicts with installed rails-0.12.1-1
%include	/usr/lib/rpm/macros.php
%define		_class		Text
%define		_subclass	Highlighter
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - syntax highlighting
Summary(pl):	%{_pearname} - pod¶wietlanie sk³adni
Name:		php-pear-%{_pearname}
Version:	0.6.9
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	59f4f5b8cd666b5126e972ed96fd629c
URL:		http://pear.php.net/package/Text_Highlighter/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.3.3
Requires:	php-pear
Requires:	php-pear-Console_Getopt >= 1.0
Requires:	php-pear-PEAR-core >= 1:1.0
Requires:	php-pear-XML_Parser >= 1.0.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text_Highlighter is a package for syntax highlighting.

It provides a base class providing all the functionality, and a
descendent classes geneator class.

The main idea is to simplify creation of subclasses implementing
syntax highlighting for particular language. Subclasses do not
implement any new functionality, they just provide syntax highlighting
rules. The rules sources are in XML format.

To create a highlighter for a language, there is no need to code a new
class manually. Simply describe the rules in XML file and use
Text_Highlighter_Generator to create a new class.

In PEAR status of this package is: %{_status}.

%description -l pl
Text_Highlighter to pakiet do pod¶wietlania sk³adni.

Zawiera klasê bazow± dostarczaj±c± ca³± funkcjonalno¶æ i klasê
generuj±c± klasy dziedzicz±ce.

G³ówn± ide± jest uproszczenie tworzenia podklas implementuj±cych
pod¶wietlanie sk³adni dla danego jêzyka. Podklasy nie implementuj±
¿adnej nowej funkcjonalno¶ci, a jedynie dostarczaj± regu³y
pod¶wietlania sk³adni. ¬ród³a regu³ s± w formacie XML.

Aby stworzyæ pod¶wietlanie dla jêzyka, nie trzeba kodowaæ rêcznie
nowej klasy. Wystarczy opisaæ regu³y w pliku XML i u¿yæ
Text_Highlighter_Generator, aby utworzyæ now± klasê.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
%pear_package_install
install ./%{_bindir}/%{_class}/%{_subclass}/generate $RPM_BUILD_ROOT%{_bindir}/generate

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%attr(755,root,root) %{_bindir}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%{php_pear_dir}/data/%{_pearname}
