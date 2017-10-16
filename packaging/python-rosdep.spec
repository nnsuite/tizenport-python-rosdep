Name:           python-rosdep
Version:        0.11.8
Release:        0
License:        BSD
Summary:        Package manager abstrction tool for ROS
Url:            http://wiki.ros.org/rosdep
Group:          Development/Languages/Python
Source0:        %{name}-%{version}.tar.gz
Source1001:     %{name}.manifest
BuildRequires:  python-devel
BuildRequires:  python-nose
BuildRequires:  python-catkin_pkg
BuildRequires:  python-rospkg
BuildRequires:  python-rosdistro >= 0.3.0
BuildRequires:  python-PyYAML >= 3.1
Requires:       python-catkin_pkg
Requires:       python-rospkg
Requires:       python-rosdistro >= 0.3.0
Requires:       python-PyYAML >= 3.1

%description
Command-line tool for installing system dependencies on a variety of platforms.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%{_bindir}/rosdep
%{_bindir}/rosdep-source
%{python_sitelib}/*

%changelog
