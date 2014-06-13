# revision 23979
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-ifoddpage
Version:	20111103
Release:	7
Summary:	TeXLive ifoddpage package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifoddpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifoddpage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifoddpage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive ifoddpage package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ifoddpage/ifoddpage.sty
%doc %{_texmfdistdir}/doc/latex/ifoddpage/README
%doc %{_texmfdistdir}/doc/latex/ifoddpage/ifoddpage.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ifoddpage/ifoddpage.dtx
%doc %{_texmfdistdir}/source/latex/ifoddpage/ifoddpage.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111103-2
+ Revision: 752722
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111103-1
+ Revision: 718701
- texlive-ifoddpage
- texlive-ifoddpage
- texlive-ifoddpage
- texlive-ifoddpage

