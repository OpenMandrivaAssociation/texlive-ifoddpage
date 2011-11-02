Name:		texlive-ifoddpage
Version:	20111102
Release:	1
Summary:	TeXLive ifoddpage package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifoddpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifoddpage.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ifoddpage.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive ifoddpage package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
