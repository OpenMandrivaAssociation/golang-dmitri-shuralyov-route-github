 # Run tests in check section
%bcond_without check

%global goipath         dmitri.shuralyov.com/route/github
%global commit          ce4edef1f8c9585ca16cca2f9990a099d038c0a2

%global common_description %{expand:
Router for targeting GitHub subjects.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        Router for targeting GitHub subjects
License:        BSD
URL:            %{gourl}
# git clone dmitri.shuralyov.com/route/github
# cd github
# git archive --format tar.gz --prefix github-%%{commit}/ %%{commit} > github-%%{commit}.tar.gz
Source0:        github-%{commit}.tar.gz
Source1:        https://dmitri.shuralyov.com/LICENSE

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%autosetup -n github-%{commit}
cp %{S:1} .


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.gitce4edef
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 24 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180420gitce4edef
- First package for Fedora

