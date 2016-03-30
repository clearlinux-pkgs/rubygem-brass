#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-brass
Version  : 1.2.1
Release  : 4
URL      : https://rubygems.org/downloads/brass-1.2.1.gem
Source0  : https://rubygems.org/downloads/brass-1.2.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires : ruby
BuildRequires : rubygem-rdoc

%description
# BRASS
[Website](http://rubyworks.github.com/brass) /
[Report Issue](http://github.com/rubyworks/brass/issues) /
[Development](http://github.com/rubyworks/brass)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n brass-1.2.1
gem spec %{SOURCE0} -l --ruby > rubygem-brass.gemspec

%build
gem build rubygem-brass.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
brass-1.2.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/brass-1.2.1 && rubytest -I.:lib:test test/case_brass.rb && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/brass-1.2.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/.ruby
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/COPYING.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/HISTORY.rdoc
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/lib/brass.rb
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/lib/brass/adapters/minitest.rb
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/lib/brass/adapters/testunit.rb
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/lib/brass/adapters/testunit1.rb
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/lib/brass/expect.rb
/usr/lib64/ruby/gems/2.3.0/gems/brass-1.2.1/test/case_brass.rb
/usr/lib64/ruby/gems/2.3.0/specifications/brass-1.2.1.gemspec
