#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-brass
Version  : 1.2.1
Release  : 2
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
pushd %{buildroot}%{gem_dir}/gems/brass-1.2.1
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/brass-1.2.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Exception/assertion%3f-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Exception/cdesc-Exception.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Exception/set_assertion-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Exception/set_message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Kernel/assert-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Kernel/assert-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Kernel/cdesc-Kernel.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Kernel/expect-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Kernel/fail%21-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Kernel/fail%21-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Kernel/refute-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Kernel/refute-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/MiniTest/Unit/cdesc-Unit.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/MiniTest/cdesc-MiniTest.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Test/Unit/BrassAssertionHandler/add_brass_failure-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Test/Unit/BrassAssertionHandler/cdesc-BrassAssertionHandler.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Test/Unit/BrassAssertionHandler/handle_brass_assertion_failed_error-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Test/Unit/BrassAssertionHandler/included-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Test/Unit/TestCase/cdesc-TestCase.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Test/Unit/cdesc-Unit.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/Test/cdesc-Test.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/page-COPYING_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/page-HISTORY_rdoc.ri
/usr/lib64/ruby/gems/2.2.0/doc/brass-1.2.1/ri/page-README_md.ri
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/.ruby
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/.yardopts
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/COPYING.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/HISTORY.rdoc
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/lib/brass.rb
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/lib/brass/adapters/minitest.rb
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/lib/brass/adapters/testunit.rb
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/lib/brass/adapters/testunit1.rb
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/lib/brass/expect.rb
/usr/lib64/ruby/gems/2.2.0/gems/brass-1.2.1/test/case_brass.rb
/usr/lib64/ruby/gems/2.2.0/specifications/brass-1.2.1.gemspec
